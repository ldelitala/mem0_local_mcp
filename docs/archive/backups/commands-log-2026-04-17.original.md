# Comandi Usati - Sessione 2026-04-17

Comandi per ambiente Python 3.14, fix dipendenze, test concorrenza.

## Python & Environment
```bash
# Downgrade setuptools per fix pkg_resources
pip install "setuptools<70"

# Installazione dipendenze progetto
pip install -e .
pip install filelock chromadb mem0ai fastmcp
```

## Testing & Concurrency
```bash
# Esecuzione test integrazione
pytest tests/test_integration.py

# Test manuale concorrenza multi-processo
python3 test_concurrency.py
```

## File Management
```bash
# Spostamento file (safe)
mv -n <source> <dest>

# Eliminazione file (safe)
trash <path>
```
