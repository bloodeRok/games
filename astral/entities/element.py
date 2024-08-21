import pygame

from astral.base_entities import BaseElement
from astral.constants.images import (
    ELEMENT_BUTTON_IMAGE,
    ELEMENT_BUTTON_PRESSED_IMAGE,
)
from astral.constants.sizes import (
    BUTTON_DISTANCE,
    SCREEN_WIDTH,
    BUTTON_WIDTH,
    CARD_WIDTH,
    SCREEN_HEIGHT,
    BUTTON_HEIGHT,
    CARD_HEIGHT, MENU_CARD_DISTANCE,
)
from astral.entities.creatures.air_creatures import (
    AirPriest,
    Griffin,
    Harpy,
    AirElemental,
)
from astral.entities.creatures.earth_creatures import (
    EarthElemental, Dwarf, Bear, Troll
)
from astral.entities.creatures.fire_creatures import (
    Demon, Phoenix, WallOfFire, FireElemental
)
from astral.entities.creatures.spirit_creatures import (
    AstralChanneler, Ghost, SpectralWolf, SpiritElemental
)
from astral.entities.creatures.water_creatures import (
    Mermaid,
    Luska,
    Undine,
    WaterElemental,
)
from astral.game_init import screen


class Element(BaseElement):
    def __init__(self, x: int, y: int, element: str, team: str) -> None:
        super().__init__(x, y, element, team)
        self._pressed = False
        self._button_image = pygame.image.load(
            ELEMENT_BUTTON_IMAGE.format(element=self._element)
        ).convert()
        self._sprite = pygame.transform.scale(
            self._button_image,
            (BUTTON_WIDTH, BUTTON_HEIGHT)
        )
        self._creatures = self.__get_random_creatures()
        self._menu = ElementMenu(
            team=team,
            creatures=self._creatures,
            element=self
        )
        self._font_power = pygame.font.SysFont('Arial', 18)

    def __get_random_creatures(self):
        creatures_classes = []
        match self.element:
            case "fire":
                creatures_classes = [Demon, Phoenix, WallOfFire, FireElemental]
            case "water":
                creatures_classes = [Mermaid, Luska, Undine, WaterElemental]
            case "air":
                creatures_classes = [AirPriest, Griffin, Harpy, AirElemental]
            case "earth":
                creatures_classes = [Dwarf, Bear, Troll, EarthElemental]
            case "spirit":
                creatures_classes = [
                    AstralChanneler,
                    Ghost,
                    SpectralWolf,
                    SpiritElemental
                ]
        return creatures_classes

    def draw(self) -> None:
        screen.blit(source=self._sprite, dest=(self._x, self._y))

        power_text = self._font_power.render(
            str(self._power),
            True,
            (128, 128, 128)
        )
        text_rect = power_text.get_rect(
            center=(self._x + BUTTON_WIDTH // 1.2, self._y + BUTTON_HEIGHT // 2)
        )

        if self._pressed:
            self.__draw_element_menu()

        screen.blit(power_text, text_rect)

    def press(self) -> None:
        self._pressed = True
        self._button_image = pygame.image.load(
            ELEMENT_BUTTON_PRESSED_IMAGE.format(element=self._element)
        ).convert()
        self._sprite = pygame.transform.scale(
            self._button_image,
            (BUTTON_WIDTH, BUTTON_HEIGHT)
        )

    def unpress(self) -> None:
        self._pressed = False
        self._button_image = pygame.image.load(
            ELEMENT_BUTTON_IMAGE.format(element=self._element)
        ).convert()
        self._sprite = pygame.transform.scale(
            self._button_image,
            (BUTTON_WIDTH, BUTTON_HEIGHT)
        )

    def collidepoint(self, pos: tuple[int, int]) -> bool:
        return (
                self._x <= pos[0] <= self._x + BUTTON_WIDTH
                and self._y <= pos[1] <= self._y + BUTTON_HEIGHT
        )

    def __draw_element_menu(self) -> None:
        self._menu.draw()


class ElementMenu:
    def __init__(
            self,
            team: str,
            creatures,
            element
    ) -> None:

        self.creatures = []
        match team:
            case "radiant":
                left_top_x = BUTTON_DISTANCE + BUTTON_WIDTH + MENU_CARD_DISTANCE
            case "dire":
                left_top_x = (
                        SCREEN_WIDTH - BUTTON_WIDTH -
                        BUTTON_DISTANCE - CARD_WIDTH * 2
                        - MENU_CARD_DISTANCE * 2
                )
            case _:
                left_top_x = 0

        left_top_y = (
                (SCREEN_HEIGHT - (
                        BUTTON_HEIGHT + BUTTON_DISTANCE
                ) * 5) // 2
        )

        for i, CreatureClass in enumerate(creatures):
            x = left_top_x + (i % 2) * (CARD_WIDTH + MENU_CARD_DISTANCE)
            y = left_top_y + (i // 2) * (CARD_HEIGHT + MENU_CARD_DISTANCE)
            creature = CreatureClass(element)
            self.creatures.append((creature, x, y))

    def draw(self) -> None:
        for creature, x, y in self.creatures:
            creature.draw(x, y)
