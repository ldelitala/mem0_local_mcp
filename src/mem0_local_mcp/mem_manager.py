import os
from dotenv import load_dotenv
from mem0 import Memory
from .utils import get_project_id

load_dotenv()

class MemManager:
    def __init__(self, user_id="default_user"):
        self.user_id = user_id
        self.project_id = get_project_id()
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "path": "./mem0_db",
                    "collection_name": "mem0_gemini_768",
                    "embedding_model_dims": 768
                }
            },
            "embedder": {
                "provider": "gemini",
                "config": {
                    "model": "gemini-embedding-001",
                    "api_key": os.environ.get("GOOGLE_API_KEY")
                }
            },
            "llm": {
                "provider": "gemini",
                "config": {
                    "model": "gemini-2.0-flash",
                    "api_key": os.environ.get("GOOGLE_API_KEY")
                }
            }
        }
        self.memory = Memory.from_config(config)

    def add(self, content, category, reason):
        metadata = {
            "category": category,
            "project_id": self.project_id if category == "project" else "global",
            "reason": reason
        }
        return self.memory.add(content, user_id=self.user_id, metadata=metadata)

    def search(self, query, category="all"):
        filters = {"user_id": self.user_id}
        if category == "project":
            filters["project_id"] = self.project_id
        elif category == "user":
            filters["category"] = "user"
        
        return self.memory.search(query, filters=filters)
