# Comandi Usati - Sessione 2026-04-18

Pulizia workspace, refactoring test e documentazione compound.

## Testing & Environment
```bash
# Esecuzione test dal venv
.venv/bin/python -m pytest tests/

# Esecuzione test specifico con output
.venv/bin/python -m pytest -s tests/test_integration.py
```

## File Management
```bash
# Pulizia cache e file temporanei
trash .pytest_cache
find . -name "__pycache__" -type d -exec trash {} +

# Spostamento test dalla root
git mv test_concurrency.py tests/
git mv test_mem0_fix.py tests/

# Gestione backup (original.md)
find . -name "*.original.md" -exec mv -n {} docs/archive/backups/ \;
```
