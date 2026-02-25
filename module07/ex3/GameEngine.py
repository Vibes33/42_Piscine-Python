from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Game orchestrator using factory and strategy patterns."""

    def __init__(self):
        self.factory: CardFactory = None
        self.strategy: GameStrategy = None
        self.hand: list = []
        self.battlefield: list = []
        self.turns: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        try:
            self.hand = [
                self.factory.create_creature(),
                self.factory.create_creature("goblin"),
                self.factory.create_spell()
            ]
            self.cards_created += len(self.hand)
            result = self.strategy.execute_turn(self.hand, self.battlefield)
            self.turns += 1
            self.total_damage += result.get("damage_dealt", 0)
            return result
        except Exception as e:
            return {"error": str(e)}

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": (self.strategy.get_strategy_name()
                              if self.strategy else "None"),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
