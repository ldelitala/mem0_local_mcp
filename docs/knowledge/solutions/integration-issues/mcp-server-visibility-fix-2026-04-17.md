# Fix MCP Server Visibility & Path Configuration

## Problem
MCP server not visible to Gemini CLI. Tools like `add_memory` (old name) failing or missing.

## Root Cause
1. **Broken Config**: `.gemini/settings.json` missing or incomplete after KB migration.
2. **Broken Venv**: Editable install (`pip install -e .`) pointing to non-existent path `/home/deli/projects/mem0_local_mcp` instead of `/home/deli/projects/mcp/mem0_local_mcp`.
3. **Naming Drift**: Tool names changed during `FastMCP` refactor (`add_memory` -> `store_memory`).

## Solution
1. **Fix Venv**: Re-install project in editable mode within `.venv`.
   ```bash
   ./.venv/bin/python -m pip install -e .
   ```
2. **Restore Settings**: Re-create `.gemini/settings.json` with correct absolute paths and `PYTHONPATH`.
   ```json
   "mem0-local-mcp": {
     "command": "/home/deli/projects/mcp/mem0_local_mcp/.venv/bin/mem0-local-mcp"
   }
   ```
3. **Sync Docs/Tests**: Update `README.md` and `tests/test_integration.py` to use current tool names:
   - `store_memory`
   - `search_memory`
   - `get_context`
4. **Mem0 v2 API Fix**: Resolved compatibility issues with `mem0ai` v2.0.0. See [Mem0 v2 API Fix](mem0-v2-api-fix-2026-04-17.md) for technical details.

## Verification
- Run `pytest tests/test_integration.py` -> PASSED.
- Shell test: `python -c "from mem0_local_mcp.mcp_server import get_context; ..."` -> OK.
