---
module: mem0-local-mcp
date: 2026-04-17
problem_type: integration_issue
component: database
severity: high
symptoms:
  - "Mem0 sqlite provider hallucination"
  - "Multi-process lock issues in local vector stores (Qdrant/Milvus)"
  - "Concurrency failures in multi-client MCP sessions"
root_cause: thread_violation
resolution_type: code_fix
tags:
  - mem0
  - chroma
  - filelock
  - sqlite
  - concurrency
---

# Concurrent Access Support for Mem0 MCP Server

## Problem
Concurrent access for Mem0 MCP server. Local vector stores (Qdrant/Milvus) use file locking. Fail on multi-process access.

## Symptoms
- `Open local milvus failed`
- `Database is locked`
- `ValidationError: Unsupported vector store provider: sqlite`

## What Didn't Work
- **'sqlite' provider**: `mem0ai` v2.0.0 not support `sqlite` vector store.
- **Milvus Lite**: Fail in multi-process. Need exclusive access.
- **Qdrant (Local)**: File locks collide on multiple sessions.

## Solution
Switch to **ChromaDB**. Use `filelock` to sync database init + critical ops.

```python
import os
from filelock import FileLock

class MemManager:
    def __init__(self, user_id=None):
        base_path = "mem0_db"
        self.lock = FileLock(os.path.join(base_path, "mem0.lock"))
        
        config = {
            "vector_store": {
                "provider": "chroma",
                "config": {"path": base_path}
            },
            # ...
        }
        
        with self.lock:
            self.memory = Memory.from_config(config)

    def add(self, content, category):
        with self.lock:
            return self.memory.add(content, user_id=self.user_id, metadata={"category": category}, infer=False)

    def search(self, query):
        with self.lock:
            return self.memory.search(query, filters={"user_id": self.user_id})
```

## Why This Works
ChromaDB handle concurrent reads well. `FileLock` serialize init + writes. Mitigate lock errors/race conditions.

## Prevention
- Verify providers in library source before migration.
- Use `filelock` for local file-based DB in multi-process (FastMCP).

## Related Issues
- [[docs/knowledge/superpowers/plans/2026-04-17-sqlite-migration.md]]
- [[docs/knowledge/superpowers/specs/2026-04-17-sqlite-migration-design.md]]
