from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from splendor_pokemon.models.card import DevelopmentCard, NobleCard
from splendor_pokemon.types import PlayerPhase, TokenColor


@dataclass
class PlayerState:
    """State for a single player in the game."""

    player_id: str
    tokens: Dict[TokenColor, int] = field(default_factory=dict)
    cards: List[DevelopmentCard] = field(default_factory=list)
    reserved: List[DevelopmentCard] = field(default_factory=list)
    nobles: List[NobleCard] = field(default_factory=list)
    phase: PlayerPhase = PlayerPhase.WAITING

    def total_points(self) -> int:
        card_points = sum(card.points for card in self.cards)
        noble_points = sum(noble.points for noble in self.nobles)
        return card_points + noble_points

    def bonuses(self) -> Dict[TokenColor, int]:
        bonuses: Dict[TokenColor, int] = {}
        for card in self.cards:
            bonuses[card.bonus] = bonuses.get(card.bonus, 0) + 1
        return bonuses
