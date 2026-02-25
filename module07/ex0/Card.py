from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract base class for all cards in DataDeck."""

    def __init__(self, name: str, cost: int, rarity: str):
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play the card. Must be implemented by subclasses."""
        pass

    def get_card_info(self) -> dict:
        """Return card information."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if the card can be played with available mana."""
        return available_mana >= self.cost
