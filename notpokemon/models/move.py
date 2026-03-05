from dataclasses import dataclass
from enum import Enum
from typing import Optional

from notpokemon.models.types import ElementType


class MoveCategory(Enum):
    PHYSICAL = "Physical"
    STATUS = "Status"
    HEAL = "Heal"


class StatusEffect(Enum):
    ATTACK_UP = "Attack Up"
    DEFENSE_UP = "Defense Up"
    ATTACK_DOWN = "Attack Down"
    DEFENSE_DOWN = "Defense Down"


@dataclass(frozen=True)
class Move:
    name: str
    element: ElementType
    category: MoveCategory
    power: int = 0
    accuracy: int = 100
    description: str = ""
    status_effect: Optional[StatusEffect] = None
    heal_percent: int = 0
    status_chance: int = 100
    priority: bool = False
