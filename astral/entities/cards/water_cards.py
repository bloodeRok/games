from astral.entities import Element
from astral.entities.card import Card


class Mermaid(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Mermaid", hp=7, attack=1, element=element)

    def end_turn_ability(self) -> None:
        self._element += 1


class Luska(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Luska", hp=8, attack=9, element=element)


class Undine(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Undine", hp=8, attack=4, element=element)


class WaterElemental(Card):

    def __init__(self, element: Element) -> None:
        super().__init__(name="Fire elemental", hp=20, attack=0,
                         element=element)
        self.attack = element.power
