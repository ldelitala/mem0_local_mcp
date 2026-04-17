import os
from mem0 import Memory
from mem0_local_mcp.utils import load_env

# Carica le variabili d'ambiente
load_env()

class MemManager:
    def __init__(self, user_id=None):
        base_path = os.environ.get("MEM0_DB_PATH", os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "mem0_db"))
        
        # Ensure the directory exists
        os.makedirs(base_path, exist_ok=True)
        
        config = {
            "llm": {
                "provider": "gemini",
                "config": {
                    "model": "gemini-2.5-flash",
                    "api_key": os.environ.get("GOOGLE_API_KEY")
                }
            },
            "embedder": {
                "provider": "gemini",
                "config": {
                    "model": "models/gemini-embedding-001",
                    "api_key": os.environ.get("GOOGLE_API_KEY")
                }
            },
            "vector_store": {
                "provider": "chroma",
                "config": {
                    "path": base_path
                }
            },
        }
        self.memory = Memory.from_config(config)
        self.user_id = user_id

    def add(self, memory, category=None, reason=None):
        metadata = {"category": category, "reason": reason} if category or reason else None
        return self.memory.add(memory, user_id=self.user_id, metadata=metadata)

    def search(self, query):
        filters = {"user_id": self.user_id} if self.user_id else None
        results = self.memory.search(query, filters=filters)
        return results.get("results", []) if isinstance(results, dict) else results
