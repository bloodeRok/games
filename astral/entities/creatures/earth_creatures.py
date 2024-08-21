from astral.constants.images import ELEMENT_ART
from astral.base_entities import BaseCreature, BaseElement


class Dwarf(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Dwarf",
            hp=14,
            attack=3,
            element=element,
            art=ELEMENT_ART.format(element="earth", name="dwarf")
        )

    def end_turn_ability(self) -> None:
        self._element += 2


class Bear(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Bear",
            hp=12,
            attack=5,
            element=element,
            art=ELEMENT_ART.format(element="earth", name="bear")
        )


class Troll(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Troll",
            hp=20,
            attack=5,
            element=element,
            art=ELEMENT_ART.format(element="earth", name="troll")
        )

    def end_turn_ability(self) -> None:
        self.hp += 2


class EarthElemental(BaseCreature):

    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Earth elemental",
            hp=20,
            attack=0,
            element=element,
            art=ELEMENT_ART.format(element="earth", name="earth_elemental")
        )
        self.attack = element.power
