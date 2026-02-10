import sys

def main():
    """
    Gestion des flux standards :
    - sys.stdout : Pour afficher (sortie standard)
    - sys.stdin  : Pour lire (entrée standard)
    - sys.stderr : Pour les erreurs/alertes (sortie d'erreur)
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    try:
        # 1. Demander l'ID
        # On utilise stdout car c'est l'ordinateur qui PARLE (affiche la question)
        sys.stdout.write("Input Stream active. Enter archivist ID: ")
        sys.stdout.flush() # IMPORTANT : Force l'affichage immédiat du texte
        
        # On utilise stdin car c'est l'ordinateur qui ECOUTE (reçoit la réponse)
        archivist_id = sys.stdin.readline().strip()

        # 2. Demander le rapport
        sys.stdout.write("Input Stream active. Enter status report: ")
        sys.stdout.flush() # Force l'affichage
        status_report = sys.stdin.readline().strip()
        
        # Vérification basique
        if not archivist_id or not status_report:
            sys.stderr.write("Error: Empty input received.\n")
            return

        # 3. Afficher le message standard (Canal STDOUT)
        sys.stdout.write(f"[STANDARD] Archive status from {archivist_id}: {status_report}\n")
        
        # 4. Afficher l'alerte (Canal STDERR)
        sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
        
        # Fin de transmission
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        
        print("Three-channel communication test successful.")
        
    except KeyboardInterrupt:
        sys.stdout.write("\nOperation cancelled.\n")

if __name__ == "__main__":
    main()
