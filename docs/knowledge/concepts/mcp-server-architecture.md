---
title: "MCP Server Architecture"
sources: ["daily/2026-04-17.md"]
created: 2026-04-17
updated: 2026-04-17
---
# MCP Server Architecture
Architettura del server MCP per la gestione della memoria semantica. Implementato in Python con supporto per tool di lettura e scrittura.

## Componenti e Tool
- **MCP Server**: Implementato in `src/mem0_local_mcp/mcp_server.py`.
- **add_memory**: Salva ricordi nel database vettoriale (content, category, reason).
- **search_memory**: Ricerca ricordi tramite query e categoria.
