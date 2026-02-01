from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from splendor_pokemon.types import TokenColor


@dataclass
class TokenBank:
    """Tracks available tokens in the shared bank."""

    tokens: Dict[TokenColor, int] = field(default_factory=dict)

    def take(self, color: TokenColor, amount: int = 1) -> None:
        if self.tokens.get(color, 0) < amount:
            raise ValueError(f"Not enough tokens for {color}.")
        self.tokens[color] -= amount

    def add(self, color: TokenColor, amount: int = 1) -> None:
        self.tokens[color] = self.tokens.get(color, 0) + amount

    def snapshot(self) -> Dict[TokenColor, int]:
        return dict(self.tokens)
