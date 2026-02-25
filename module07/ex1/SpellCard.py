from ex0.Card import Card


class SpellCard(Card):
    """An instant spell card with a one-time effect."""

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: dict) -> dict:
        """Cast the spell (consumed after use)."""
        effects = {
            "damage": f"Deal {self.cost} damage to target",
            "heal": f"Restore {self.cost} health to target",
            "buff": f"Buff target with +{self.cost} power",
            "debuff": f"Debuff target with -{self.cost} power"
        }
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effects.get(self.effect_type, "Spell cast")
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Spell"
        info["effect_type"] = self.effect_type
        return info

    def resolve_effect(self, targets: list) -> dict:
        """Resolve spell effect on targets."""
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets_affected": len(targets),
            "resolved": True
        }
