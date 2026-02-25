import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class Deck:
    """Manages a collection of cards."""

    def __init__(self):
        self.cards: list = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card by name. Returns True if removed."""
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck randomly."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw the top card from the deck."""
        if not self.cards:
            raise IndexError("Deck is empty")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        """Return deck statistics."""
        from ex1.SpellCard import SpellCard
        from ex1.ArtifactCard import ArtifactCard

        creatures = len([c for c in self.cards
                         if isinstance(c, CreatureCard)])
        spells = len([c for c in self.cards
                      if isinstance(c, SpellCard)])
        artifacts = len([c for c in self.cards
                         if isinstance(c, ArtifactCard)])
        total = len(self.cards)
        avg = sum(c.cost for c in self.cards) / total if total else 0
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg
        }
