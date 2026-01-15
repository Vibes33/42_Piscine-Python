alice_achievements = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob_achievements = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie_achievements = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}

print("=== Achievement Tracker System ===")
print(f"Player alice achievements: {alice_achievements}")
print(f"Player bob achievements: {bob_achievements}")
print(f"Player charlie achievements: {charlie_achievements}")

print("=== Achievement Analytics ===")

all_achievements = alice_achievements.union(bob_achievements).union(charlie_achievements)
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}")

common_all = alice_achievements.intersection(bob_achievements).intersection(charlie_achievements)
print(f"Common to all players: {common_all}")

# Rare achievements: appearing in exactly one player's list
only_alice = alice_achievements.difference(bob_achievements).difference(charlie_achievements)
only_bob = bob_achievements.difference(alice_achievements).difference(charlie_achievements)
only_charlie = charlie_achievements.difference(alice_achievements).difference(bob_achievements)

rare_achievements = only_alice.union(only_bob).union(only_charlie)
print(f"Rare achievements (1 player): {rare_achievements}")

alice_bob_common = alice_achievements.intersection(bob_achievements)
print(f"Alice vs Bob common: {alice_bob_common}")

alice_unique = alice_achievements.difference(bob_achievements)
print(f"Alice unique: {alice_unique}")

bob_unique = bob_achievements.difference(alice_achievements)
print(f"Bob unique: {bob_unique}")
