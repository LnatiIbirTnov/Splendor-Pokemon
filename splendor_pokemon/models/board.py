from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from splendor_pokemon.models.card import DevelopmentCard, NobleCard
from splendor_pokemon.models.tokens import TokenBank
from splendor_pokemon.types import CardTier


@dataclass
class BoardState:
    """State of the shared board, including open cards and nobles."""

    bank: TokenBank
    open_cards: Dict[CardTier, List[DevelopmentCard]] = field(default_factory=dict)
    decks: Dict[CardTier, List[DevelopmentCard]] = field(default_factory=dict)
    nobles: List[NobleCard] = field(default_factory=list)

    def refill_open_cards(self, tier: CardTier, count: int = 4) -> None:
        current = self.open_cards.get(tier, [])
        deck = self.decks.get(tier, [])
        while len(current) < count and deck:
            current.append(deck.pop(0))
        self.open_cards[tier] = current
        self.decks[tier] = deck
