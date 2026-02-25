from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Card with combat and ranking abilities for tournaments."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, card_id: str):
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack
        self.health: int = health
        self.card_id: str = card_id
        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = 1200

    # --- Card ---
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters the arena"
        }

    # --- Combatable ---
    def attack(self, target) -> dict:
        target_name = target.name if hasattr(target, "name") else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    # --- Rankable ---
    def calculate_rating(self) -> int:
        self.rating = 1200 + (self.wins * 16) - (self.losses * 16)
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            "card_id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            **self.get_card_info(),
            **self.get_combat_stats(),
            **self.get_rank_info()
        }
