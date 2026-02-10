def main():
    print("=== Game Analytics Dashboard ===")
   
    # Sample Data (Raw Database)
    # A list of dictionaries representing player records
    data = [
        {"name": "alice",   "score": 2300, "status": "active",   "region": "north",   "achievements": ["first_kill", "level_10", "boss_slayer"]},
        {"name": "bob",     "score": 1800, "status": "inactive", "region": "east",    "achievements": ["level_10"]},
        {"name": "charlie", "score": 2150, "status": "active",   "region": "north",   "achievements": ["first_kill", "speed_demon"]},
        {"name": "diana",   "score": 2050, "status": "active",   "region": "central", "achievements": ["boss_slayer", "collector"]},
        {"name": "eve",     "score": 900,  "status": "banned",   "region": "east",    "achievements": []}
    ]

    # 1. LIST COMPREHENSIONS (Transformer les listes)
    # Syntaxe: [ expression for item in list if condition ]
    print("\n=== List Comprehension Examples ===")
    
    # Filtrer: Noms des joueurs avec un score > 2000
    high_scorers = [p["name"] for p in data if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    
    # Transformer: Liste de statuts en majuscules
    player_statuses = [p["status"].upper() for p in data]
    print(f"Player statuses: {player_statuses}")
    
    # Calculs: Doubler les scores (Simulation de bonus)
    bonus_scores = [p["score"] * 2 for p in data]
    print(f"Scores with 2x bonus: {bonus_scores}")

    # 2. DICT COMPREHENSIONS (Créer des maps)
    # Syntaxe: { key_expr: value_expr for item in list if condition }
    print("\n=== Dict Comprehension Examples ===")
    
    # Mapping simple: Nom -> Score
    score_map = {p["name"]: p["score"] for p in data}
    print(f"Player scores: {score_map}")
    
    # Mapping avec calcul: Nom -> Nombre d'achievements
    ach_count = {p["name"]: len(p["achievements"]) for p in data}
    print(f"Achievement counts: {ach_count}")
    
    # Filtrage dans la dict comp: Nom -> Score seulement pour les actifs
    active_scores = {p["name"]: p["score"] for p in data if p["status"] == "active"}
    print(f"Active player scores: {active_scores}")

    # 3. SET COMPREHENSIONS (Unicité)
    # Syntaxe: { expression for item in list if condition }
    print("\n=== Set Comprehension Examples ===")
    
    # Trouver les régions uniques (élimine les doublons automatiquement)
    regions = {p["region"] for p in data}
    print(f"Active regions: {regions}")
    
    # Trouver tous les achievements uniques (Nested loop dans une compréhension !)
    # "Pour chaque joueur p, pour chaque ach dans ses achievements, garde ach"
    unique_achievements = {ach for p in data for ach in p["achievements"]}
    print(f"Unique achievements: {unique_achievements}")

    # 4. COMBINED ANALYSIS (Petit bonus)
    print("\n=== Combined Analysis ===")
    
    total_score = sum([p["score"] for p in data]) # List comp passée à sum()
    avg_score = total_score / len(data)
    
    # Trouver le meilleur joueur (celui qui a le max score)
    # On utilise max() avec une clé personnalisée, pas une compréhension, mais c'est pour l'analyse
    top_player = max(data, key=lambda x: x["score"])
    
    print(f"Total players: {len(data)}")
    print(f"Average score: {avg_score:.1f}")
    print(f"Top performer: {top_player['name']} ({top_player['score']} points)")

if __name__ == "__main__":
    main()
