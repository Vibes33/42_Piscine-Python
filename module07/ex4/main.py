from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

print("=== DataDeck Tournament Platform ===\n")
print("Registering Tournament Cards...")

dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, "dragon_001")
wizard = TournamentCard("Ice Wizard", 4, "Rare", 4, 6, "wizard_001")
wizard.rating = 1150

platform = TournamentPlatform()
platform.register_card(dragon)
platform.register_card(wizard)

print(f"\nFire Dragon (ID: dragon_001):")
print(f"  - Interfaces: [Card, Combatable, Rankable]")
print(f"  - Rating: {dragon.rating}")
print(f"  - Record: {dragon.wins}-{dragon.losses}")

print(f"\nIce Wizard (ID: wizard_001):")
print(f"  - Interfaces: [Card, Combatable, Rankable]")
print(f"  - Rating: {wizard.rating}")
print(f"  - Record: {wizard.wins}-{wizard.losses}")

print("\nCreating tournament match...")
result = platform.create_match("dragon_001", "wizard_001")
print(f"Match result: {result}")

print("\nTournament Leaderboard:")
for line in platform.get_leaderboard():
    print(f"  {line}")

print(f"\nPlatform Report:")
print(platform.generate_tournament_report())

print("\n=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
