import pygame

from astral.constants.images import END_TURN_IMAGE
from astral.constants.sizes import (
    END_TURN_HEIGHT,
    END_TURN_WIDTH,
    END_TURN_DISTANCE_X,
    END_TURN_DISTANCE_Y,
    SCREEN_WIDTH,
)
from astral.game_init import screen


class CleanBoardButton:
    def __init__(self, team: str) -> None:
        end_turn_img = pygame.image.load(END_TURN_IMAGE).convert()
        self._sprite = pygame.transform.scale(
            end_turn_img,
            (END_TURN_WIDTH, END_TURN_HEIGHT)
        )
        match team:
            case "radiant":
                self._x = END_TURN_DISTANCE_X
            case "dire":
                self._x = SCREEN_WIDTH - END_TURN_DISTANCE_X - END_TURN_WIDTH
            case _:
                self._x = 0
        self._y = END_TURN_DISTANCE_Y + 100

    def draw(self) -> None:
        screen.blit(source=self._sprite, dest=(self._x, self._y))

    def collidepoint(self, pos: tuple[int, int]) -> bool:
        return (
                self._x <= pos[0] <= self._x + END_TURN_WIDTH
                and self._y <= pos[1] <= self._y + END_TURN_HEIGHT
        )
