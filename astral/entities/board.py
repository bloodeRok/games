from astral.constants.sizes import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    CARD_WIDTH,
    CARD_DISTANCE,
    CARD_HEIGHT
)
from astral.entities import BoardSide


class Board:
    def __init__(self):
        column_height = CARD_HEIGHT * 6 + CARD_DISTANCE * 5
        centered_y = (SCREEN_HEIGHT - column_height) // 2

        radiant_x = SCREEN_WIDTH // 2 - CARD_WIDTH - CARD_DISTANCE // 2
        dire_x = SCREEN_WIDTH // 2 + CARD_DISTANCE // 2

        self.radiant_side = BoardSide(
            x=radiant_x,
            y=centered_y
        )
        self.dire_side = BoardSide(
            x=dire_x,
            y=centered_y
        )

    def draw(self) -> None:
        self.radiant_side.draw()
        self.dire_side.draw()
