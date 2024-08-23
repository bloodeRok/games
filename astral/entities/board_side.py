from astral.constants.sizes import CARD_HEIGHT, CARD_DISTANCE
from .card_place import CardPlace


class BoardSide:
    def __init__(self, x: int, y: int) -> None:
        self.left_top_x = x
        self.left_top_y = y
        self._card_places = []

        y = self.left_top_y
        for card_num in range(6):
            self._card_places.append(
                CardPlace(
                    x=self.left_top_x,
                    y=y
                )
            )
            y += CARD_DISTANCE + CARD_HEIGHT

    def draw(self) -> None:
        for card_place in self._card_places:
            card_place.draw()

    def get_active_card_slot(
            self,
            mouse_pos: tuple[int, int]
    ) -> CardPlace | None:

        for card_place in self._card_places:
            if card_place.collidepoint(mouse_pos):
                self.unpress_all_card_slots()
                card_place.press()
                return card_place
        return None

    def unpress_all_card_slots(self) -> None:
        for card_place in self._card_places:
            card_place.unpress()

    @property
    def card_places(self) -> list[CardPlace]:
        return self._card_places
