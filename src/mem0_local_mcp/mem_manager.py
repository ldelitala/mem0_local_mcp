import os
from mem0 import Memory

class MemManager:
    def __init__(self, user_id=None):
        base_path = os.environ.get("MEM0_DB_PATH", os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "mem0_db"))
        
        # Ensure the directory exists
        os.makedirs(base_path, exist_ok=True)
        
        config = {
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
        return self.memory.add(memory, user_id=self.user_id, category=category, reason=reason)

    def search(self, query):
        return self.memory.search(query, user_id=self.user_id)
