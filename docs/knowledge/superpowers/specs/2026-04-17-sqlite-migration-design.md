# Design: SQLite Migration for Concurrent Access

## Context
User reports "lock" errors when multiple Gemini instances attempt to access the same Mem0 storage (Qdrant in local mode). Qdrant local mode is designed for single-process access and uses file locking.

## Objective
Enable multi-instance support (concurrency) for the Mem0 MCP server by migrating from Qdrant local storage to SQLite storage.

## Architecture
- **Vector Store**: Migrate from `qdrant` to `sqlite`.
- **Provider**: Mem0 `sqlite` provider.
- **Concurrency**: SQLite's WAL (Write-Ahead Logging) mode allows multiple readers and queued writers, resolving the lock collision issue inherent in Qdrant's local file access.
- **Storage**: Single file `mem0_sqlite.db` located in the `mem0_db` directory.

## Components & Data Flow
1. **MemManager Update**:
   - Change `vector_store` configuration in `src/mem0_local_mcp/mem_manager.py`.
   - Use `sqlite` provider.
   - Point to `mem0_sqlite.db`.
2. **Environment Variables**:
   - Reuse `MEM0_DB_PATH` to determine the directory for the SQLite file.
3. **Data Migration Strategy**:
   - **Fresh Start**: Existing Qdrant data will not be migrated. A new SQLite database will be initialized on first run.
   - Legacy Qdrant files will remain on disk but will be ignored by the updated server.

## Configuration Details
```python
config = {
    "vector_store": {
        "provider": "sqlite",
        "config": {
            "path": os.path.join(db_directory, "mem0_sqlite.db"),
            "collection_name": "mem0_gemini_768",
            "embedding_model_dims": 768
        }
    },
    ...
}
```

## Error Handling
- SQLite handles concurrency internally. No manual lock management is required.
- Standard file permission checks apply to the `mem0_db` directory.

## Validation & Testing
1. **Initialization**: Verify `mem0_sqlite.db` is created in the configured path.
2. **Multi-Instance Simulation**:
   - Open Instance A: Add a memory.
   - Open Instance B: Add a memory while A is active.
   - Verify both instances can search and retrieve all memories.
3. **Persistence**: Verify data remains after server restarts.
