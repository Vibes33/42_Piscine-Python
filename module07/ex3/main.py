from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

print("=== DataDeck Game Engine ===\n")
print("Configuring Fantasy Card Game...")

factory = FantasyCardFactory()
strategy = AggressiveStrategy()
engine = GameEngine()
engine.configure_engine(factory, strategy)

print(f"Factory: FantasyCardFactory")
print(f"Strategy: {strategy.get_strategy_name()}")
print(f"Available types: {factory.get_supported_types()}")

print("\nSimulating aggressive turn...")
hand = [
    factory.create_creature(),
    factory.create_creature("goblin"),
    factory.create_spell()
]
hand_str = ", ".join(f"{c.name} ({c.cost})" for c in hand)
print(f"Hand: [{hand_str}]")

print("\nTurn execution:")
result = engine.simulate_turn()
print(result)

print(f"\nGame Report:")
print(engine.get_engine_status())

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
