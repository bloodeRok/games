from astral.constants.images import ELEMENT_ART
from astral.base_entities import BaseElement, BaseCreature


class AirPriest(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Air priest",
            hp=9,
            attack=2,
            element=element,
            art=ELEMENT_ART.format(element="air", name="air_priest")
        )

    def end_turn_ability(self) -> None:
        self._element += 1


class Griffin(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Griffin",
            hp=9,
            attack=4,
            element=element,
            art=ELEMENT_ART.format(element="air", name="griffin")
        )


class Harpy(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Harpy",
            hp=3,
            attack=7,
            element=element,
            art=ELEMENT_ART.format(element="air", name="harpy")
        )


class AirElemental(BaseCreature):

    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Air elemental",
            hp=20,
            attack=0,
            element=element,
            art=ELEMENT_ART.format(element="air", name="air_elemental")
        )
        self.attack = element.power
