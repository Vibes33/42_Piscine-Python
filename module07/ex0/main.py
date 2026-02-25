from ex0.CreatureCard import CreatureCard

print("=== DataDeck Card Foundation ===\n")
print("Testing Abstract Base Class Design:\n")

dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

print("CreatureCard Info:")
print(dragon.get_card_info())

print("\nPlaying Fire Dragon with 6 mana available:")
print(f"Playable: {dragon.is_playable(6)}")
print(f"Play result: {dragon.play({})}")

goblin = CreatureCard("Goblin Warrior", 2, "Common", 3, 2)
print(f"\nFire Dragon attacks Goblin Warrior:")
print(f"Attack result: {dragon.attack_target(goblin)}")

print(f"\nTesting insufficient mana (3 available):")
print(f"Playable: {dragon.is_playable(3)}")

print("\nAbstract pattern successfully demonstrated!")
