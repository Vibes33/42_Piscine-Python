from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Prioritizes attacking and dealing damage."""

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        # Sort by cost (play cheapest first)
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        played = []
        mana_used = 0
        damage = 0

        for card in sorted_hand:
            played.append(card.name)
            mana_used += card.cost
            damage += getattr(card, "attack_power",
                              getattr(card, "attack", card.cost))

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage
        }

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets,
                      key=lambda t: getattr(t, "health", 0))
