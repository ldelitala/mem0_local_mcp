import asyncio
import os
from mcp_server import add_memory, search_memory

async def test():
    print("Testing add_memory...")
    res_add = await add_memory("L'utente preferisce Python per lo sviluppo backend", "user", "Preferenza linguaggio utente")
    print(res_add)
    
    print("\nTesting search_memory...")
    res_search = await search_memory("quale linguaggio preferisce l'utente?", "user")
    print(res_search)

if __name__ == "__main__":
    asyncio.run(test())
