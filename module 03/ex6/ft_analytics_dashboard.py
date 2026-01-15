# Sample Data
# We use a list of dictionaries to represent our raw data
players_data = [
    {"name": "alice",   "score": 2300, "role": "tank",    "achievements": ["first_kill", "level_10", "brave", "lucky", "rich"], "region": "north"},
    {"name": "bob",     "score": 1800, "role": "healer",  "achievements": ["first_kill", "level_10", "builder"], "region": "east"},
    {"name": "charlie", "score": 2150, "role": "dps",     "achievements": ["level_10", "boss_slayer", "lucky", "rich", "helper", "vip", "legend"], "region": "central"},
    {"name": "diana",   "score": 2050, "role": "tank",    "achievements": ["first_kill", "speed_run"], "region": "north"}
]

print("=== Game Analytics Dashboard ===")

# 1. List Comprehensions
# Syntax: [expression for item in iterable if condition]
print("=== List Comprehension Examples ===")

# Filter: Get names of players with score > 2000
high_scorers = [p["name"] for p in players_data if p["score"] > 2000]
print(f"High scorers (>2000): {high_scorers}")

# Transform: Create a list of scores doubled (e.g., for a bonus event)
doubled_scores = [p["score"] * 2 for p in players_data]
print(f"Scores doubled: {doubled_scores}")

# Filter + Transform: Get names of 'tank' players
tank_players = [p["name"] for p in players_data if p["role"] == "tank"]
print(f"Tank players: {tank_players}")


# 2. Dict Comprehensions
# Syntax: {key_expression: value_expression for item in iterable if condition}
print("=== Dict Comprehension Examples ===")

# Mapping: Create a dictionary of name -> score
player_scores = {p["name"]: p["score"] for p in players_data}
print(f"Player scores: {player_scores}")

# Mapping with calculation: name -> achievement count
achievement_counts = {p["name"]: len(p["achievements"]) for p in players_data}
print(f"Achievement counts: {achievement_counts}")

# Categorization/Grouping logic using comprehension
# We assign a category based on score
score_categories_map = {
    p["name"]: "high" if p["score"] > 2000 else "medium" if p["score"] > 1500 else "low"
    for p in players_data
}
print(f"Player categories: {score_categories_map}")


# 3. Set Comprehensions
# Syntax: {expression for item in iterable if condition}
# Useful for deduplication
print("=== Set Comprehension Examples ===")

# Extract unique regions
unique_regions = {p["region"] for p in players_data}
print(f"Active regions: {unique_regions}")

# Flatten nested lists: Get all unique achievements across all players
# Uses nested loop syntax inside comprehension: for p in data for ach in p['achievements']
unique_achievements = {ach for p in players_data for ach in p["achievements"]}
print(f"Unique achievements ({len(unique_achievements)}): {unique_achievements}")


# 4. Combined Analysis
print("=== Combined Analysis ===")

total_players = len(players_data)
average_score = sum([p["score"] for p in players_data]) / total_players

# Find top performer using max() with a key (lambda usually, or simple max of values)
# Since we need the name, we can sort or use max on the tuple (score, name)
best_score = max([p["score"] for p in players_data])
# Find the player with that score using a list comp
top_player_name = [p["name"] for p in players_data if p["score"] == best_score][0]
top_player_ach_count = achievement_counts[top_player_name]

print(f"Total players: {total_players}")
print(f"Total unique achievements: {len(unique_achievements)}")
print(f"Average score: {average_score}")
print(f"Top performer: {top_player_name} ({best_score} points, {top_player_ach_count} achievements)")
