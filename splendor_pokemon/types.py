from __future__ import annotations

from enum import Enum


class TokenColor(str, Enum):
    FIRE = "fire"
    WATER = "water"
    GRASS = "grass"
    ELECTRIC = "electric"
    PSYCHIC = "psychic"
    STEEL = "steel"
    GOLD = "gold"  # Wild token


class CardTier(int, Enum):
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3


class PlayerPhase(str, Enum):
    WAITING = "waiting"
    ACTIVE = "active"
    FINISHED = "finished"
