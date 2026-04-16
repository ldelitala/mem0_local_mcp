import os
from utils import get_project_id

def test_get_project_id_is_consistent():
    path = os.getcwd()
    id1 = get_project_id(path)
    id2 = get_project_id(path)
    assert id1 == id2
    assert len(id1) == 32
