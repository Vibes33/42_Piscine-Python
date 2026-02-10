import sys
import os

def crisis_handler(filename):
    """
    Tente d'acceder a un fichier et gere les crises (erreurs) specifiques.
    """
    # Affichage de l'alerte
    if "lost" in filename or "classified" in filename:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
    else:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")

    try:
        # TENTATIVE D'ACCES
        # Le 'with' garantit que le fichier sera ferme proprement quoi qu'il arrive
        with open(filename, "r") as archive:
            content = archive.read().strip()
            print(f"SUCCESS: Archive recovered - '{content}'")
            print("STATUS: Normal operations resumed")
            
    # GESTION DES CRISES
    
    except FileNotFoundError:
        # Cas 1 : Le fichier n'existe pas
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        
    except PermissionError:
        # Cas 2 : On n'a pas les droits pour lire (fichier verrouille)
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        
    except Exception as e:
        # Cas 3 : Autre probleme (ex: c'est un dossier et pas un fichier)
        print(f"RESPONSE: Unexpected anomaly detected: {e}")
        print("STATUS: Crisis handled, system stable")

def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    
    # Test 1: Fichier manquant
    crisis_handler("lost_archive.txt")
    
    # Test 2: Fichier interdit (Permissions)
    crisis_handler("classified_vault.txt")
    
    # Test 3: Fichier normal
    crisis_handler("standard_archive.txt")
    
    print("All crisis scenarios handled successfully. Archives secure.")

if __name__ == "__main__":
    main()
