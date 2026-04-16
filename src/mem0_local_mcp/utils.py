import os

def load_env():
    # Carica la chiave API se non presente
    if not os.environ.get("GOOGLE_API_KEY"):
        with open(".env", "r") as f:
            for line in f:
                if line.startswith("GOOGLE_API_KEY="):
                    os.environ["GOOGLE_API_KEY"] = line.split("=", 1)[1].strip()
                    break
