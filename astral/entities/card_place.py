import pygame

from astral.base_entities import BaseCreature
from astral.constants.images import CARD_PLACE_IMAGE, CARD_PLACE_IMAGE_PRESSED
from astral.constants.sizes import CARD_WIDTH, CARD_HEIGHT
from astral.game_init import screen


class CardPlace:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y
        self._pressed = False
        self._empty = True
        self._button_image = pygame.image.load(
            CARD_PLACE_IMAGE
        ).convert()
        self._creature = None

    def draw(self) -> None:
        if self._empty:
            sprite = pygame.transform.scale(
                self._button_image,
                (CARD_WIDTH, CARD_HEIGHT)
            )
            screen.blit(source=sprite, dest=(self._x, self._y))
            return
        self._creature.draw(self._x, self._y, show_stats=True)

    def collidepoint(self, pos: tuple[int, int]) -> bool:
        return (
            self._x <= pos[0] <= self._x + CARD_WIDTH
            and self._y <= pos[1] <= self._y + CARD_HEIGHT
        )

    def press(self) -> None:
        self._pressed = True
        self._button_image = pygame.image.load(
            CARD_PLACE_IMAGE_PRESSED
        ).convert()

    def unpress(self) -> None:
        self._pressed = False
        self._button_image = pygame.image.load(
            CARD_PLACE_IMAGE
        ).convert()

    def put_creature(self, creature) -> None:
        self._empty = False
        self._creature = creature

    def remove_creature(self) -> None:
        self._empty = True
        self._creature = None

    def get_position(self) -> tuple[int, int]:
        return self._x, self._y

    # Getters/setters
    @property
    def empty(self) -> bool:
        return self._empty

    @empty.setter
    def empty(self, value: bool) -> None:
        self._empty = value

    @property
    def creature(self) -> BaseCreature | None:
        return self._creature
