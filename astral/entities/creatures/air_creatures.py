from astral.entities import Element
from astral.entities.creature import Card


class AirPriest(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Air priest", hp=9, attack=2, element=element)

    def end_turn_ability(self) -> None:
        self._element += 1


class Phoenix(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Phoenix", hp=10, attack=4, element=element)


class Harpy(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Harpy", hp=3, attack=7, element=element)


class AirElemental(Card):

    def __init__(self, element: Element) -> None:
        super().__init__(name="Air elemental", hp=20, attack=0,
                         element=element)
        self.attack = element.power
