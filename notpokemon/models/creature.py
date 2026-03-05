from __future__ import annotations

from dataclasses import dataclass, field

from notpokemon.models.move import Move
from notpokemon.models.types import ElementType


@dataclass
class Creature:
    id: str
    name: str
    element: ElementType
    max_hp: int
    attack: int
    defense: int
    speed: int
    moves: list[Move]
    current_hp: int = 0
    stat_modifiers: dict[str, tuple[float, int]] = field(default_factory=dict)

    def __post_init__(self):
        if self.current_hp == 0:
            self.current_hp = self.max_hp

    @property
    def effective_attack(self) -> float:
        mod = self.stat_modifiers.get("attack", (1.0, 0))
        return self.attack * mod[0] if mod[1] > 0 else float(self.attack)

    @property
    def effective_defense(self) -> float:
        mod = self.stat_modifiers.get("defense", (1.0, 0))
        return self.defense * mod[0] if mod[1] > 0 else float(self.defense)

    def apply_modifier(self, stat: str, multiplier: float, turns: int = 3):
        self.stat_modifiers[stat] = (multiplier, turns)

    def tick_modifiers(self) -> list[str]:
        expired = []
        to_update = {}
        for stat, (multiplier, turns) in self.stat_modifiers.items():
            if turns <= 1:
                expired.append(stat)
            else:
                to_update[stat] = (multiplier, turns - 1)
        for stat in expired:
            del self.stat_modifiers[stat]
        self.stat_modifiers.update(to_update)
        return expired

    @property
    def is_fainted(self) -> bool:
        return self.current_hp <= 0

    @property
    def hp_fraction(self) -> float:
        return max(0, self.current_hp / self.max_hp)

    def take_damage(self, amount: int) -> int:
        actual = min(amount, self.current_hp)
        self.current_hp = max(0, self.current_hp - amount)
        return actual

    def heal(self, amount: int) -> int:
        before = self.current_hp
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        return self.current_hp - before

    def clone(self) -> Creature:
        return Creature(
            id=self.id,
            name=self.name,
            element=self.element,
            max_hp=self.max_hp,
            attack=self.attack,
            defense=self.defense,
            speed=self.speed,
            moves=list(self.moves),
        )
