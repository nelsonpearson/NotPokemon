from notpokemon.models.creature import Creature
from notpokemon.models.types import ElementType
from notpokemon.data.moves import (
    # Fire
    INFERNO_SLASH, FLAME_PECK, FLAME_BURST, MAGMA_STOMP,
    ASH_CLOUD, SHARPEN, MAGMA_MEND, QUICK_STRIKE,
    # Water
    TIDAL_CRASH, AQUA_JET, BUBBLE_BEAM, TORRENT,
    SHELL_GUARD, MIST_VEIL, HEALING_SPLASH, OCEAN_MEND,
    # Nature
    BRAMBLE_SLAM, VINE_WHIP, THORN_SHOT, FOREST_SLAM,
    LEECH_SEED, SPORE_CLOUD, HERBAL_MEND, PETAL_MEND,
    # Electric
    THUNDER_FANG, SPARK_RUSH, SPARK_BOLT, ARC_FLASH,
    MAGNETIZE, CHARGE_UP, STATIC_COAT, VOLT_MEND,
    # Ice
    BLIZZARD_BITE, FROST_FANG, ICE_SHARD, BLIZZARD_STORM,
    HAIL_VEIL, PERMAFROST, AURORA_HEAL, FROST_MEND,
    # Earth
    EARTHQUAKE_COIL, SAND_FANG, ROCK_THROW, BOULDER_CRUSH,
    HARDEN_SCALE, DUST_STORM, VENOM_SPIT, STONE_MEND,
)

# All HP values are ~2x original to make fights last longer.
# Base stat totals are preserved in ATK/DEF/SPD; HP is bonus on top.

