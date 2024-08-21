from astral.constants.images import ELEMENT_ART
from astral.base_entities import BaseCreature, BaseElement


class Demon(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Demon",
            hp=5,
            attack=2,
            element=element,
            art=ELEMENT_ART.format(element="fire", name="demon")
        )

    def end_turn_ability(self) -> None:
        self._element += 1


class Phoenix(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Phoenix",
            hp=8,
            attack=5,
            element=element,
            art=ELEMENT_ART.format(element="fire", name="phoenix")
        )


class WallOfFire(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Wall of fire",
            hp=20,
            attack=0,
            element=element,
            art=ELEMENT_ART.format(element="fire", name="wall_of_fire")
        )


class FireElemental(BaseCreature):

    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Fire elemental",
            hp=20,
            attack=0,
            element=element,
            art=ELEMENT_ART.format(element="fire", name="fire_elemental")
        )
        self.attack = element.power
