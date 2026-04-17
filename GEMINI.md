# 🚀 BOOTSTRAP LOADER (GEMINI-CLI)

**STOP IMMEDIATO.** Non leggere il codice senza aver caricato la memoria a lungo termine.

## 🛑 PROTOCOLLO OBBLIGATORIO (Avvio)
Esegui ESCLUSIVAMENTE questa lettura per sincronizzarti:
1. **`docs/knowledge/index.md`**: Indice della conoscenza e mappa concettuale.
2. **`docs/daily/`**: Ultimi log operativi per contesto immediato.

## 🛠 WORKFLOW (Legge del Progetto)
1. **READ**: Carica sempre `docs/knowledge/index.md` e usa `mcp_mem0_search_memory` per contesto profondo.
2. **THINK**: Crea ADR in `docs/ADRs/` per modifiche strutturali.
3. **EXECUTE**: Modifiche chirurgiche seguendo la conoscenza in `docs/knowledge/`. **USA SEMPRE `run_shell_command` NATIVO per comandi di sistema (ls, git, pytest, etc.)**.
4. **SYNC (Real-time)**: 
   - Se modifichi tool o flussi, aggiorna IMMEDIATAMENTE gli articoli in `docs/knowledge/concepts/`.
   - **OBBLIGATORIO**: A fine task o sessione, aggiorna il log giornaliero in `docs/daily/`.
   - **OBBLIGATORIO**: Salva i "perché" delle decisioni in Mem0 via `mcp_mem0_add_memory`.
5. **WRITE**: **OBBLIGATORIO.** Aggiorna `docs/knowledge/index.md` e `docs/knowledge/log.md` prima di chiudere.

## 🧠 PROTOCOLLO MEMORIA
- **Short-term**: Diario operativo in `docs/daily/`.
- **Long-term**: Verità Tecnica in `docs/knowledge/concepts/`.
- **Episodic**: Preferenze e "perché" salvati via `mcp_mem0_add_memory`.

---
*La documentazione in `docs/` è l'unica fonte di verità sullo stato del progetto. Mantienila sincronizzata in tempo reale.*
