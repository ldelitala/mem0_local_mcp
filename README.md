# Mem0 Local MCP Server

Server MCP locale per gestire memoria semantica persistente utilizzando `mem0` e ChromaDB. Supporta l'accesso concorrente multi-processo tramite un sistema di file-locking.

## Caratteristiche
- **Memoria Semantica**: Memorizza e ricerca informazioni basate sul contesto.
- **Multi-processo**: Sicuro per l'uso con molteplici sessioni Gemini CLI contemporanee.
- **Local-first**: I dati sono salvati localmente in `mem0_db/`.

## Requisiti
- Python 3.10+ (Testato su 3.14 con `setuptools<70`)
- Chiave API Google (per embeddings e LLM) impostata in `.env`

## Installazione
1. Clona la repository.
2. Crea un ambiente virtuale e installa le dipendenze:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install "setuptools<70"
   pip install -e .
   ```
3. Configura il file `.env`:
   ```env
   GOOGLE_API_KEY=tua_chiave_qui
   ```

## Tool Disponibili
- `store_memory(content: str, category: str, reason: str = None)`: Salva una nuova informazione in una categoria.
- `search_memory(query: str, category: str = "all", limit: int = 3)`: Cerca memorie rilevanti (semantica).
- `get_context(category: str)`: Recupera tutte le memorie di una categoria (lista completa).

## Sviluppo e Test
Per verificare la concorrenza:
```bash
python test_concurrency.py
```
