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
