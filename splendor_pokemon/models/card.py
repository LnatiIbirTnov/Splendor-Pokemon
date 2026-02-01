from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional

from splendor_pokemon.types import CardTier, TokenColor


@dataclass(frozen=True)
class Cost:
    """Cost to purchase a card expressed by token color."""

    requirements: Dict[TokenColor, int] = field(default_factory=dict)


@dataclass(frozen=True)
class DevelopmentCard:
    """Base development card for Splendor-like gameplay."""

    card_id: str
    tier: CardTier
    bonus: TokenColor
    points: int
    cost: Cost
    pokemon_name: Optional[str] = None
    description: Optional[str] = None


@dataclass(frozen=True)
class NobleCard:
    """Represents a noble-style objective card."""

    card_id: str
    points: int
    requirement: Cost
    name: Optional[str] = None
