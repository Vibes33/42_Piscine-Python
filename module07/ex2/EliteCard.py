from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """A powerful card with combat and magic abilities."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana_pool: int):
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack
        self.health: int = health
        self.mana_pool: int = mana_pool
        self.armor: int = 3

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed with combat and magic abilities"
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Elite"
        info["attack"] = self.attack_power
        info["health"] = self.health
        info["mana_pool"] = self.mana_pool
        return info

    # --- Combatable ---
    def attack(self, target) -> dict:
        target_name = target.name if hasattr(target, "name") else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(incoming_damage, self.armor)
        taken = incoming_damage - blocked
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
            "armor": self.armor
        }

    # --- Magical ---
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(targets) * 2
        self.mana_pool -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> dict:
        return {"mana_pool": self.mana_pool}
