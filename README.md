# Mem0 Local MCP Memory

Server MCP per la gestione della memoria semantica a lungo termine (User & Project) usando `mem0`.

## Installazione in Gemini CLI

Aggiungi la configurazione al tuo file di configurazione di Gemini CLI:

```json
{
  "mcpServers": {
    "mem0": {
      "command": "/home/deli/projects/mem0_local_mcp/.venv/bin/python",
      "args": ["/home/deli/projects/mem0_local_mcp/mcp_server.py"],
      "env": {
        "GOOGLE_API_KEY": "LA_TUA_CHIAVE_QUI"
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
2. Run server: `python mcp_server.py`
