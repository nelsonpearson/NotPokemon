from notpokemon.models.creature import Creature
from notpokemon.models.types import ElementType
from notpokemon.data.moves import (
    INFERNO_SLASH, FLAME_PECK, SHARPEN, QUICK_STRIKE,
    TIDAL_CRASH, AQUA_JET, SHELL_GUARD, HEALING_SPLASH,
    BRAMBLE_SLAM, VINE_WHIP, LEECH_SEED, HERBAL_MEND,
    THUNDER_FANG, SPARK_RUSH, MAGNETIZE, STATIC_COAT,
    BLIZZARD_BITE, FROST_FANG, HAIL_VEIL, AURORA_HEAL,
    EARTHQUAKE_COIL, SAND_FANG, HARDEN_SCALE, VENOM_SPIT,
)

CREATURE_DEFS: dict[str, dict] = {
    "emberaptor": {
        "name": "Emberaptor",
        "element": ElementType.FIRE,
        "max_hp": 70,
        "attack": 90,
        "defense": 55,
        "speed": 85,
        "moves": [INFERNO_SLASH, FLAME_PECK, SHARPEN, QUICK_STRIKE],
    },
    "tidalotter": {
        "name": "Tidalotter",
        "element": ElementType.WATER,
        "max_hp": 85,
        "attack": 65,
        "defense": 80,
        "speed": 70,
        "moves": [TIDAL_CRASH, AQUA_JET, SHELL_GUARD, HEALING_SPLASH],
    },
    "thornhare": {
        "name": "Thornhare",
        "element": ElementType.NATURE,
        "max_hp": 75,
        "attack": 75,
        "defense": 70,
        "speed": 80,
        "moves": [BRAMBLE_SLAM, VINE_WHIP, LEECH_SEED, HERBAL_MEND],
    },
    "voltlynx": {
        "name": "Voltlynx",
        "element": ElementType.ELECTRIC,
        "max_hp": 65,
        "attack": 85,
        "defense": 60,
        "speed": 90,
        "moves": [THUNDER_FANG, SPARK_RUSH, MAGNETIZE, STATIC_COAT],
    },
    "glacifox": {
        "name": "Glacifox",
        "element": ElementType.ICE,
        "max_hp": 80,
        "attack": 70,
        "defense": 75,
        "speed": 75,
        "moves": [BLIZZARD_BITE, FROST_FANG, HAIL_VEIL, AURORA_HEAL],
    },
    "dunecobra": {
        "name": "Dunecobra",
        "element": ElementType.EARTH,
        "max_hp": 90,
        "attack": 80,
        "defense": 85,
        "speed": 45,
        "moves": [EARTHQUAKE_COIL, SAND_FANG, HARDEN_SCALE, VENOM_SPIT],
    },
}


def create_creature(creature_id: str) -> Creature:
    defn = CREATURE_DEFS[creature_id]
    return Creature(id=creature_id, **defn)


def get_all_creature_ids() -> list[str]:
    return list(CREATURE_DEFS.keys())
