# Mem0 Local MCP Memory

Server MCP per la gestione della memoria semantica a lungo termine (User & Project) usando `mem0`.

## Installazione in Gemini CLI

Aggiungi la configurazione al tuo file di configurazione di Gemini CLI:

```json
{
  "mcpServers": {
    "mem0": {
      "command": "/home/deli/projects/mem0_local_mcp/.venv/bin/mem0-local-mcp",
      "env": {
        "GOOGLE_API_KEY": "LA_TUA_CHIAVE_QUI",
        "MEM0_DB_PATH": "/home/deli/projects/mem0_local_mcp/mem0_db"
      }
    }
  }
}
```

## Tool Disponibili

- `add_memory(content, category, reason)`: Salva un'informazione. Category può essere 'user' o 'project'.
- `search_memory(query, category)`: Cerca informazioni salvate.

## Sviluppo

1. Attiva venv: `source .venv/bin/activate`
2. Installa in modalità editabile: `pip install -e .`
3. Run server: `mem0-local-mcp`
4. Run test: `pytest`
