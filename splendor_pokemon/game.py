from __future__ import annotations

from dataclasses import dataclass
from typing import List

from splendor_pokemon.actions import Action
from splendor_pokemon.models.board import BoardState
from splendor_pokemon.models.player import PlayerState
from splendor_pokemon.observation import Observation
from splendor_pokemon.rules import RuleEngine


@dataclass
class GameConfig:
    max_score: int = 15


class GameEngine:
    """Main game loop handler. Connects rules, state, and agents."""

    def __init__(self, board: BoardState, players: List[PlayerState], config: GameConfig | None = None):
        self.board = board
        self.players = players
        self.config = config or GameConfig()
        self.current_player_index = 0
        self.rules = RuleEngine()
        self.winner: PlayerState | None = None

    def current_player(self) -> PlayerState:
        return self.players[self.current_player_index]

    def observation(self) -> Observation:
        current = self.current_player()
        opponents = [player for idx, player in enumerate(self.players) if idx != self.current_player_index]
        return Observation(
            current_player=current,
            opponents=opponents,
            board=self.board,
            available_tokens=self.board.bank.snapshot(),
        )

    def legal_actions(self) -> List[Action]:
        return self.rules.legal_actions(self.current_player(), self.board)

    def apply_action(self, action: Action) -> None:
        self.rules.validate_action(self.current_player(), self.board, action)
        # Placeholder: perform action resolution.

    def step(self, action: Action) -> None:
        self.apply_action(action)
        self._advance_turn()
        self.winner = self.rules.check_winner(self.players)

    def _advance_turn(self) -> None:
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
