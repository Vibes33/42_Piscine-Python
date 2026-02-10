def create_archive():
    filename = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {filename}")
    
    file = None
    try:
        # Ouverture du fichier en mode écriture ('w' = write)
        # ATTENTION : Si le fichier existe déjà, 'w' efface tout son contenu !
        # Si le fichier n'existe pas, il est créé.
        file = open(filename, "w")
        print("Storage unit created successfully...")
        print("Inscribing preservation data...")
        
        # Données à écrire
        entries = [
            "[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee"
        ]
        
        for entry in entries:
            print(entry) # Simulation de l'affichage terminal
            file.write(entry + "\n") # Écriture réelle dans le fichier (+ saut de ligne)
            
        print("Data inscription complete. Storage unit sealed.")
        
    except IOError as e:
        print(f"ERROR: Failed to write to storage unit: {e}")
        
    finally:
        if file:
            file.close() # Toujours sceller l'archive !
            print(f"Archive '{filename}' ready for long-term preservation.")

if __name__ == "__main__":
    create_archive()
