import pytest
from mem0_local_mcp.mem_manager import MemManager
import os
import shutil

def test_sqlite_concurrency():
    db_path = "tests/temp_mem0_db"
    if os.path.exists(db_path):
        shutil.rmtree(db_path)
    os.makedirs(db_path)
    os.environ["MEM0_DB_PATH"] = db_path
    
    # Instance 1
    m1 = MemManager(user_id="user1")
    m1.add("Memory from instance 1", category="user", reason="testing")
    
    # Instance 2 (Concurrent)
    m2 = MemManager(user_id="user1")
    m2.add("Memory from instance 2", category="user", reason="testing")
    
    results = m1.search("Memory")
    # Should contain at least 2 memories
    assert len(results) >= 2
    
    shutil.rmtree(db_path)
