from astral.constants.images import ELEMENT_ART
from astral.base_entities import BaseCreature, BaseElement


class AstralChanneler(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Astral Channeler",
            hp=5,
            attack=1,
            element=element,
            art=ELEMENT_ART.format(element="spirit", name="astral_channeler")
        )

    def end_turn_ability(self) -> None:
        self._element += 2


class Ghost(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Bear",
            hp=12,
            attack=5,
            element=element,
            art=ELEMENT_ART.format(element="spirit", name="ghost")
        )


class SpectralWolf(BaseCreature):
    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Spectral Wolf",
            hp=14,
            attack=5,
            element=element,
            art=ELEMENT_ART.format(element="spirit", name="spectral_wolf")
        )

    def end_turn_ability(self) -> None:
        self.hp += 2


class SpiritElemental(BaseCreature):

    def __init__(self, element: BaseElement) -> None:
        super().__init__(
            name="Spirit elemental",
            hp=20,
            attack=0,
            element=element,
            art=ELEMENT_ART.format(element="spirit", name="spirit_elemental")
        )
        self.attack = self.hp
