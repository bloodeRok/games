from astral.entities import Element
from astral.entities.card import Card


class Demon(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Demon", hp=5, attack=2, element=element)

    def end_turn_ability(self) -> None:
        self._element += 1


class Phoenix(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Phoenix", hp=8, attack=5, element=element)


class WallOfFire(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Wall of fire", hp=20, attack=0, element=element)


class FireElemental(Card):

    def __init__(self, element: Element) -> None:
        super().__init__(name="Fire elemental", hp=20, attack=0, element=element)
        self.attack = element.power




