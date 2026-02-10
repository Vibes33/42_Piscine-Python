import sys

def recover_data():
    filename = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {filename}")
    
    file = None # Initialisation de la variable file
    
    try:
        # Ouverture du fichier en mode lecture ('r' = read)
        file = open(filename, "r")
        print("Connection established...")
        
        # Lecture du contenu entier
        content = file.read()
        
        print("RECOVERED DATA:")
        print(content)
        
    except FileNotFoundError:
         print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        # Le bloc finally s'execute TOUJOURS, qu'il y ait erreur ou non.
        # C'est l'endroit parfait pour fermer le fichier proprement.
        print("Data recovery complete. Storage unit disconnected.")
        if file:
            file.close()

if __name__ == "__main__":
    recover_data()
