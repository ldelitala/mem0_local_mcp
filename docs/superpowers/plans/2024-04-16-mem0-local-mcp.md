# Mem0 Local MCP Memory Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crea un server MCP locale che usa `mem0` per gestire memoria utente e di progetto con metadati di contesto ("perché").

**Architecture:** Server Python che implementa il protocollo MCP via STDIO, integrando la libreria `mem0ai` per la ricerca semantica e lo storage locale.

**Tech Stack:** Python 3.12+, `mcp` SDK, `mem0ai`, `hashlib`, `pathlib`.

---

### Task 1: Setup Ambiente e Dipendenze

**Files:**
- Create: `requirements.txt`
- Action: Create `.venv` and install dependencies.

- [ ] **Step 1: Create requirements.txt**

```text
mcp
mem0ai
pydantic
```

- [ ] **Step 2: Create .venv and install**

Run: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
Expected: Ambiente configurato correttamente.

- [ ] **Step 3: Commit**

```bash
git add requirements.txt
git commit -m "chore: add dependencies and setup venv"
```

---

### Task 2: Utility per Project ID

**Files:**
- Create: `utils.py`
- Test: `tests/test_utils.py`

- [ ] **Step 1: Write test for project_id calculation**

```python
import os
from utils import get_project_id

def test_get_project_id_is_consistent():
    path = os.getcwd()
    id1 = get_project_id(path)
    id2 = get_project_id(path)
    assert id1 == id2
    assert len(id1) == 32
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_utils.py`
Expected: FAIL (ModuleNotFoundError)

- [ ] **Step 3: Implement get_project_id**

```python
import hashlib
from pathlib import Path

def get_project_id(path: str = None) -> str:
    if path is None:
        path = str(Path.cwd().resolve())
    return hashlib.md5(path.encode()).hexdigest()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_utils.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add utils.py tests/test_utils.py
git commit -m "feat: add project_id utility"
```

---

### Task 3: Core Mem0 Wrapper

**Files:**
- Create: `mem_manager.py`
- Test: `tests/test_mem_manager.py`

- [ ] **Step 1: Write test for MemManager**

```python
from mem_manager import MemManager

def test_mem_manager_init():
    mgr = MemManager(user_id="test_user")
    assert mgr.user_id == "test_user"
```

- [ ] **Step 2: Implement MemManager class**

```python
from mem0 import Memory
from utils import get_project_id

class MemManager:
    def __init__(self, user_id="default_user"):
        self.user_id = user_id
        self.project_id = get_project_id()
        self.memory = Memory()

    def add(self, content, category, reason):
        metadata = {
            "category": category,
            "project_id": self.project_id if category == "project" else "global",
            "reason": reason
        }
        return self.memory.add(content, user_id=self.user_id, metadata=metadata)

    def search(self, query, category="all"):
        filters = {}
        if category == "project":
            filters = {"project_id": self.project_id}
        elif category == "user":
            filters = {"category": "user"}
        
        return self.memory.search(query, user_id=self.user_id, filters=filters)
```

- [ ] **Step 3: Commit**

```bash
git add mem_manager.py tests/test_mem_manager.py
git commit -m "feat: add MemManager core logic"
```

---

### Task 4: MCP Server Implementation

**Files:**
- Create: `mcp_server.py`

- [ ] **Step 1: Implement MCP server with tools**

```python
import asyncio
from mcp.server.fastmcp import FastMCP
from mem_manager import MemManager

mcp = FastMCP("Mem0 Memory Server")
mem = MemManager()

@mcp.tool()
async def add_memory(content: str, category: str, reason: str) -> str:
    """Aggiunge un ricordo con categoria ('user' o 'project') e il motivo (reason)."""
    result = mem.add(content, category, reason)
    return f"Memoria salvata: {result}"

@mcp.tool()
async def search_memory(query: str, category: str = "all") -> str:
    """Cerca nelle memorie. Categorie: 'user', 'project', 'all'."""
    results = mem.search(query, category)
    if not results:
        return "Nessun ricordo pertinente trovato."
    return str(results)

if __name__ == "__main__":
    mcp.run()
```

- [ ] **Step 2: Commit**

```bash
git add mcp_server.py
git commit -m "feat: implement MCP server tools"
```

---

### Task 5: Final Validation

- [ ] **Step 1: Test locally via python**

Run: `python mcp_server.py` (Verify it starts without errors, then Ctrl+C)

- [ ] **Step 2: Manual integration test script**

```python
# test_integration.py
import asyncio
from mcp_server import add_memory, search_memory

async def test():
    await add_memory("L'utente preferisce Python", "user", "Preferenza linguaggio")
    res = await search_memory("linguaggio", "user")
    print(res)

if __name__ == "__main__":
    asyncio.run(test())
```

- [ ] **Step 3: Cleanup and Docs**

Update README with instructions on how to add this to Gemini CLI.
