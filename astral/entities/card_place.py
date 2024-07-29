import pygame

from astral.constants.images import CARD_PLACE_IMAGE
from astral.constants.sizes import CARD_WIDTH, CARD_HEIGHT
from astral.game_init import screen


class CardPlace:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        sprite = pygame.image.load(CARD_PLACE_IMAGE).convert()
        self.sprite = pygame.transform.scale(sprite, (CARD_WIDTH, CARD_HEIGHT))

    def draw(self) -> None:
        screen.blit(source=self.sprite, dest=(self.x, self.y))
