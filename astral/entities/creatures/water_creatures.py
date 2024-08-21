from astral.constants.images import ELEMENT_ART
from astral.base_entities import BaseCreature, BaseElement


class Mermaid(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Mermaid",
            hp=7,
            attack=3,
            element=element,
            art=ELEMENT_ART.format(element="water", name="mermaid")
        )

    def end_turn_ability(self) -> None:
        self._element += 1


class Luska(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Luska",
            hp=8,
            attack=9,
            element=element,
            art=ELEMENT_ART.format(element="water", name="luska")
        )


class Undine(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Undine",
            hp=8,
            attack=4,
            element=element,
            art=ELEMENT_ART.format(element="water", name="undine")
        )


class WaterElemental(BaseCreature):

    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Water elemental",
            hp=20,
            attack=0,
            element=element,
            art=ELEMENT_ART.format(element="water", name="water_elemental")
        )
        self.attack = element.power
