def secure_vault_access():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    
    filename = "classified_vault.txt"
    protected_data = """[CLASSIFIED] Quantum encryption keys recovered
[CLASSIFIED] Archive integrity: 100%"""

    # 1. Étape préliminaire : Créer le fichier pour pouvoir le lire ensuite
    # On utilise 'with' même pour la création pour être propre
    try:
        with open(filename, "w") as vault:
             vault.write(protected_data)
        # Note : Ici, le fichier est déjà fermé automatiquement grâce au 'with' !
    except IOError as e:
        print(f"Error initializing vault: {e}")
        return

    # 2. SECURE EXTRACTION (Lecture avec 'with')
    try:
        # C'est ici la magie de l'exercice :
        # 'with open(...) as file' remplace 'file = open(...)' + 'file.close()'
        with open(filename, "r") as vault:
            print("Vault connection established with failsafe protocols")
            print("SECURE EXTRACTION:")
            
            content = vault.read()
            print(content)
            
        # Dès qu'on sort du bloc 'with' (l'indentation), le fichier est fermé.
        # Même si un crash (exception) arrive dans le bloc, Python le fermera avant de crasher.
        
    except FileNotFoundError:
        print("Error: Vault not found.")
    except Exception as e:
        print(f"Security Breach: {e}")

    # 3. SECURE PRESERVATION (Écriture avec 'with')
    print("SECURE PRESERVATION:")
    try:
        # On rouvre le fichier en mode "ajout" ('a' = append) pour ne pas écraser l'existant
        with open(filename, "a") as vault:
            new_protocol = "\n[CLASSIFIED] New security protocols archived"
            vault.write(new_protocol)
            print("[CLASSIFIED] New security protocols archived")
            
        print("Vault automatically sealed upon completion")
            
    except Exception as e:
        print(f"Security Breach during preservation: {e}")

    print("All vault operations completed with maximum security.")

if __name__ == "__main__":
    secure_vault_access()
