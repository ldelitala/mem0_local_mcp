---
title: "Mem0 Integration"
sources: ["daily/2026-04-17.md"]
created: 2026-04-17
updated: 2026-04-17
---
# Mem0 Integration
Integrazione della libreria mem0 per la gestione degli embeddings e della ricerca vettoriale. Utilizza Google Gemini API per la generazione di embeddings e Qdrant per lo storage locale.

## Dettagli Tecnici
- **Mem0 Engine**: Gestisce il ciclo di vita dei ricordi e la logica di associazione.
- **Storage**: Database locale situato in `mem0_db/`.
- **Embeddings**: Generati via Google Gemini API.
