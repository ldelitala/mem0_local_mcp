# Design: SQLite Migration for Concurrent Access

## Context
Lock errors in Qdrant local mode. Multi-instance fail.

## Objective
Multi-instance support. Migrate to SQLite.

## Architecture
- **Vector Store**: `sqlite`.
- **Provider**: Mem0 `sqlite`.
- **Concurrency**: SQLite WAL mode.
- **Storage**: `mem0_sqlite.db` in `mem0_db/`.

## Components
1. **MemManager Update**: `sqlite` provider configuration.
2. **Env Vars**: `MEM0_DB_PATH`.
3. **Migration Strategy**: Fresh start. Ignore Qdrant.

## Configuration
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

## Validation
Initialization, multi-instance simulation, persistence.
