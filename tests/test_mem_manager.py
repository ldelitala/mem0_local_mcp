from mem_manager import MemManager

def test_mem_manager_init():
    mgr = MemManager(user_id="test_user")
    assert mgr.user_id == "test_user"
