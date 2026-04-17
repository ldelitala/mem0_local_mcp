import asyncio
import sys
import os
from pathlib import Path

# Aggiungi 'src' al path per permettere l'importazione del modulo
src_path = str(Path(__file__).parent.parent)
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from mcp.server.fastmcp import FastMCP
from mem0_local_mcp.mem_manager import MemManager
from mem0_local_mcp.utils import load_env

# Carica API key all'avvio
load_env()

mcp = FastMCP("Mem0 Memory Server")
_mem = None
_lock = asyncio.Lock()

async def get_mem():
    global _mem
    async with _lock:
        if _mem is None:
            _mem = MemManager()
        return _mem

@mcp.tool()
async def store_insight(content: str, category: str, importance: int = 2, rationale: str = None) -> str:
    """Salva una memoria con gerarchia (1-3) e consapevolezza.
    Categorie: axiom, decision, preference, fact.
    Importanza: 1 (Critical), 2 (Standard), 3 (Low).
    Rationale: Obbligatorio per 'decision'.
    """
    mem = await get_mem()
    try:
        mem.add(content, category, importance=importance, rationale=rationale)
        return f"Stored as {category} (Level {importance})."
    except ValueError as e:
        return f"Validation Error: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

@mcp.tool()
async def search_insight(query: str, category: str = "all", limit: int = 3) -> str:
    """Cerca memorie (max {limit} risultati). Categoria opzionale.
    Mostra gerarchia e consapevolezza (Rationale).
    """
    mem = await get_mem()
    try:
        results = mem.search(query, category, limit=limit)
        if not results:
            return "No memories found."
        
        lines = []
        for r in results:
            meta = r.get("metadata", {})
            cat = meta.get("category", "unknown")
            lvl = meta.get("importance", 2)
            rationale = meta.get("rationale")
            text = r.get("memory") or r.get("text") or str(r)
            
            line = f"- [{cat}][Level {lvl}]: {text}"
            if rationale:
                line += f" (Rationale: {rationale})"
            lines.append(line)
        return "\n".join(lines)
    except ValueError as e:
        return f"Validation Error: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

@mcp.tool()
async def get_context(category: str) -> str:
    """Recupera tutte le memorie di una categoria (senza ricerca semantica).
    Ideale per caricare project_context o user_context all'avvio.
    """
    mem = await get_mem()
    try:
        results = mem.get_all(category)
        if not results:
            return f"No memories in {category}."
        
        lines = []
        for r in results:
            text = r.get("memory") or r.get("text") or str(r)
            lines.append(f"- {text}")
        return f"### {category}\n" + "\n".join(lines)
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

@mcp.resource("mem0://context/critical")
async def get_critical_context() -> str:
    """Carica automaticamente tutte le memorie di importanza 1 (Critical).
    Ideale per definire l'identità e le regole fondamentali del progetto.
    """
    mem = await get_mem()
    try:
        results = mem.get_critical()
        if not results:
            return "No critical context defined."
        
        lines = ["# Critical Project Context"]
        for r in results:
            meta = r.get("metadata", {})
            cat = meta.get("category", "axiom")
            text = r.get("memory") or r.get("text") or str(r)
            rationale = meta.get("rationale")
            
            line = f"- **{cat}**: {text}"
            if rationale:
                line += f" *(Rationale: {rationale})*"
            lines.append(line)
        return "\n".join(lines)
    except Exception as e:
        return f"Error loading critical context: {str(e)}"

if __name__ == "__main__":
    mcp.run()
