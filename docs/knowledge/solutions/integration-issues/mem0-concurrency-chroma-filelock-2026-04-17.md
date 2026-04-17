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
Implementing concurrent access support for Mem0 MCP server to handle multiple simultaneous requests (sessions) without database locking or initialization failures. Local vector stores like Qdrant and Milvus Lite use file locking that prevents multi-process access.

## Symptoms
- `Open local milvus failed`
- `Database is locked`
- `ValidationError: Unsupported vector store provider: sqlite` (when attempting a non-existent provider)

## What Didn't Work
- **'sqlite' provider**: Attempted based on an implementation plan, but discovered `mem0ai` v2.0.0 does not support `sqlite` as a vector store provider.
- **Milvus Lite**: Failed in multi-process environments because it requires exclusive access to the `.db` file during initialization and write operations.
- **Qdrant (Local)**: Similarly uses file locks that collide when multiple Gemini sessions start the MCP server.

## Solution
Switched to **ChromaDB** as the vector store backend and implemented `filelock` to synchronize database initialization and critical operations across multiple MCP server processes.

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
            # ... other config
        }
        
        with self.lock:
            # Synchronize Memory initialization and setup
            self.memory = Memory.from_config(config)

    def add(self, content, category):
        with self.lock:
            # Note: add still supports top-level user_id in v2.0.0
            return self.memory.add(content, user_id=self.user_id, metadata={"category": category}, infer=False)

    def search(self, query):
        with self.lock:
            # CRITICAL: search requires filters dictionary in v2.0.0+
            return self.memory.search(query, filters={"user_id": self.user_id})
```

## Why This Works
ChromaDB handles concurrent reads more gracefully than Qdrant/Milvus in local mode. The `FileLock` serializes access to the initialization routine and write operations. While this introduces a slight latency during high-load startup (serialization of LLM/Embedder setup), it effectively mitigates "Database is locked" errors and race conditions across multiple processes.

## Prevention
- Always verify supported providers in the library source code (e.g., `.venv/lib/python3.14/site-packages/mem0/vector_stores/configs.py`) before planning migrations.
- Use `filelock` to wrap initialization of local file-based database clients when deployment involves multi-process access (like FastMCP tools).

## Related Issues
- [[docs/knowledge/superpowers/plans/2026-04-17-sqlite-migration.md]]: Plan for concurrency support.
- [[docs/knowledge/superpowers/specs/2026-04-17-sqlite-migration-design.md]]: Original (obsolete) design.
