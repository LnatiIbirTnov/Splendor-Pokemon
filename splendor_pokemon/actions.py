from __future__ import annotations

from dataclasses import dataclass
from typing import List

from splendor_pokemon.types import TokenColor


class Action:
    """Base action type to be extended by concrete actions."""


@dataclass(frozen=True)
class TakeTokens(Action):
    colors: List[TokenColor]


@dataclass(frozen=True)
class ReserveCard(Action):
    card_id: str


@dataclass(frozen=True)
class PurchaseCard(Action):
    card_id: str


@dataclass(frozen=True)
class Pass(Action):
    reason: str = "No valid moves"
