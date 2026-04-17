# Build Log
## [2026-04-17] integration | Mem0 v2 API Refactor
- Fix `ValueError: frozenset({'user_id'})`. Move `user_id` to `filters` in `get_all` + `search`.
- Align `MemManager` to `mem0ai` v2.0.0.
- Verify memory load via integration tests + shell.

## [2026-04-17] integration | MCP Visibility & Configuration Fix
- Restore `.gemini/settings.json`. Entry point `mem0-local-mcp`.
- Fix corrupted path in venv editable.
- Align tool names in `README.md` + `tests/test_integration.py` (`store_memory`, `search_memory`, `get_context`).
- Verify server + `MemManager` integration.

## [2026-04-17] migration | Final sync & consolidation
- Complete migration to Karpathy-style vault.
- Consolidate log + architecture to atomic concepts.
- Sync KB with setup plan.

## [2026-04-17] concurrency | SQLite migration redirected to Chroma + FileLock
- SQLite vector store not supported by `mem0ai` v2.0.0.
- Implement multi-process concurrency via ChromaDB + `filelock`.
- Fix syntax in `mcp_server.py`. Align `__init__.py`.
- Fix `search()` signature (user_id in filters).
- Concurrency test passed. No lock errors.

## [2026-04-17T15:00:00] migration | Initial structure setup
- Migrate docs/ to vault structure.
