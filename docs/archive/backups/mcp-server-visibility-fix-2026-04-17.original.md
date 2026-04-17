# Fix MCP Server Visibility & Path Configuration

## Problem
MCP server invisible to Gemini CLI. Tools missing/fail.

## Root Cause
1. **Broken Config**: `.gemini/settings.json` missing/incomplete.
2. **Broken Venv**: Editable install point to wrong path `/home/deli/projects/mem0_local_mcp`. Should be `/home/deli/projects/mcp/mem0_local_mcp`.
3. **Naming Drift**: Tool names changed in `FastMCP` refactor (`add_memory` → `store_memory`).

## Solution
1. **Fix Venv**: Re-install project editable in `.venv`.
   ```bash
   ./.venv/bin/python -m pip install -e .
   ```
2. **Restore Settings**: Re-create `.gemini/settings.json`. Use absolute paths + `PYTHONPATH`.
   ```json
   "mem0-local-mcp": {
     "command": "/home/deli/projects/mcp/mem0_local_mcp/.venv/bin/mem0-local-mcp"
   }
   ```
3. **Sync Docs/Tests**: Update `README.md` + `tests/test_integration.py`. Use tool names:
   - `store_memory`
   - `search_memory`
   - `get_context`
4. **Mem0 v2 API Fix**: Fix `mem0ai` v2.0.0 compatibility. Detail: [Mem0 v2 API Fix](mem0-v2-api-fix-2026-04-17.md).

## Verification
- `pytest tests/test_integration.py` → PASSED.
- Shell test: `python -c "from mem0_local_mcp.mcp_server import get_context; ..."` → OK.
