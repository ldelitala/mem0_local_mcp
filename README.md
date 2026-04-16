# Mem0 Local MCP Server

Un server MCP (Model Context Protocol) che fornisce una memoria semantica a lungo termine per agenti AI, basato su [mem0](https://github.com/mem0ai/mem0). Permette di memorizzare e recuperare informazioni organizzate per categorie (**User** e **Project**).

## Caratteristiche

- **Memoria Persistente**: Utilizza Qdrant (locale) per lo storage dei vettori.
- **Isolamento**: Distingue tra ricordi personali dell'utente e ricordi specifici del progetto corrente.
- **Integrazione Gemini**: Configurato per utilizzare le API Gemini per embeddings e LLM.
- **Layout Standard**: Segue il layout `src/` e utilizza `pyproject.toml` per il packaging moderno.

## Requisiti

- Python 3.10+
- Una chiave API di Google Gemini (`GOOGLE_API_KEY`).

## Installazione

Per installare il server in modalità editabile nel tuo ambiente locale:

```bash
git clone https://github.com/ldelitala/mem0_local_mcp.git
cd mem0_local_mcp
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Configurazione in Gemini CLI

Aggiungi il server al tuo file di configurazione (`config.json` o equivalente):

```json
{
  "mcpServers": {
    "mem0": {
      "command": "python",
      "args": ["-m", "mem0_local_mcp.mcp_server"],
      "env": {
        "GOOGLE_API_KEY": "TUA_API_KEY_QUI",
        "MEM0_DB_PATH": "/percorso/assoluto/a/mem0_db"
      }
    }
  }
}
```

*Nota: Se hai installato il pacchetto, puoi anche usare il comando `mem0-local-mcp` direttamente se il path del venv è configurato.*

## Tool Disponibili

### `add_memory`
Salva un nuovo pezzo di informazione nella memoria.
- `content`: Il testo da ricordare.
- `category`: 'user' (per ricordi globali) o 'project' (per quelli legati al progetto corrente).
- `reason`: Il motivo per cui questa informazione viene salvata.

### `search_memory`
Cerca informazioni rilevanti nella memoria semantica.
- `query`: La stringa di ricerca.
- `category`: 'user', 'project' o 'all' (default: 'all').

## Variabili d'Ambiente

| Variabile | Descrizione | Default |
|-----------|-------------|---------|
| `GOOGLE_API_KEY` | Chiave API per Gemini (Obbligatoria) | - |
| `MEM0_DB_PATH` | Percorso dove salvare i dati di Qdrant | `./mem0_db` |

## Sviluppo e Test

Il progetto utilizza `pytest` per la suite di test. I test del database sono isolati utilizzando directory temporanee per evitare conflitti di lock.

```bash
# Esegui tutti i test
pytest

# Esegui i test di integrazione
pytest tests/test_integration.py
```

## Licenza

MIT
