import pygame

from astral.constants.sizes import PORTRAIT_WIDTH, PORTRAIT_HEIGHT
from astral.game_init import screen


class Portrait:
    def __init__(self, x: int, y: int, portrait_image: str) -> None:
        self.x = x
        self.y = y
        sprite = pygame.image.load(portrait_image).convert()
        self.sprite = pygame.transform.scale(
            sprite,
            (PORTRAIT_WIDTH, PORTRAIT_HEIGHT)
        )

    def draw(self) -> None:
        screen.blit(source=self.sprite, dest=(self.x, self.y))
