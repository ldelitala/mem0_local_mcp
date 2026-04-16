import asyncio
from mcp.server.fastmcp import FastMCP
from .mem_manager import MemManager

mcp = FastMCP("Mem0 Memory Server")
_mem = None

def get_mem():
    global _mem
    if _mem is None:
        _mem = MemManager()
    return _mem

@mcp.tool()
async def add_memory(content: str, category: str, reason: str) -> str:
    """Aggiunge un ricordo con categoria ('user' o 'project') e il motivo (reason)."""
    mem = get_mem()
    result = mem.add(content, category, reason)
    return f"Memoria salvata: {result}"

@mcp.tool()
async def search_memory(query: str, category: str = "all") -> str:
    """Cerca nelle memorie. Categorie: 'user', 'project', 'all'."""
    mem = get_mem()
    results = mem.search(query, category)
    if not results:
        return "Nessun ricordo pertinente trovato."
    return str(results)

if __name__ == "__main__":
    mcp.run()
