# Project Reorganization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrare il progetto a una struttura `src` layout moderna con `pyproject.toml` e unificare i test.

**Architecture:** Spostamento dei file sorgente in `src/mem0_local_mcp/`, adozione di `pyproject.toml` per packaging/dipendenze e aggiornamento degli import per supportare il nuovo layout.

**Tech Stack:** Python 3.x, setuptools (build backend), pytest.

---

### Task 1: Creazione Struttura Directory e __init__.py

**Files:**
- Create: `src/mem0_local_mcp/__init__.py`

- [ ] **Step 1: Creare le directory necessarie**
Run: `mkdir -p src/mem0_local_mcp`

- [ ] **Step 2: Creare `src/mem0_local_mcp/__init__.py` per esporre i membri principali**

```python
from .mcp_server import mcp, add_memory, search_memory
from .mem_manager import MemManager
from .utils import get_project_id

__all__ = ["mcp", "add_memory", "search_memory", "MemManager", "get_project_id"]
```

- [ ] **Step 3: Commit**
Run: `git add src && git commit -m "chore: initialize src directory structure"`

### Task 2: Migrazione Sorgenti e Aggiornamento Import

**Files:**
- Move: `mcp_server.py`, `mem_manager.py`, `utils.py` -> `src/mem0_local_mcp/`
- Modify: `src/mem0_local_mcp/mcp_server.py`, `src/mem0_local_mcp/mem_manager.py`

- [ ] **Step 1: Spostare i file**
Run: `mv mcp_server.py mem_manager.py utils.py src/mem0_local_mcp/`

- [ ] **Step 2: Aggiornare import in `src/mem0_local_mcp/mcp_server.py`**
Change `from mem_manager import MemManager` to `from .mem_manager import MemManager`.

- [ ] **Step 3: Aggiornare import in `src/mem0_local_mcp/mem_manager.py`**
Change `from utils import get_project_id` to `from .utils import get_project_id`.

- [ ] **Step 4: Commit**
Run: `git add src && git commit -m "refactor: move source files and update internal imports"`

### Task 3: Unificazione dei Test

**Files:**
- Move: `test_integration.py` -> `tests/`
- Modify: `tests/test_mem_manager.py`, `tests/test_utils.py`, `tests/test_integration.py`

- [ ] **Step 1: Spostare il test d'integrazione**
Run: `mv test_integration.py tests/`

- [ ] **Step 2: Aggiornare import in `tests/test_mem_manager.py`**
Change `from mem_manager import MemManager` to `from mem0_local_mcp.mem_manager import MemManager`.

- [ ] **Step 3: Aggiornare import in `tests/test_utils.py`**
Change `from utils import get_project_id` to `from mem0_local_mcp.utils import get_project_id`.

- [ ] **Step 4: Aggiornare import in `tests/test_integration.py`**
Change `from mcp_server import add_memory, search_memory` to `from mem0_local_mcp.mcp_server import add_memory, search_memory`.

- [ ] **Step 5: Commit**
Run: `git add tests && git commit -m "refactor: unify tests and update imports to use package path"`

### Task 4: Configurazione Packaging Moderno (pyproject.toml)

**Files:**
- Create: `pyproject.toml`
- Delete: `requirements.txt`

- [ ] **Step 1: Creare `pyproject.toml` con metadati e dipendenze**

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "mem0-local-mcp"
version = "0.1.0"
description = "Mem0 Local Memory MCP Server"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "mcp",
    "mem0ai",
    "pydantic",
    "python-dotenv",
]

[project.scripts]
mem0-local-mcp = "mem0_local_mcp.mcp_server:mcp.run"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
```

- [ ] **Step 2: Rimuovere `requirements.txt`**
Run: `trash requirements.txt`

- [ ] **Step 3: Commit**
Run: `git add pyproject.toml && git commit -m "build: add pyproject.toml and remove requirements.txt"`

### Task 5: Validazione e Installazione Editabile

- [ ] **Step 1: Installare in modalità editabile**
Run: `pip install -e .`

- [ ] **Step 2: Eseguire i test per verificare la correttezza**
Run: `pytest`
Expected: Tutti i test passano.

- [ ] **Step 3: Verificare l'entry point**
Run: `mem0-local-mcp --help` (o simile, a seconda di FastMCP)
Expected: Il server si avvia o mostra l'help senza errori di import.

- [ ] **Step 4: Pulizia finale (rimozione cache)**
Run: `trash __pycache__ tests/__pycache__`

- [ ] **Step 5: Commit finale**
Run: `git commit --allow-empty -m "chore: final project reorganization validation"`
