from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from splendor_pokemon.models.board import BoardState
from splendor_pokemon.models.player import PlayerState
from splendor_pokemon.types import TokenColor


@dataclass
class Observation:
    """Observation passed to agents to decide the next action."""

    current_player: PlayerState
    opponents: List[PlayerState]
    board: BoardState
    available_tokens: Dict[TokenColor, int]
