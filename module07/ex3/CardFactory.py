from abc import ABC, abstractmethod
from typing import Union
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory interface for creating cards."""

    @abstractmethod
    def create_creature(self, name_or_power: Union[str, int, None] = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: Union[str, int, None] = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: Union[str, int, None] = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass
