from enum import Enum


class ElementType(Enum):
    FIRE = "Fire"
    WATER = "Water"
    NATURE = "Nature"
    ELECTRIC = "Electric"
    ICE = "Ice"
    EARTH = "Earth"


TYPE_CHART: dict[tuple[ElementType, ElementType], float] = {
    (ElementType.FIRE, ElementType.NATURE): 2.0,
    (ElementType.FIRE, ElementType.WATER): 0.5,
    (ElementType.WATER, ElementType.FIRE): 2.0,
    (ElementType.WATER, ElementType.NATURE): 0.5,
    (ElementType.NATURE, ElementType.WATER): 2.0,
    (ElementType.NATURE, ElementType.FIRE): 0.5,
    (ElementType.ELECTRIC, ElementType.EARTH): 2.0,
    (ElementType.ELECTRIC, ElementType.ICE): 0.5,
    (ElementType.ICE, ElementType.ELECTRIC): 2.0,
    (ElementType.ICE, ElementType.EARTH): 0.5,
    (ElementType.EARTH, ElementType.ICE): 2.0,
    (ElementType.EARTH, ElementType.ELECTRIC): 0.5,
}


def get_type_multiplier(attack_type: ElementType, defender_type: ElementType) -> float:
    return TYPE_CHART.get((attack_type, defender_type), 1.0)
