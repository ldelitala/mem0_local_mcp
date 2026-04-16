# Design Spec: Mem0 Local MCP Memory

## Overview
Crea un server MCP locale che usa `mem0` per fornire una memoria semantica a lungo termine per l'agente. 
Permette di salvare informazioni su specifici utenti e progetti, includendo il "perché" (ragionamento/contesto).

## Architecture
- **Language:** Python 3.12+ (in `.venv`).
- **Core Library:** `mem0ai` (Python library).
- **Storage:** SQLite locale (default mem0) + Local Vector Store (ChromaDB/Qdrant default mem0).
- **Communication:** MCP Protocol via STDIO.

## Data Model
- **User Memory:** Globale (legata a `user_id` fisso).
- **Project Memory:** Isolata (legata a `project_id` derivato dall'hash del percorso cartella corrente).
- **Metadata Fields:**
  - `category`: "user" | "project"
  - `project_id`: Path-based hash
  - `reason`: Stringa descrittiva del contesto o del "perché" dell'informazione.

## MCP Tools
1. `add_memory(content: str, category: str, reason: str)`
   - Aggiunge un ricordo con metadati.
2. `search_memory(query: str, category: str = "all")`
   - Ricerca semantica filtrata per categoria e `project_id`.
3. `forget_memory(memory_id: str)`
   - Elimina un record specifico.

## Error Handling
- Fallback su `default_project` se il path non è risolvibile.
- Log degli errori di database su `stderr`.
- Risposte vuote eleganti se la ricerca non produce risultati.

## Success Criteria
- L'agente può salvare e recuperare informazioni tra diverse sessioni nello stesso progetto.
- L'agente può recuperare informazioni dell'utente anche in progetti diversi.
- Le informazioni includono esplicitamente il "perché" sono state salvate.
