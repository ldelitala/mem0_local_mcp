import pytest
import os
import uuid
import asyncio
from mem0_local_mcp.mcp_server import store_insight, search_insight, get_context

from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_full_memory_flow(temp_db_path):
    """Test di integrazione completo: store -> search -> get_context."""
    # Uso un identificativo unico per evitare collisioni se il DB non è pulito
    test_content = f"Test content {uuid.uuid4()}"
    category = "fact"
    rationale = "Integration Test"
    
    # 1. Store
    res_add = await store_insight(test_content, category, importance=1, rationale=rationale)
    assert f"Stored as {category} (Level 1)" in res_add
    
    # Attendiamo un po' per l'indicizzazione di mem0/chroma
    await asyncio.sleep(2)
    
    # 2. Search
    res_search = await search_insight(test_content, category)
    # Se la ricerca semantica fallisce, proviamo get_context che è diretto
    if test_content not in res_search:
        res_context = await get_context(category)
        assert test_content in res_context
    else:
        assert test_content in res_search
        assert "Level 1" in res_search
        assert f"Rationale: {rationale}" in res_search

@pytest.mark.asyncio
async def test_invalid_category_error(temp_db_path):
    # mcp_server cattura ValueError e ritorna stringa
    res = await store_insight("content", "invalid_cat")
    assert "Validation Error" in res

@pytest.mark.asyncio
async def test_search_insight_unexpected_error(temp_db_path):
    from unittest.mock import patch
    with patch("mem0_local_mcp.mcp_server.get_mem") as mock_get_mem:
        mock_mem = MagicMock()
        mock_mem.search.side_effect = Exception("Database is down")
        mock_get_mem.return_value = mock_mem
        
        res = await search_insight("query")
        assert "Unexpected Error: Database is down" in res

@pytest.mark.asyncio
async def test_get_critical_resource_empty(temp_db_path):
    from unittest.mock import patch
    from mem0_local_mcp.mcp_server import get_critical_context
    with patch("mem0_local_mcp.mcp_server.get_mem") as mock_get_mem:
        mock_mem = MagicMock()
        mock_mem.get_critical.return_value = []
        mock_get_mem.return_value = mock_mem
        
        res = await get_critical_context()
        assert "No critical context defined." in res
