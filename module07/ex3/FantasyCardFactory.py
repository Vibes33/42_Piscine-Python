from typing import Union
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Creates fantasy-themed cards."""

    def create_creature(self, name_or_power: Union[str, int, None] = None) -> Card:
        if isinstance(name_or_power, str):
            if "goblin" in name_or_power.lower():
                return CreatureCard("Goblin Warrior", 2, "Common", 3, 2)
            return CreatureCard(name_or_power, 5, "Rare", 5, 4)
        power = name_or_power if isinstance(name_or_power, int) else 7
        return CreatureCard("Fire Dragon", 5, "Legendary", power, 5)

    def create_spell(self, name_or_power: Union[str, int, None] = None) -> Card:
        if isinstance(name_or_power, str):
            return SpellCard(name_or_power, 3, "Rare", "damage")
        cost = name_or_power if isinstance(name_or_power, int) else 3
        return SpellCard("Lightning Bolt", cost, "Rare", "damage")

    def create_artifact(self, name_or_power: Union[str, int, None] = None) -> Card:
        if isinstance(name_or_power, str):
            return ArtifactCard(name_or_power, 2, "Uncommon", 5, "+1 mana per turn")
        dur = name_or_power if isinstance(name_or_power, int) else 5
        return ArtifactCard("Mana Ring", 2, "Uncommon", dur, "+1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        for i in range(size):
            r = i % 3
            if r == 0:
                cards.append(self.create_creature())
            elif r == 1:
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
        return {"cards": cards, "size": len(cards), "theme": "Fantasy"}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
