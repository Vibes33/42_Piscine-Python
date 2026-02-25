from ex0.Card import Card


class CreatureCard(Card):
    """A creature card with attack and health."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict) -> dict:
        """Summon the creature to the battlefield."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def get_card_info(self) -> dict:
        """Return creature card information."""
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    def attack_target(self, target) -> dict:
        """Attack a target creature or player."""
        return {
            "attacker": self.name,
            "target": target.name if hasattr(target, "name") else str(target),
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
