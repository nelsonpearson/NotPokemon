from __future__ import annotations

import random
from dataclasses import dataclass
from enum import Enum, auto

from notpokemon.models.creature import Creature
from notpokemon.models.move import Move, MoveCategory, StatusEffect
from notpokemon.models.types import get_type_multiplier


class EventType(Enum):
    MOVE_USED = auto()
    DAMAGE = auto()
    HEAL = auto()
    STATUS_APPLIED = auto()
    STATUS_EXPIRED = auto()
    MISS = auto()
    FAINT = auto()
    EFFECTIVENESS = auto()


@dataclass
class BattleEvent:
    event_type: EventType
    source: str  # creature id
    target: str  # creature id
    message: str
    value: int = 0  # damage/heal amount
    extra: str = ""  # "super_effective", "not_effective", etc.


class BattleState:
    def __init__(self, player: Creature, opponent: Creature):
        self.player = player
        self.opponent = opponent

    def execute_turn(self, player_move: Move, opponent_move: Move) -> list[BattleEvent]:
        events: list[BattleEvent] = []
        first, first_move, second, second_move = self._determine_order(
            player_move, opponent_move
        )

        events.extend(self._execute_move(first, second, first_move))
        if second.is_fainted:
            events.append(BattleEvent(
                EventType.FAINT, second.id, second.id,
                f"{second.name} fainted!"
            ))
            return events

        events.extend(self._execute_move(second, first, second_move))
        if first.is_fainted:
            events.append(BattleEvent(
                EventType.FAINT, first.id, first.id,
                f"{first.name} fainted!"
            ))
            return events

        for creature in (self.player, self.opponent):
            expired = creature.tick_modifiers()
            for stat in expired:
                events.append(BattleEvent(
                    EventType.STATUS_EXPIRED, creature.id, creature.id,
                    f"{creature.name}'s {stat} returned to normal."
                ))

        return events

    def _determine_order(
        self, player_move: Move, opponent_move: Move
    ) -> tuple[Creature, Move, Creature, Move]:
        if player_move.priority and not opponent_move.priority:
            return self.player, player_move, self.opponent, opponent_move
        if opponent_move.priority and not player_move.priority:
            return self.opponent, opponent_move, self.player, player_move

        if self.player.speed > self.opponent.speed:
            return self.player, player_move, self.opponent, opponent_move
        elif self.opponent.speed > self.player.speed:
            return self.opponent, opponent_move, self.player, player_move
        else:
            if random.random() < 0.5:
                return self.player, player_move, self.opponent, opponent_move
            return self.opponent, opponent_move, self.player, player_move

    def _execute_move(
        self, attacker: Creature, defender: Creature, move: Move
    ) -> list[BattleEvent]:
        events: list[BattleEvent] = []

        events.append(BattleEvent(
            EventType.MOVE_USED, attacker.id, defender.id,
            f"{attacker.name} used {move.name}!"
        ))

        if move.category == MoveCategory.HEAL:
            heal_amount = int(attacker.max_hp * move.heal_percent / 100)
            actual = attacker.heal(heal_amount)
            events.append(BattleEvent(
                EventType.HEAL, attacker.id, attacker.id,
                f"{attacker.name} restored {actual} HP!",
                value=actual
            ))
            return events

        if move.category == MoveCategory.STATUS:
            if random.randint(1, 100) > move.accuracy:
                events.append(BattleEvent(
                    EventType.MISS, attacker.id, defender.id,
                    f"{attacker.name}'s attack missed!"
                ))
                return events
            events.extend(self._apply_status(attacker, defender, move))
            return events

        # Physical move
        if random.randint(1, 100) > move.accuracy:
            events.append(BattleEvent(
                EventType.MISS, attacker.id, defender.id,
                f"{attacker.name}'s attack missed!"
            ))
            return events

        damage, multiplier = self._calc_damage(attacker, defender, move)
        actual = defender.take_damage(damage)

        if multiplier > 1.0:
            events.append(BattleEvent(
                EventType.EFFECTIVENESS, attacker.id, defender.id,
                "It's super effective!",
                extra="super_effective"
            ))
        elif multiplier < 1.0:
            events.append(BattleEvent(
                EventType.EFFECTIVENESS, attacker.id, defender.id,
                "It's not very effective...",
                extra="not_effective"
            ))

        events.append(BattleEvent(
            EventType.DAMAGE, attacker.id, defender.id,
            f"{defender.name} took {actual} damage!",
            value=actual
        ))

        if move.status_effect and move.status_chance > 0:
            if random.randint(1, 100) <= move.status_chance:
                events.extend(self._apply_status(attacker, defender, move))

        return events

    def _calc_damage(
        self, attacker: Creature, defender: Creature, move: Move
    ) -> tuple[int, float]:
        type_mult = get_type_multiplier(move.element, defender.element)
        rand_factor = random.uniform(0.85, 1.0)

        eff_atk = attacker.effective_attack
        eff_def = max(1, defender.effective_defense)

        base = (move.power * eff_atk) / (50 * eff_def) * 20 + 2
        final = int(base * type_mult * rand_factor)
        return max(1, final), type_mult

    def _apply_status(
        self, attacker: Creature, defender: Creature, move: Move
    ) -> list[BattleEvent]:
        events: list[BattleEvent] = []
        if move.status_effect is None:
            return events

        effect = move.status_effect
        if effect == StatusEffect.ATTACK_UP:
            attacker.apply_modifier("attack", 1.5)
            events.append(BattleEvent(
                EventType.STATUS_APPLIED, attacker.id, attacker.id,
                f"{attacker.name}'s attack rose!"
            ))
        elif effect == StatusEffect.DEFENSE_UP:
            attacker.apply_modifier("defense", 1.5)
            events.append(BattleEvent(
                EventType.STATUS_APPLIED, attacker.id, attacker.id,
                f"{attacker.name}'s defense rose!"
            ))
        elif effect == StatusEffect.ATTACK_DOWN:
            defender.apply_modifier("attack", 0.67)
            events.append(BattleEvent(
                EventType.STATUS_APPLIED, attacker.id, defender.id,
                f"{defender.name}'s attack fell!"
            ))
        elif effect == StatusEffect.DEFENSE_DOWN:
            defender.apply_modifier("defense", 0.67)
            events.append(BattleEvent(
                EventType.STATUS_APPLIED, attacker.id, defender.id,
                f"{defender.name}'s defense fell!"
            ))

        return events

    def pick_ai_move(self) -> Move:
        opponent = self.opponent
        moves = opponent.moves

        if opponent.hp_fraction < 0.4:
            heal_moves = [m for m in moves if m.category == MoveCategory.HEAL]
            if heal_moves and random.random() < 0.6:
                return heal_moves[0]

        has_active_buff = any(
            stat in ("attack", "defense") and turns > 0
            for stat, (_, turns) in opponent.stat_modifiers.items()
        )
        if not has_active_buff and random.random() < 0.2:
            status_moves = [m for m in moves if m.category == MoveCategory.STATUS]
            if status_moves:
                return random.choice(status_moves)

        damage_moves = [m for m in moves if m.category == MoveCategory.PHYSICAL]
        if damage_moves:
            scored = []
            for m in damage_moves:
                mult = get_type_multiplier(m.element, self.player.element)
                score = m.power * mult * (m.accuracy / 100)
                scored.append((score, m))
            scored.sort(key=lambda x: x[0], reverse=True)

            if random.random() < 0.7:
                return scored[0][1]
            return random.choice(damage_moves)

        return random.choice(moves)
