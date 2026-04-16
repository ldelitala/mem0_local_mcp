# SQLite Migration for Concurrent Access Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate Mem0 storage from Qdrant to SQLite to allow concurrent access by multiple Gemini instances.

**Architecture:** Update `MemManager` to use the `sqlite` provider. Storage will be centralized in a single `.db` file in the existing `mem0_db` directory.

**Tech Stack:** Python, mem0ai, SQLite.

---

### Task 1: Environment and Dependency Check

**Files:**
- Modify: `pyproject.toml` (if needed)

- [ ] **Step 1: Verify sqlite dependency**

Mem0 usually includes sqlite support by default, but we should verify.

Run: `pip show mem0ai`
Expected: Check if it's installed. If not, we might need to update dependencies.

- [ ] **Step 2: Commit (if changes made)**

```bash
git add pyproject.toml
git commit -m "chore: ensure dependencies for sqlite"
```

### Task 2: Update MemManager to use SQLite

**Files:**
- Modify: `src/mem0_local_mcp/mem_manager.py`

- [ ] **Step 1: Update configuration in `MemManager.__init__`**

```python
<<<<
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "path": os.environ.get("MEM0_DB_PATH", os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "mem0_db")),
                    "collection_name": "mem0_gemini_768",
                    "embedding_model_dims": 768
                }
            },
====
            "vector_store": {
                "provider": "sqlite",
                "config": {
                    "path": os.path.join(os.environ.get("MEM0_DB_PATH", os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "mem0_db")), "mem0_sqlite.db")
                }
            },
>>>>
```

- [ ] **Step 2: Verify code changes**

Ensure `import os` is present and `os.path.join` is used correctly to create the full path to the `.db` file.

- [ ] **Step 3: Commit**

```bash
git add src/mem0_local_mcp/mem_manager.py
git commit -m "feat: migrate vector store from qdrant to sqlite"
```

### Task 3: Validation and Integration Test

**Files:**
- Create: `tests/test_sqlite_concurrency.py`

- [ ] **Step 1: Write concurrency test**

```python
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
    assert len(results) >= 2
    
    shutil.rmtree(db_path)
```

- [ ] **Step 2: Run the test**

Run: `pytest tests/test_sqlite_concurrency.py`
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add tests/test_sqlite_concurrency.py
git commit -m "test: add sqlite concurrency validation test"
```

### Task 4: Cleanup (Optional/Manual)

- [ ] **Step 1: Inform user about old Qdrant files**

The old `mem0_db` folder contains Qdrant files that are no longer used. They can be deleted manually to save space.
