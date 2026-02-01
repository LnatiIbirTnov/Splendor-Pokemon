from __future__ import annotations

from typing import List

from splendor_pokemon.actions import Action, Pass
from splendor_pokemon.models.board import BoardState
from splendor_pokemon.models.player import PlayerState


class RuleEngine:
    """Validates actions and resolves wins. Extend with full Splendor rules."""

    def legal_actions(self, player: PlayerState, board: BoardState) -> List[Action]:
        # Placeholder: extend with actual rule logic.
        return [Pass()]

    def validate_action(self, player: PlayerState, board: BoardState, action: Action) -> None:
        if not isinstance(action, Action):
            raise ValueError("Action must derive from Action base class.")

    def check_winner(self, players: List[PlayerState]) -> PlayerState | None:
        for player in players:
            if player.total_points() >= 15:
                return player
        return None
