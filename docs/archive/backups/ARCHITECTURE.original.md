---
title: "MCP Server Architecture"
sources: ["daily/2026-04-17.md"]
created: 2026-04-17
updated: 2026-04-17
---
# MCP Server Architecture
Architettura server MCP per memoria semantica. Python. Tool lettura/scrittura.

## Componenti e Tool
- **MCP Server**: `src/mem0_local_mcp/mcp_server.py`.
- **store_memory**: Salva ricordi in DB vettoriale (content, category, reason).
- **search_memory**: Ricerca ricordi (query, categoria).
