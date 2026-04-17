import pytest
from mem0_local_mcp.mem_manager import MemManager
import os
import shutil

# Mocking OpenAI to avoid requiring an API key for tests
from unittest.mock import MagicMock
import sys

# Configure environment for tests
os.environ["OPENAI_API_KEY"] = "sk-mock-key"

def test_sqlite_concurrency():
    db_path = "tests/temp_mem0_db"
    if os.path.exists(db_path):
        shutil.rmtree(db_path)
    os.makedirs(db_path)
    os.environ["MEM0_DB_PATH"] = db_path
    
    # Instance 1
    m1 = MemManager(user_id="user1")
    
    # Mock adding to avoid actual API call
    m1.memory.add = MagicMock(return_value=True)
    m1.add("Memory from instance 1", category="fact", importance=2, rationale="testing")
    
    # Instance 2 (Concurrent)
    m2 = MemManager(user_id="user1")
    m2.memory.add = MagicMock(return_value=True)
    m2.add("Memory from instance 2", category="fact", importance=2, rationale="testing")
    
    # For search, we need a real result mock
    m1.memory.search = MagicMock(return_value=[
        {"memory": "Memory from instance 1"},
        {"memory": "Memory from instance 2"}
    ])
    
    results = m1.search("Memory")
    assert len(results) >= 2
    
    shutil.rmtree(db_path)
