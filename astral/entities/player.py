import pygame

from astral.constants.defaults import ELEMENTS
from astral.constants.images import HEROES_IMAGE
from astral.constants.sizes import (
    BUTTON_DISTANCE,
    SCREEN_WIDTH,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    SCREEN_HEIGHT,
    PORTRAIT_WIDTH, PORTRAIT_DISTANCE, HP_OFFSET, HP_RECT_WIDTH, HP_RECT_HEIGHT,
)
from astral.entities import ElementButton, Portrait
from astral.game_init import screen


class Player:
    def __init__(self, team: str) -> None:
        if team not in ["dire", "radiant"]:
            raise ValueError("team must be either 'dire' or 'radiant'")

        self._team = team
        self._element_buttons = self.create_element_buttons()
        self._portrait = self.create_portrait()
        self._font = pygame.font.SysFont('Arial', 24)
        self._hp = 50

    def create_element_buttons(self) -> list[ElementButton]:
        buttons = []
        match self._team:
            case "radiant":
                x = BUTTON_DISTANCE
            case "dire":
                x = SCREEN_WIDTH - BUTTON_WIDTH - BUTTON_DISTANCE
            case _:
                x = 0

        y = (SCREEN_HEIGHT - (BUTTON_HEIGHT + BUTTON_DISTANCE) * 5) // 2

        for element in ELEMENTS:
            button = ElementButton(x=x, y=y, element=element)
            buttons.append(button)
            y += BUTTON_HEIGHT + BUTTON_DISTANCE

        return buttons

    def create_portrait(self) -> Portrait:
        match self._team:
            case "radiant":
                x = PORTRAIT_DISTANCE
            case "dire":
                x = SCREEN_WIDTH - PORTRAIT_WIDTH - PORTRAIT_DISTANCE
            case _:
                x = 0
        return Portrait(
            x=x,
            y=SCREEN_HEIGHT // 20,
            portrait_image=HEROES_IMAGE.format(name=f"test_{self._team}")
        )

    def draw_hp(self) -> None:
        """Отрисовка прямоугольника с жизнями (HP)."""
        # Создаем прямоугольник
        hp_rect_x, hp_rect_y = self.__get_initial_hp_rect_position()
        hp_rect = pygame.Rect(
            hp_rect_x,
            hp_rect_y,
            HP_RECT_WIDTH,
            HP_RECT_HEIGHT
        )

        pygame.draw.rect(screen, (0, 0, 0), hp_rect, width=2)

        hp_text = self._font.render(
            f"HP: {self._hp}",
            True,
            (0, 0, 0)  # Черный цвет текста
        )
        text_rect = hp_text.get_rect(center=hp_rect.center)
        screen.blit(hp_text, text_rect)

    def __get_initial_hp_rect_position(self) -> tuple[int, int]:
        match self._team:
            case "radiant":
                return (
                    self._portrait.x
                    + PORTRAIT_WIDTH
                    + HP_OFFSET,
                    self._portrait.y
                )
            case "dire":
                return (
                    self._portrait.x -
                    HP_RECT_WIDTH -
                    HP_OFFSET,
                    self._portrait.y
                )
            case _:
                return 0, 0

    def change_hp(self, diff: int) -> None:
        self._hp += diff

    def update(self) -> None:
        def unpress_all_elements() -> None:
            for el_button in self._element_buttons:
                el_button.unpress()

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        for button in self._element_buttons:
            if mouse_click:
                if button.collidepoint(mouse_pos):
                    unpress_all_elements()
                    button.press()

    def draw(self) -> None:
        for button in self._element_buttons:
            button.draw()
        self._portrait.draw()
        self.draw_hp()