CREATURE_DEFS: dict[str, dict] = {

    # ── ORIGINAL 6 (HP doubled) ───────────────────────────────────────────
    "emberaptor": {
        "name": "Emberaptor",
        "element": ElementType.FIRE,
        "max_hp": 140,
        "attack": 90,
        "defense": 55,
        "speed": 85,
        "moves": [INFERNO_SLASH, FLAME_PECK, SHARPEN, QUICK_STRIKE],
    },
    "tidalotter": {
        "name": "Tidalotter",
        "element": ElementType.WATER,
        "max_hp": 170,
        "attack": 65,
        "defense": 80,
        "speed": 70,
        "moves": [TIDAL_CRASH, AQUA_JET, SHELL_GUARD, HEALING_SPLASH],
    },
    "thornhare": {
        "name": "Thornhare",
        "element": ElementType.NATURE,
        "max_hp": 150,
        "attack": 75,
        "defense": 70,
        "speed": 80,
        "moves": [BRAMBLE_SLAM, VINE_WHIP, LEECH_SEED, HERBAL_MEND],
    },
    "voltlynx": {
        "name": "Voltlynx",
        "element": ElementType.ELECTRIC,
        "max_hp": 130,
        "attack": 85,
        "defense": 60,
        "speed": 90,
        "moves": [THUNDER_FANG, SPARK_RUSH, MAGNETIZE, STATIC_COAT],
    },
    "glacifox": {
        "name": "Glacifox",
        "element": ElementType.ICE,
        "max_hp": 160,
        "attack": 70,
        "defense": 75,
        "speed": 75,
        "moves": [BLIZZARD_BITE, FROST_FANG, HAIL_VEIL, AURORA_HEAL],
    },
    "dunecobra": {
        "name": "Dunecobra",
        "element": ElementType.EARTH,
        "max_hp": 180,
        "attack": 80,
        "defense": 85,
        "speed": 45,
        "moves": [EARTHQUAKE_COIL, SAND_FANG, HARDEN_SCALE, VENOM_SPIT],
    },

    # ── FIRE (4 new) ──────────────────────────────────────────────────────
    "cindermole": {
        "name": "Cindermole",
        "element": ElementType.FIRE,
        "max_hp": 150,
        "attack": 75,
        "defense": 70,
        "speed": 45,
        "moves": [MAGMA_STOMP, FLAME_BURST, ASH_CLOUD, MAGMA_MEND],
    },
    "lavabull": {
        "name": "Lavabull",
        "element": ElementType.FIRE,
        "max_hp": 185,
        "attack": 100,
        "defense": 65,
        "speed": 15,
        "moves": [MAGMA_STOMP, INFERNO_SLASH, SHARPEN, MAGMA_MEND],
    },
    "emberwolf": {
        "name": "Emberwolf",
        "element": ElementType.FIRE,
        "max_hp": 145,
        "attack": 95,
        "defense": 50,
        "speed": 70,
        "moves": [INFERNO_SLASH, FLAME_BURST, SHARPEN, QUICK_STRIKE],
    },
    "pyrotoad": {
        "name": "Pyrotoad",
        "element": ElementType.FIRE,
        "max_hp": 170,
        "attack": 60,
        "defense": 90,
        "speed": 50,
        "moves": [FLAME_BURST, MAGMA_STOMP, ASH_CLOUD, MAGMA_MEND],
    },

    # ── WATER (4 new) ─────────────────────────────────────────────────────
    "bubblewhal": {
        "name": "Bubblewhal",
        "element": ElementType.WATER,
        "max_hp": 210,
        "attack": 70,
        "defense": 75,
        "speed": 25,
        "moves": [TIDAL_CRASH, BUBBLE_BEAM, MIST_VEIL, OCEAN_MEND],
    },
    "coralsnap": {
        "name": "Coralsnap",
        "element": ElementType.WATER,
        "max_hp": 145,
        "attack": 85,
        "defense": 75,
        "speed": 60,
        "moves": [TORRENT, AQUA_JET, SHELL_GUARD, OCEAN_MEND],
    },
    "tideshark": {
        "name": "Tideshark",
        "element": ElementType.WATER,
        "max_hp": 135,
        "attack": 95,
        "defense": 55,
        "speed": 75,
        "moves": [TORRENT, BUBBLE_BEAM, SHELL_GUARD, HEALING_SPLASH],
    },
    "mistdeer": {
        "name": "Mistdeer",
        "element": ElementType.WATER,
        "max_hp": 155,
        "attack": 60,
        "defense": 70,
        "speed": 80,
        "moves": [AQUA_JET, BUBBLE_BEAM, MIST_VEIL, HEALING_SPLASH],
    },

    # ── NATURE (3 new) ────────────────────────────────────────────────────
    "mossboar": {
        "name": "Mossboar",
        "element": ElementType.NATURE,
        "max_hp": 175,
        "attack": 80,
        "defense": 80,
        "speed": 30,
        "moves": [FOREST_SLAM, VINE_WHIP, LEECH_SEED, PETAL_MEND],
    },
    "leafwing": {
        "name": "Leafwing",
        "element": ElementType.NATURE,
        "max_hp": 125,
        "attack": 70,
        "defense": 55,
        "speed": 110,
        "moves": [THORN_SHOT, VINE_WHIP, SPORE_CLOUD, HERBAL_MEND],
    },
    "bramblebear": {
        "name": "Bramblebear",
        "element": ElementType.NATURE,
        "max_hp": 190,
        "attack": 95,
        "defense": 60,
        "speed": 25,
        "moves": [FOREST_SLAM, THORN_SHOT, LEECH_SEED, PETAL_MEND],
    },

    # ── ELECTRIC (3 new) ──────────────────────────────────────────────────
    "zapfinch": {
        "name": "Zapfinch",
        "element": ElementType.ELECTRIC,
        "max_hp": 115,
        "attack": 80,
        "defense": 55,
        "speed": 105,
        "moves": [ARC_FLASH, SPARK_BOLT, CHARGE_UP, VOLT_MEND],
    },
    "stormhound": {
        "name": "Stormhound",
        "element": ElementType.ELECTRIC,
        "max_hp": 150,
        "attack": 85,
        "defense": 65,
        "speed": 65,
        "moves": [THUNDER_FANG, SPARK_BOLT, MAGNETIZE, VOLT_MEND],
    },
    "bolttiger": {
        "name": "Bolttiger",
        "element": ElementType.ELECTRIC,
        "max_hp": 155,
        "attack": 100,
        "defense": 55,
        "speed": 55,
        "moves": [ARC_FLASH, SPARK_RUSH, CHARGE_UP, STATIC_COAT],
    },

    # ── ICE (3 new) ───────────────────────────────────────────────────────
    "frostmoth": {
        "name": "Frostmoth",
        "element": ElementType.ICE,
        "max_hp": 120,
        "attack": 75,
        "defense": 60,
        "speed": 100,
        "moves": [BLIZZARD_STORM, ICE_SHARD, PERMAFROST, FROST_MEND],
    },
    "glacimoose": {
        "name": "Glacimoose",
        "element": ElementType.ICE,
        "max_hp": 195,
        "attack": 75,
        "defense": 80,
        "speed": 25,
        "moves": [BLIZZARD_BITE, ICE_SHARD, HAIL_VEIL, FROST_MEND],
    },
    "chilltoad": {
        "name": "Chilltoad",
        "element": ElementType.ICE,
        "max_hp": 165,
        "attack": 65,
        "defense": 90,
        "speed": 50,
        "moves": [BLIZZARD_STORM, FROST_FANG, PERMAFROST, AURORA_HEAL],
    },

    # ── EARTH (2 new) ─────────────────────────────────────────────────────
    "mudbison": {
        "name": "Mudbison",
        "element": ElementType.EARTH,
        "max_hp": 210,
        "attack": 85,
        "defense": 80,
        "speed": 5,
        "moves": [BOULDER_CRUSH, ROCK_THROW, HARDEN_SCALE, STONE_MEND],
    },
    "stonecrab": {
        "name": "Stonecrab",
        "element": ElementType.EARTH,
        "max_hp": 155,
        "attack": 75,
        "defense": 100,
        "speed": 40,
        "moves": [EARTHQUAKE_COIL, ROCK_THROW, DUST_STORM, STONE_MEND],
    },
}


def create_creature(creature_id: str) -> Creature:
    defn = CREATURE_DEFS[creature_id]
    return Creature(id=creature_id, **defn)


def get_all_creature_ids() -> list[str]:
    return list(CREATURE_DEFS.keys())
