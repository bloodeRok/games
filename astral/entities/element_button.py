import pygame

from astral.constants.images import (
    ELEMENT_BUTTON_IMAGE,
    ELEMENT_BUTTON_PRESSED_IMAGE,
)
from astral.constants.sizes import BUTTON_WIDTH, BUTTON_HEIGHT
from astral.game_init import screen


class ElementButton:
    def __init__(self, x: int, y: int, element: str):
        self._x = x
        self._y = y
        self._element = element
        self._pressed = False
        self._button_image = pygame.image.load(
                ELEMENT_BUTTON_IMAGE.format(element=self._element)
            ).convert()
        self._sprite = pygame.transform.scale(
            self._button_image,
            (BUTTON_WIDTH, BUTTON_HEIGHT)
        )

    def draw(self) -> None:
        screen.blit(source=self._sprite, dest=(self._x, self._y))

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
