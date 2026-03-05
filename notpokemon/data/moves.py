from notpokemon.models.move import Move, MoveCategory, StatusEffect
from notpokemon.models.types import ElementType

# ============================================================
# FIRE MOVES
# ============================================================

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

FLAME_BURST = Move(
    name="Flame Burst",
    element=ElementType.FIRE,
    category=MoveCategory.PHYSICAL,
    power=65,
    accuracy=95,
    description="Releases a burst of intense flame.",
)

MAGMA_STOMP = Move(
    name="Magma Stomp",
    element=ElementType.FIRE,
    category=MoveCategory.PHYSICAL,
    power=95,
    accuracy=75,
    description="Slams down with magma-heated feet.",
)

ASH_CLOUD = Move(
    name="Ash Cloud",
    element=ElementType.FIRE,
    category=MoveCategory.STATUS,
    description="Coats foe in ash to lower its defense.",
    status_effect=StatusEffect.DEFENSE_DOWN,
)

SHARPEN = Move(
    name="Sharpen",
    element=ElementType.FIRE,
    category=MoveCategory.STATUS,
    description="Hones claws to boost attack.",
    status_effect=StatusEffect.ATTACK_UP,
)

MAGMA_MEND = Move(
    name="Magma Mend",
    element=ElementType.FIRE,
    category=MoveCategory.HEAL,
    description="Absorbs geothermal heat to restore HP.",
    heal_percent=20,
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

# ============================================================
# WATER MOVES
# ============================================================

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

BUBBLE_BEAM = Move(
    name="Bubble Beam",
    element=ElementType.WATER,
    category=MoveCategory.PHYSICAL,
    power=65,
    accuracy=95,
    description="Fires a stream of high-pressure bubbles.",
)

TORRENT = Move(
    name="Torrent",
    element=ElementType.WATER,
    category=MoveCategory.PHYSICAL,
    power=90,
    accuracy=80,
    description="Unleashes a relentless raging torrent.",
)

SHELL_GUARD = Move(
    name="Shell Guard",
    element=ElementType.WATER,
    category=MoveCategory.STATUS,
    description="Tucks into shell to boost defense.",
    status_effect=StatusEffect.DEFENSE_UP,
)

MIST_VEIL = Move(
    name="Mist Veil",
    element=ElementType.WATER,
    category=MoveCategory.STATUS,
    description="Wraps self in concealing mist to boost defense.",
    status_effect=StatusEffect.DEFENSE_UP,
)

HEALING_SPLASH = Move(
    name="Healing Splash",
    element=ElementType.WATER,
    category=MoveCategory.HEAL,
    description="Restorative waters heal wounds.",
    heal_percent=30,
)

OCEAN_MEND = Move(
    name="Ocean Mend",
    element=ElementType.WATER,
    category=MoveCategory.HEAL,
    description="Draws on ocean currents to restore HP.",
    heal_percent=20,
)

# ============================================================
# NATURE MOVES
# ============================================================

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

THORN_SHOT = Move(
    name="Thorn Shot",
    element=ElementType.NATURE,
    category=MoveCategory.PHYSICAL,
    power=65,
    accuracy=95,
    description="Fires a volley of sharp thorns.",
)

FOREST_SLAM = Move(
    name="Forest Slam",
    element=ElementType.NATURE,
    category=MoveCategory.PHYSICAL,
    power=90,
    accuracy=80,
    description="Channels the power of an ancient forest into a slam.",
)

LEECH_SEED = Move(
    name="Leech Seed",
    element=ElementType.NATURE,
    category=MoveCategory.STATUS,
    description="Saps the foe's strength.",
    status_effect=StatusEffect.ATTACK_DOWN,
)

SPORE_CLOUD = Move(
    name="Spore Cloud",
    element=ElementType.NATURE,
    category=MoveCategory.STATUS,
    accuracy=90,
    description="Releases weakening spores to lower foe's attack.",
    status_effect=StatusEffect.ATTACK_DOWN,
)

HERBAL_MEND = Move(
    name="Herbal Mend",
    element=ElementType.NATURE,
    category=MoveCategory.HEAL,
    description="Draws energy from plants to heal.",
    heal_percent=25,
)

PETAL_MEND = Move(
    name="Petal Mend",
    element=ElementType.NATURE,
    category=MoveCategory.HEAL,
    description="Absorbs nutrients from flower petals to restore HP.",
    heal_percent=20,
)

# ============================================================
# ELECTRIC MOVES
# ============================================================

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

SPARK_BOLT = Move(
    name="Spark Bolt",
    element=ElementType.ELECTRIC,
    category=MoveCategory.PHYSICAL,
    power=65,
    accuracy=95,
    description="Hurls a concentrated bolt of electricity.",
)

ARC_FLASH = Move(
    name="Arc Flash",
    element=ElementType.ELECTRIC,
    category=MoveCategory.PHYSICAL,
    power=90,
    accuracy=80,
    description="Discharges a blinding electric arc.",
)

MAGNETIZE = Move(
    name="Magnetize",
    element=ElementType.ELECTRIC,
    category=MoveCategory.STATUS,
    description="Weakens the foe's defenses with a magnetic field.",
    status_effect=StatusEffect.DEFENSE_DOWN,
)

CHARGE_UP = Move(
    name="Charge Up",
    element=ElementType.ELECTRIC,
    category=MoveCategory.STATUS,
    description="Builds up electrical charge to boost attack.",
    status_effect=StatusEffect.ATTACK_UP,
)

STATIC_COAT = Move(
    name="Static Coat",
    element=ElementType.ELECTRIC,
    category=MoveCategory.STATUS,
    description="Cloaks in static electricity to boost defense.",
    status_effect=StatusEffect.DEFENSE_UP,
)

VOLT_MEND = Move(
    name="Volt Mend",
    element=ElementType.ELECTRIC,
    category=MoveCategory.HEAL,
    description="Converts stored electric charge into healing energy.",
    heal_percent=20,
)

# ============================================================
# ICE MOVES
# ============================================================

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

ICE_SHARD = Move(
    name="Ice Shard",
    element=ElementType.ICE,
    category=MoveCategory.PHYSICAL,
    power=65,
    accuracy=95,
    description="Hurls razor-sharp shards of ice.",
)

BLIZZARD_STORM = Move(
    name="Blizzard Storm",
    element=ElementType.ICE,
    category=MoveCategory.PHYSICAL,
    power=90,
    accuracy=80,
    description="Summons a ferocious blizzard to batter the foe.",
)

HAIL_VEIL = Move(
    name="Hail Veil",
    element=ElementType.ICE,
    category=MoveCategory.STATUS,
    description="Surrounds self in hail to boost defense.",
    status_effect=StatusEffect.DEFENSE_UP,
)

PERMAFROST = Move(
    name="Permafrost",
    element=ElementType.ICE,
    category=MoveCategory.STATUS,
    description="Hardens outer layer to permafrost, boosting defense.",
    status_effect=StatusEffect.DEFENSE_UP,
)

AURORA_HEAL = Move(
    name="Aurora Heal",
    element=ElementType.ICE,
    category=MoveCategory.HEAL,
    description="Bathes in aurora light to restore health.",
    heal_percent=25,
)

FROST_MEND = Move(
    name="Frost Mend",
    element=ElementType.ICE,
    category=MoveCategory.HEAL,
    description="Draws on the stillness of permafrost to restore HP.",
    heal_percent=20,
)

# ============================================================
# EARTH MOVES
# ============================================================

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

ROCK_THROW = Move(
    name="Rock Throw",
    element=ElementType.EARTH,
    category=MoveCategory.PHYSICAL,
    power=65,
    accuracy=95,
    description="Hurls a jagged boulder at the foe.",
)

BOULDER_CRUSH = Move(
    name="Boulder Crush",
    element=ElementType.EARTH,
    category=MoveCategory.PHYSICAL,
    power=90,
    accuracy=80,
    description="Crushes the foe beneath a massive boulder.",
)

HARDEN_SCALE = Move(
    name="Harden Scale",
    element=ElementType.EARTH,
    category=MoveCategory.STATUS,
    description="Hardens scales to boost defense.",
    status_effect=StatusEffect.DEFENSE_UP,
)

DUST_STORM = Move(
    name="Dust Storm",
    element=ElementType.EARTH,
    category=MoveCategory.STATUS,
    accuracy=90,
    description="Whips up a dust storm to lower foe's attack.",
    status_effect=StatusEffect.ATTACK_DOWN,
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

STONE_MEND = Move(
    name="Stone Mend",
    element=ElementType.EARTH,
    category=MoveCategory.HEAL,
    description="Absorbs minerals from the earth to restore HP.",
    heal_percent=20,
)
