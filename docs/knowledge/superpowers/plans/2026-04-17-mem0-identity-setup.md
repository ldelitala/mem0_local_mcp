# Mem0 Identity and Docs Protocol Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish the identity and self-managed memory protocol for `mem0_local_mcp` agent.

**Architecture:** Create a root `GEMINI.md` entry point and a `docs/` directory with standardized dashboard, log, and architecture files.

**Tech Stack:** Markdown, Gemini CLI Protocol.

---

### Task 1: Create GEMINI.md

**Files:**
- Create: `/home/deli/projects/mem0_local_mcp/GEMINI.md`

- [ ] **Step 1: Write GEMINI.md content**

```markdown
# 🚀 BOOTSTRAP LOADER (GEMINI-CLI)

**STOP IMMEDIATO.** Non leggere il codice senza aver caricato la memoria a lungo termine.

## 🛑 PROTOCOLLO OBBLIGATORIO (Avvio)
Esegui ESCLUSIVAMENTE questa lettura per sincronizzarti:
1. **`docs/000_CORE.md`**: Indice della memoria, mappe e stato task attivo.

## 🛠 WORKFLOW (Legge del Progetto)
1. **READ**: Carica sempre `docs/000_CORE.md` e usa `mcp_mem0_search_memory` per contesto profondo.
2. **THINK**: Crea ADR in `docs/ADRs/` per modifiche strutturali.
3. **EXECUTE**: Modifiche chirurgiche seguendo i `docs/ARCHITECTURE.md` approvati. **USA SEMPRE `run_shell_command` NATIVO per comandi di sistema (ls, git, pytest, etc.)**.
4. **SYNC (Real-time)**: 
   - Se modifichi tool o flussi, aggiorna IMMEDIATAMENTE `docs/ARCHITECTURE.md`.
   - **OBBLIGATORIO**: A fine task o sessione, aggiorna `docs/MEMORY_LOG.md`.
   - **OBBLIGATORIO**: Salva i "perché" delle decisioni in Mem0 via `mcp_mem0_add_memory`.
5. **WRITE**: **OBBLIGATORIO.** Aggiorna `docs/000_CORE.md` (Dashboard) e `docs/MEMORY_LOG.md` prima di chiudere.

## 🧠 PROTOCOLLO MEMORIA
- **Short-term**: Diario operativo in `docs/MEMORY_LOG.md`.
- **Long-term**: Verità Tecnica in `docs/ARCHITECTURE.md`.
- **Episodic**: Preferenze e "perché" salvati via `mcp_mem0_add_memory`.

---
*La documentazione in `docs/` è l'unica fonte di verità sullo stato del progetto. Mantienila sincronizzata in tempo reale.*
```

- [ ] **Step 2: Commit**

```bash
git add GEMINI.md
git commit -m "feat: add GEMINI.md entry point and docs protocol"
```

### Task 2: Initialize docs/000_CORE.md

**Files:**
- Create: `/home/deli/projects/mem0_local_mcp/docs/000_CORE.md`

- [ ] **Step 1: Write 000_CORE.md content**

```markdown
# 🗺️ CORE DASHBOARD - Mem0 Local MCP

## 📍 MAPPA DOCUMENTAZIONE
- [ARCHITECTURE.md](./ARCHITECTURE.md) - Verità Tecnica e Design.
- [MEMORY_LOG.md](./MEMORY_LOG.md) - Diario operativo e storico modifiche.
- [superpowers/specs/](../docs/superpowers/specs/) - Specifiche dei feature.

## 🎯 STATO TASK ATTIVI
- [x] Setup Identità Agente e Protocollo Docs (2026-04-17)
- [ ] Implementazione test suite per tool MCP
- [ ] Ottimizzazione gestione errori database

## 🛠️ CONTESTO ATTUALE
Il server MCP è funzionale e fornisce tool `add_memory` e `search_memory`. 
Stato attuale: Allineamento all'ecosistema agenti completato.
```

- [ ] **Step 2: Commit**

```bash
git add docs/000_CORE.md
git commit -m "docs: initialize 000_CORE.md dashboard"
```

### Task 3: Initialize docs/MEMORY_LOG.md

**Files:**
- Create: `/home/deli/projects/mem0_local_mcp/docs/MEMORY_LOG.md`

- [ ] **Step 1: Write MEMORY_LOG.md content**

```markdown
# 📜 MEMORY LOG - Mem0 Local MCP

## 2026-04-17
### Identity Setup
- Creato `GEMINI.md` con protocollo di avvio obbligatorio.
- Inizializzata struttura `docs/` con `000_CORE.md`, `MEMORY_LOG.md` e `ARCHITECTURE.md`.
- Obiettivo: Rendere l'agente mem0_local_mcp conforme agli standard dell'ecosistema Deli.
```

- [ ] **Step 2: Commit**

```bash
git add docs/MEMORY_LOG.md
git commit -m "docs: initialize MEMORY_LOG.md"
```

### Task 4: Initialize docs/ARCHITECTURE.md

**Files:**
- Create: `/home/deli/projects/mem0_local_mcp/docs/ARCHITECTURE.md`

- [ ] **Step 1: Write ARCHITECTURE.md content**

```markdown
# 🏛️ ARCHITECTURE - Mem0 Local MCP

## 📝 SCOPO
Server MCP per memoria semantica a lungo termine basato su `mem0`.

## 🛠️ COMPONENTI
- **MCP Server**: Implementato in `src/mem0_local_mcp/mcp_server.py`.
- **Mem0 Engine**: Gestisce embeddings e ricerca vettoriale via Google Gemini API.
- **Storage**: Database Qdrant locale in `mem0_db/`.

## 🔧 TOOL DISPONIBILI
### `add_memory`
- Input: `content`, `category` (user/project), `reason`.
- Effetto: Salva il ricordo nel DB vettoriale.

### `search_memory`
- Input: `query`, `category` (user/project/all).
- Output: Lista di ricordi rilevanti.

## 📂 STRUTTURA CARTELLE
- `src/`: Codice sorgente.
- `mem0_db/`: Dati persistenti del database.
- `docs/`: Documentazione e protocollo memoria agente.
- `tests/`: Suite di test.
```

- [ ] **Step 2: Commit**

```bash
git add docs/ARCHITECTURE.md
git commit -m "docs: initialize ARCHITECTURE.md"
```
