from __future__ import annotations

from abc import ABC, abstractmethod

from splendor_pokemon.actions import Action
from splendor_pokemon.observation import Observation


class Agent(ABC):
    """Base interface for AI or human policy implementations."""

    @abstractmethod
    def select_action(self, observation: Observation) -> Action:
        raise NotImplementedError
