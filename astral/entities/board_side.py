from astral.constants.sizes import CARD_HEIGHT, CARD_DISTANCES, CARD_WIDTH
from astral.entities import CardPlace


class BoardSide:
    def __init__(self, x: int, y: int) -> None:
        self.left_top_x = x
        self.left_top_y = y
        self.card_places = []

        y = self.left_top_y
        for card_num in range(6):
            self.card_places.append(
                CardPlace(
                    x=self.left_top_x,
                    y=y
                )
            )
            y += CARD_DISTANCES + CARD_HEIGHT

    def draw(self) -> None:
        for card_place in self.card_places:
            card_place.draw()
