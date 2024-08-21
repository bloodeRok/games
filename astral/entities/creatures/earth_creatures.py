from astral.entities import Element
from astral.entities.creature import Card


class Dwarf(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Dwarf", hp=14, attack=3, element=element)

    def end_turn_ability(self) -> None:
        self._element += 2


class Bear(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Bear", hp=12, attack=5, element=element)


class Troll(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Troll", hp=20, attack=5, element=element)

    def end_turn_ability(self) -> None:
        self.hp += 2


class EarthElemental(Card):

    def __init__(self, element: Element) -> None:
        super().__init__(name="Earth elemental", hp=20, attack=0,
                         element=element)
        self.attack = element.power
