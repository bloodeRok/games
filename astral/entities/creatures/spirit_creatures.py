from astral.entities import Element
from astral.entities.creature import Card


class AstralChanneler(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(
            name="Astral Channeler", hp=5, attack=1, element=element)

    def end_turn_ability(self) -> None:
        self._element += 2


class Ghost(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Bear", hp=12, attack=5, element=element)


class SpectralWolf(Card):
    def __init__(self, element: Element) -> None:
        super().__init__(name="Spectral Wolf", hp=14, attack=5, element=element)

    def end_turn_ability(self) -> None:
        self.hp += 2


class SpiritElemental(Card):

    def __init__(self, element: Element) -> None:
        super().__init__(
            name="Spirit elemental",
            hp=20,
            attack=0,
            element=element
        )
        self.attack = self.hp
