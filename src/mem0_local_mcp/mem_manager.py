import os
from mem0 import Memory
from mem0_local_mcp.utils import load_env
from filelock import FileLock

# Carica le variabili d'ambiente
load_env()

class MemManager:
    VALID_CATEGORIES = {
        "axiom",
        "decision",
        "preference",
        "fact"
    }

    def __init__(self, user_id=None):
        base_path = os.environ.get("MEM0_DB_PATH", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "mem0_db")))
        
        # Ensure the directory exists
        os.makedirs(base_path, exist_ok=True)
        
        self.lock_path = os.path.join(base_path, "mem0.lock")
        self.lock = FileLock(self.lock_path)
        
        config = {
            "llm": {
                "provider": "gemini",
                "config": {
                    "model": "gemini-2.0-flash",
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
                    "path": base_path,
                    "collection_name": "mem0_gemini_768"
                }
            },
        }
        self.config = config
        with self.lock:
            self.memory = Memory.from_config(config)
        self.user_id = user_id or "default_user"

    def add(self, content, category, importance=2, rationale=None):
        if category not in self.VALID_CATEGORIES:
            raise ValueError(f"Invalid category: {category}. Must be one of {self.VALID_CATEGORIES}")
        
        if importance not in [1, 2, 3]:
            raise ValueError(f"Invalid importance: {importance}. Must be 1, 2, or 3.")

        if category == "decision" and not rationale:
            raise ValueError("Category 'decision' requires a rationale explaining the 'why'.")
        
        metadata = {
            "category": category,
            "importance": importance
        }
        if rationale:
            metadata["rationale"] = rationale
            
        with self.lock:
            res = self.memory.add(content, user_id=self.user_id, metadata=metadata, infer=False)
            return res

    def search(self, query, category=None, limit=3):
        filters = {"user_id": self.user_id}
        if category and category != "all":
            if category not in self.VALID_CATEGORIES:
                raise ValueError(f"Invalid category: {category}")
            # Try simple metadata filtering
            filters["category"] = category
            
        with self.lock:
            # filters MUST contain user_id in mem0 v2.0+
            results = self.memory.search(query, filters=filters, top_k=limit)
        
        actual_results = results.get("results", []) if isinstance(results, dict) else results
        return actual_results

    def get_all(self, category=None):
        filters = {"user_id": self.user_id}
        with self.lock:
            # Query ALL data to find where it is
            results = self.memory.get_all(filters=filters)
        
        # results is dict {"results": [...]}
        all_mems = results.get("results", []) if isinstance(results, dict) else results

        if not category or category == "all":
            return all_mems
            
        return [m for m in all_mems if m.get("metadata", {}).get("category") == category]

    def get_critical(self):
        """Return all memories with importance Level 1 (Critical)."""
        all_mems = self.get_all()
        return [m for m in all_mems if m.get("metadata", {}).get("importance") == 1]
