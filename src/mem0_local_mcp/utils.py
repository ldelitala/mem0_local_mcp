import hashlib
from pathlib import Path

def get_project_id(path: str = None) -> str:
    if path is None:
        path = str(Path.cwd().resolve())
    return hashlib.md5(path.encode()).hexdigest()
