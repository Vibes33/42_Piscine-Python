def print_achievement_analytics(players):
    print("=== Achievement Analytics ===")
    
    # 1. All Unique Achievements (UNION)
    # Start with empty set and unite with all player sets
    all_achievements = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    
    # Sorting for consistent display (sets are unordered by nature)
    sorted_all = sorted(all_achievements)
    print(f"All unique achievements: {set(sorted_all)}") # Printed as set for format matching
    print(f"Total unique achievements: {len(all_achievements)}")
    
    # 2. Common to ALL players (INTERSECTION)
    # Start with the first player's achievements as the base
    # Then intersect with every other player's set
    common_achievements = set(list(players.values())[0])
    for achievements in players.values():
        common_achievements = common_achievements.intersection(achievements)
        
    print(f"Common to all players: {common_achievements}")
    
    # 3. Rare Achievements (Found in exactly 1 player's list)
    # This requires counting occurrences manually since sets delete duplicates
    achievement_counts = {}
    for achievements in players.values():
        for ach in achievements:
            achievement_counts[ach] = achievement_counts.get(ach, 0) + 1
            
    rare = {ach for ach, count in achievement_counts.items() if count == 1}
    print(f"Rare achievements (1 player): {sorted(rare)}")
    
    # 4. Specific Comparisons (Alice vs Bob)
    # Requires safe access in case names change, but hardcoded for the exercise demo
    if "alice" in players and "bob" in players:
        alice_set = players["alice"]
        bob_set = players["bob"]

        # Intersection: What do they share?
        common_ab = alice_set.intersection(bob_set)
        print(f"Alice vs Bob common: {sorted(common_ab)}")
        
        # Difference: What Alice has that Bob doesn't
        alice_unique = alice_set.difference(bob_set)
        print(f"Alice unique: {sorted(alice_unique)}")
        
        # Difference: What Bob has that Alice doesn't
        bob_unique = bob_set.difference(alice_set)
        print(f"Bob unique: {sorted(bob_unique)}")

def main():
    print("=== Achievement Tracker System ===")
    
    # Creating player data using Sets directly
    # Sets are defined with {} similar to dicts but without key:value pairs
    players = {
        "alice": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "bob": {"first_kill", "level_10", "boss_slayer", "collector"},
        "charlie": {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}
    }
    
    # Display raw data
    for name, achievements in players.items():
        print(f"Player {name} achievements: {achievements}")
        
    # Analyze
    print_achievement_analytics(players)

if __name__ == "__main__":
    main()
