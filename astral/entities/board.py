from astral.constants.sizes import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    CARD_WIDTH,
    CARD_DISTANCES, CARD_HEIGHT
)
from astral.entities import BoardSide


class Board:
    def __init__(self):
        column_height = CARD_HEIGHT * 6 + CARD_DISTANCES * 5
        centered_y = (SCREEN_HEIGHT - column_height) // 2

        player_x = SCREEN_WIDTH // 2 - CARD_WIDTH - CARD_DISTANCES // 2
        opponent_x = SCREEN_WIDTH // 2 + CARD_DISTANCES // 2

        self.player_side = BoardSide(
            x=player_x,
            y=centered_y
        )
        self.opponent_side = BoardSide(
            x=opponent_x,
            y=centered_y
        )

    def draw(self) -> None:
        self.player_side.draw()
        self.opponent_side.draw()
