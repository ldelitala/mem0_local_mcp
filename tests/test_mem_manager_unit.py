import pytest
from unittest.mock import MagicMock, patch
from mem0_local_mcp.mem_manager import MemManager

@pytest.fixture
def mock_memory():
    with patch("mem0_local_mcp.mem_manager.Memory") as mocked:
        instance = mocked.from_config.return_value
        yield instance

def test_mem_manager_initialization(temp_db_path, mock_memory):
    mgr = MemManager(user_id="test_user")
    assert mgr.user_id == "test_user"
    assert mgr.lock_path.startswith(temp_db_path)

def test_add_memory_valid_category(mock_memory):
    mgr = MemManager(user_id="test_user")
    mgr.add("some content", "fact", importance=2)
    
    mock_memory.add.assert_called_once_with(
        "some content", 
        user_id="test_user", 
        metadata={"category": "fact", "importance": 2},
        infer=False
    )

def test_add_decision_requires_rationale(mock_memory):
    mgr = MemManager(user_id="test_user")
    # Missing rationale for decision
    with pytest.raises(ValueError, match="requires a rationale"):
        mgr.add("chose python", "decision")
    
    # Valid decision
    mgr.add("chose python", "decision", rationale="speed")
    mock_memory.add.assert_called_with(
        "chose python",
        user_id="test_user",
        metadata={"category": "decision", "importance": 2, "rationale": "speed"},
        infer=False
    )

def test_add_invalid_importance():
    mgr = MemManager(user_id="test_user")
    with pytest.raises(ValueError, match="Invalid importance"):
        mgr.add("content", "fact", importance=5)

def test_add_memory_invalid_category():
    mgr = MemManager(user_id="test_user")
    with pytest.raises(ValueError, match="Invalid category"):
        mgr.add("content", "invalid_cat")

def test_search_memory(mock_memory):
    mgr = MemManager(user_id="test_user")
    mock_memory.search.return_value = {"results": [{"content": "found it"}]}
    
    results = mgr.search("query", category="fact", limit=5)
    
    mock_memory.search.assert_called_once_with(
        "query", 
        filters={"user_id": "test_user", "category": "fact"},
        top_k=5
    )
    assert len(results) == 1
    assert results[0]["content"] == "found it"

def test_get_all_filtering(mock_memory):
    mgr = MemManager(user_id="test_user")
    mock_memory.get_all.return_value = {
        "results": [
            {"metadata": {"category": "preference"}, "content": "pref info"},
            {"metadata": {"category": "axiom"}, "content": "axiom info"}
        ]
    }
    
    results = mgr.get_all(category="preference")
    assert len(results) == 1
    assert results[0]["content"] == "pref info"

def test_get_critical(mock_memory):
    mgr = MemManager(user_id="test_user")
    mock_memory.get_all.return_value = {
        "results": [
            {"metadata": {"category": "axiom", "importance": 1}, "content": "critical info"},
            {"metadata": {"category": "fact", "importance": 2}, "content": "normal info"}
        ]
    }
    
    results = mgr.get_critical()
    assert len(results) == 1
    assert results[0]["content"] == "critical info"

def test_get_critical_empty(mock_memory):
    mgr = MemManager(user_id="test_user")
    mock_memory.get_all.return_value = {"results": []}
    assert mgr.get_critical() == []
