def main():
    try:
        filename = "ancient_fragment.txt"
        print(f"Generateur de donnees: Creation du fichier {filename}...")
        
        content = """[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion"""
        
        # Mode 'w' pour ecrire (write)
        file = open(filename, "w")
        file.write(content)
        file.close()
        
        print("Succes: Fichier cree dans le dossier courant.")
        print("Vous pouvez maintenant lancer l'exercice : python3 ft_ancient_text.py")
        
    except Exception as e:
        print(f"Erreur lors de la creation : {e}")

if __name__ == "__main__":
    main()
