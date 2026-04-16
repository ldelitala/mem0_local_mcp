import os
import tempfile
from mem0_local_mcp.mem_manager import MemManager

def test_mem_manager_init():
    with tempfile.TemporaryDirectory() as tmp_dir:
        os.environ["MEM0_DB_PATH"] = tmp_dir
        mgr = MemManager(user_id="test_user")
        assert mgr.user_id == "test_user"
