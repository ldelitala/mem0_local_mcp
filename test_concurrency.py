import os
import sys
import multiprocessing

# Aggiungi src al path
sys.path.append(os.path.join(os.getcwd(), "src"))

def run_session(session_id, memory_text):
    try:
        from src.mem0_local_mcp.mem_manager import MemManager
        print(f"[{session_id}] Inizializzazione...")
        mgr = MemManager(user_id=session_id)
        
        print(f"[{session_id}] Aggiunta: {memory_text}")
        mgr.add(memory_text, category="concurrency_test")
        
        print(f"[{session_id}] Ricerca...")
        results = mgr.search(memory_text)
        
        found = any(memory_text in str(r) for r in results)
        print(f"[{session_id}] Trovato: {found}")
        return found
    except Exception as e:
        print(f"[{session_id}] ERRORE: {e}")
        return False

if __name__ == "__main__":
    print("Inizio test concorrenza (2 sessioni simultanee)...")
    
    p1 = multiprocessing.Process(target=run_session, args=("session_A", "Ricordo segreto di Alice"))
    p2 = multiprocessing.Process(target=run_session, args=("session_B", "Ricordo segreto di Bob"))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("\nTest completato.")
