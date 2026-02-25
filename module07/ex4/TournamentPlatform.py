from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages tournament registration, matches, and leaderboard."""

    def __init__(self):
        self.cards: dict = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return f"Registered {card.name} ({card.card_id})"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]

        # Simple: higher attack_power wins
        if c1.attack_power >= c2.attack_power:
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(self.cards.values(),
                              key=lambda c: c.rating, reverse=True)
        return [
            f"{i + 1}. {c.name} - Rating: {c.rating} "
            f"({c.wins}-{c.losses})"
            for i, c in enumerate(sorted_cards)
        ]

    def generate_tournament_report(self) -> dict:
        ratings = [c.rating for c in self.cards.values()]
        avg = sum(ratings) / len(ratings) if ratings else 0
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": "active"
        }
