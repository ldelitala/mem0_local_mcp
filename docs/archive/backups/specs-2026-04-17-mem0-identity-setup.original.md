# Design: Mem0 Local MCP Agent Identity & Docs Protocol

Entry point `GEMINI.md` + `docs/` protocol. Allineamento ecosistema.

## Obiettivi
- Identità server Mem0.
- Protocollo lettura `docs/000_CORE.md`.
- Struttura base memoria (file-based).

## Architettura Documenti
1. **`GEMINI.md`**: Punto ingresso. Istruzioni, workflow.
2. **`docs/000_CORE.md`**: Dashboard stato. Task, mappa docs.
3. **`docs/MEMORY_LOG.md`**: Diario operativo.
4. **`docs/ARCHITECTURE.md`**: Tech spec MCP server, tool, storage.

## Protocollo Operativo
Sessione start: Leggi `docs/000_CORE.md`. Aggiorna `docs/MEMORY_LOG.md`. Sincronizza `docs/ARCHITECTURE.md`.
