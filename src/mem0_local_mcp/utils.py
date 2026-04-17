import os
import hashlib
from pathlib import Path

def load_env():
    # Carica la chiave API se non presente
    if not os.environ.get("GOOGLE_API_KEY"):
        if os.path.exists(".env"):
            with open(".env", "r") as f:
                for line in f:
                    if line.startswith("GOOGLE_API_KEY="):
                        os.environ["GOOGLE_API_KEY"] = line.split("=", 1)[1].strip()
                        break

def get_project_id(path: str = None) -> str:
    if path is None:
        path = str(Path.cwd().resolve())
    return hashlib.md5(path.encode()).hexdigest()
