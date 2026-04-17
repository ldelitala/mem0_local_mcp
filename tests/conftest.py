import pytest
import os
import tempfile
import shutil

@pytest.fixture
def temp_db_path():
    """Crea una directory temporanea per il database mem0."""
    tmp_dir = tempfile.mkdtemp()
    old_db_path = os.environ.get("MEM0_DB_PATH")
    os.environ["MEM0_DB_PATH"] = tmp_dir
    yield tmp_dir
    if old_db_path:
        os.environ["MEM0_DB_PATH"] = old_db_path
    else:
        del os.environ["MEM0_DB_PATH"]
    shutil.rmtree(tmp_dir)
