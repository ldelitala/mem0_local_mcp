# Design: Mem0 Local MCP Agent Identity & Docs Protocol

Implementazione dell'entry point `GEMINI.md` e del protocollo di documentazione `docs/` per il progetto `mem0_local_mcp`, allineandolo agli altri agenti dell'ecosistema.

## Obiettivi
- Definire l'identità del server Mem0 come agente autonomo.
- Stabilire il protocollo obbligatorio di lettura `docs/000_CORE.md` all'avvio.
- Creare la struttura base per la memoria a lungo termine (file-based).

## Architettura dei Documenti
1. **`GEMINI.md`**: Punto di ingresso. Contiene le istruzioni di sistema, i workflow e i protocolli di sicurezza.
2. **`docs/000_CORE.md`**: Dashboard dello stato. Elenca i task attivi e la mappa della documentazione.
3. **`docs/MEMORY_LOG.md`**: Diario operativo per tracciare modifiche e decisioni.
4. **`docs/ARCHITECTURE.md`**: Descrizione tecnica del server MCP, dei tool e dello storage.

## Protocollo Operativo
All'inizio di ogni sessione, l'agente deve:
1. Leggere `docs/000_CORE.md`.
2. Aggiornare `docs/MEMORY_LOG.md` con le attività svolte.
3. Sincronizzare eventuali modifiche ai contratti in `docs/ARCHITECTURE.md`.
