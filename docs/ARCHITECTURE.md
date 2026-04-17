# 🏛️ ARCHITECTURE - Mem0 Local MCP

## 📝 SCOPO
Server MCP per memoria semantica a lungo termine basato su mem0.

## 🛠️ COMPONENTI
- MCP Server: Implementato in src/mem0_local_mcp/mcp_server.py.
- Mem0 Engine: Gestisce embeddings e ricerca vettoriale via Google Gemini API.
- Storage: Database Qdrant locale in mem0_db/.

## 🔧 TOOL DISPONIBILI
### add_memory
- Input: content, category (user/project), reason.
- Effetto: Salva il ricordo nel DB vettoriale.

### search_memory
- Input: query, category (user/project/all).
- Output: Lista di ricordi rilevanti.

## 📂 STRUTTURA CARTELLE
- src/: Codice sorgente.
- mem0_db/: Dati persistenti del database.
- docs/: Documentazione e protocollo memoria agente.
- tests/: Suite di test.