import os
import sys

# Aggiungi src al path per importare il modulo locale
sys.path.append(os.path.join(os.getcwd(), "src"))

try:
    from mem0_local_mcp.mem_manager import MemManager
    
    print("Inizializzazione MemManager...")
    mgr = MemManager(user_id="test_user")
    
    print("Aggiunta memoria di test...")
    mgr.add("Nuova memoria di test specifica per oggi.", category="test", reason="debug")
    
    print("Ricerca memorie totali...")
    results = mgr.search("memoria")
    
    print(f"\nRisultati trovati ({len(results)}):")
    print(f"DEBUG: tipo_risultati={type(results)}")
    for r in results:
        print(f"DEBUG: tipo_r={type(r)}, contenuto_r={r}")
        if isinstance(r, dict):
            memory_text = r.get('memory', r.get('content', 'N/A'))
        else:
            memory_text = str(r)
        print(f"- {memory_text}")

except Exception as e:
    print(f"ERRORE durante il test: {e}")
