from notpokemon.models.move import Move, MoveCategory, StatusEffect
from notpokemon.models.types import ElementType

# --- Emberaptor (Fire) ---
INFERNO_SLASH = Move(
    name="Inferno Slash",
    element=ElementType.FIRE,
    category=MoveCategory.PHYSICAL,
    power=90,
    accuracy=80,
    description="A blazing slash with fiery claws.",
)

FLAME_PECK = Move(
    name="Flame Peck",
    element=ElementType.FIRE,
    category=MoveCategory.PHYSICAL,
    power=55,
    accuracy=100,
    description="A reliable peck wreathed in flame.",
)

SHARPEN = Move(
    name="Sharpen",
    element=ElementType.FIRE,
    category=MoveCategory.STATUS,
    description="Hones claws to boost attack.",
    status_effect=StatusEffect.ATTACK_UP,
)

QUICK_STRIKE = Move(
    name="Quick Strike",
    element=ElementType.FIRE,
    category=MoveCategory.PHYSICAL,
    power=40,
    accuracy=100,
    description="A lightning-fast strike that always goes first.",
    priority=True,
)

# --- Tidalotter (Water) ---
TIDAL_CRASH = Move(
    name="Tidal Crash",
    element=ElementType.WATER,
    category=MoveCategory.PHYSICAL,
    power=85,
    accuracy=85,
    description="Rides a massive wave into the foe.",
)

AQUA_JET = Move(
    name="Aqua Jet",
    element=ElementType.WATER,
    category=MoveCategory.PHYSICAL,
    power=50,
    accuracy=100,
    description="A quick jet of pressurized water.",
)

SHELL_GUARD = Move(
    name="Shell Guard",
    element=ElementType.WATER,
    category=MoveCategory.STATUS,
    description="Tucks into shell to boost defense.",
    status_effect=StatusEffect.DEFENSE_UP,
)

HEALING_SPLASH = Move(
    name="Healing Splash",
    element=ElementType.WATER,
    category=MoveCategory.HEAL,
    description="Restorative waters heal wounds.",
    heal_percent=30,
)

# --- Thornhare (Nature) ---
BRAMBLE_SLAM = Move(
    name="Bramble Slam",
    element=ElementType.NATURE,
    category=MoveCategory.PHYSICAL,
    power=85,
    accuracy=85,
    description="Slams foe with thorny vines.",
)

VINE_WHIP = Move(
    name="Vine Whip",
    element=ElementType.NATURE,
    category=MoveCategory.PHYSICAL,
    power=50,
    accuracy=100,
    description="Whips the foe with a sharp vine.",
)

LEECH_SEED = Move(
    name="Leech Seed",
    element=ElementType.NATURE,
    category=MoveCategory.STATUS,
    description="Saps the foe's strength.",
    status_effect=StatusEffect.ATTACK_DOWN,
)

HERBAL_MEND = Move(
    name="Herbal Mend",
    element=ElementType.NATURE,
    category=MoveCategory.HEAL,
    description="Draws energy from plants to heal.",
    heal_percent=25,
)

# --- Voltlynx (Electric) ---
THUNDER_FANG = Move(
    name="Thunder Fang",
    element=ElementType.ELECTRIC,
    category=MoveCategory.PHYSICAL,
    power=90,
    accuracy=80,
    description="Bites down with electrified fangs.",
)

SPARK_RUSH = Move(
    name="Spark Rush",
    element=ElementType.ELECTRIC,
    category=MoveCategory.PHYSICAL,
    power=55,
    accuracy=100,
    description="Charges at the foe in a burst of sparks.",
)

MAGNETIZE = Move(
    name="Magnetize",
    element=ElementType.ELECTRIC,
    category=MoveCategory.STATUS,
    description="Weakens the foe's defenses with a magnetic field.",
    status_effect=StatusEffect.DEFENSE_DOWN,
)

STATIC_COAT = Move(
    name="Static Coat",
    element=ElementType.ELECTRIC,
    category=MoveCategory.STATUS,
    description="Cloaks in static electricity to boost defense.",
    status_effect=StatusEffect.DEFENSE_UP,
)

# --- Glacifox (Ice) ---
BLIZZARD_BITE = Move(
    name="Blizzard Bite",
    element=ElementType.ICE,
    category=MoveCategory.PHYSICAL,
    power=90,
    accuracy=80,
    description="A freezing bite carried by blizzard winds.",
)

FROST_FANG = Move(
    name="Frost Fang",
    element=ElementType.ICE,
    category=MoveCategory.PHYSICAL,
    power=55,
    accuracy=100,
    description="Snaps with ice-coated fangs.",
)

HAIL_VEIL = Move(
    name="Hail Veil",
    element=ElementType.ICE,
    category=MoveCategory.STATUS,
    description="Surrounds self in hail to boost defense.",
    status_effect=StatusEffect.DEFENSE_UP,
)

AURORA_HEAL = Move(
    name="Aurora Heal",
    element=ElementType.ICE,
    category=MoveCategory.HEAL,
    description="Bathes in aurora light to restore health.",
    heal_percent=25,
)

# --- Dunecobra (Earth) ---
EARTHQUAKE_COIL = Move(
    name="Earthquake Coil",
    element=ElementType.EARTH,
    category=MoveCategory.PHYSICAL,
    power=95,
    accuracy=75,
    description="Slams the ground with a coiled strike.",
)

SAND_FANG = Move(
    name="Sand Fang",
    element=ElementType.EARTH,
    category=MoveCategory.PHYSICAL,
    power=50,
    accuracy=100,
    description="Bites with sand-hardened fangs.",
)

HARDEN_SCALE = Move(
    name="Harden Scale",
    element=ElementType.EARTH,
    category=MoveCategory.STATUS,
    description="Hardens scales to boost defense.",
    status_effect=StatusEffect.DEFENSE_UP,
)

VENOM_SPIT = Move(
    name="Venom Spit",
    element=ElementType.EARTH,
    category=MoveCategory.PHYSICAL,
    power=60,
    accuracy=90,
    description="Spits corrosive venom that may lower defense.",
    status_effect=StatusEffect.DEFENSE_DOWN,
    status_chance=30,
)
