---
title: Miglioramento Testing e Pulizia Workspace
date: 2026-04-18
category: test-failures
problem_type: knowledge
track: knowledge
module: tests
tags: [pytest, unit-testing, mocking, architecture]
---

# Miglioramento Testing e Pulizia Workspace

## Context
Workspace con test ridondanti, file di test sparsi nella root e mancanza di isolamento (database persistenti condivisi tra i test). Necessità di una struttura di testing robusta per il mantenimento futuro.

## Guidance
1.  **Isolamento DB**: Usare fixture di `pytest` in `conftest.py` per creare directory temporanee per ogni test.
2.  **Unit vs Integration**: Separare unit test (con mock) da integration test (chiamate reali).
3.  **Robustezza Async**: Gestire l'eventuale latenza di indicizzazione asincrona (es. `mem0`/`chromadb`) con piccoli delay o fallback strategici.
4.  **Pulizia Workspace**: Mantenere la root pulita spostando i test in `tests/` e i backup in `docs/archive/backups/`.

## Why This Matters
Previene collisioni di dati tra test, riduce i falsi negativi dovuti a latenza di rete/DB e mantiene il progetto conforme agli standard di ordine.

## When to Apply
Applicare ogni volta che si aggiungono nuove funzionalità al manager di memoria o si riscontrano instabilità nei test di integrazione.

## Examples
### Fixture Isolamento (conftest.py)
```python
@pytest.fixture
def temp_db_path():
    tmp_dir = tempfile.mkdtemp()
    os.environ["MEM0_DB_PATH"] = tmp_dir
    yield tmp_dir
    shutil.rmtree(tmp_dir)
```

### Mocking MemManager (test_unit.py)
```python
@pytest.fixture
def mock_memory():
    with patch("mem0_local_mcp.mem_manager.Memory") as mocked:
        yield mocked.from_config.return_value
```
