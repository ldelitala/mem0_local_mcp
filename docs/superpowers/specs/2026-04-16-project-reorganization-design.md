# Design Spec: Project Reorganization and Modernization

Design per la migrazione del progetto `mem0_local_mcp` verso una struttura `src` layout e standard di packaging moderni (`pyproject.toml`).

## 1. Obiettivi
- Organizzare il codice sorgente in modo professionale e scalabile.
- Adottare standard Python moderni per la gestione delle dipendenze e dell'installazione.
- Unificare i test in una directory dedicata.
- Pulire la root del progetto dai file di logica.

## 2. Nuova Architettura File

```text
/
├── src/
│   └── mem0_local_mcp/
│       ├── __init__.py      # Espone i membri pubblici
│       ├── mcp_server.py    # Logica server MCP
│       ├── mem_manager.py   # Gestione Mem0
│       └── utils.py         # Utility
├── tests/
│   ├── test_mem_manager.py
│   ├── test_utils.py
│   └── test_integration.py  # Spostato dalla root
├── docs/
│   └── ...                  # Struttura esistente preservata
├── pyproject.toml           # Sostituisce requirements.txt
├── .env                     # Configurazioni locali
├── .gitignore
└── README.md
```

## 3. Dettagli Implementativi

### 3.1 Packaging (`pyproject.toml`)
Verrà configurato un file `pyproject.toml` usando `setuptools` come build-backend.
- **Dipendenze**: Trasferite da `requirements.txt`.
- **Scripts**: Definizione di un entry point `mem0-local-mcp` per avviare il server.

### 3.2 Refactoring Import
Tutti gli import interni dovranno passare da import relativi/locali a import assoluti basati sul pacchetto (es. `from mem0_local_mcp.utils import ...`).

### 3.3 Test Environment
Aggiornamento della configurazione `pytest` per supportare il `src` layout (solitamente automatico con `pip install -e .`).

## 4. Piano di Migrazione (Sintesi)
1. Creazione cartelle `src/mem0_local_mcp/`.
2. Spostamento file `.py` di logica.
3. Creazione `__init__.py`.
4. Spostamento `test_integration.py` in `tests/`.
5. Creazione `pyproject.toml` basato su `requirements.txt`.
6. Aggiornamento import in tutti i file.
7. Verifica installazione in modalità editabile e test.
