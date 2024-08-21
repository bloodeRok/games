import pygame

from astral.base_entities import BaseElement
from astral.constants.defaults import ELEMENTS
from astral.constants.images import HEROES_IMAGE
from astral.constants.sizes import (
    BUTTON_DISTANCE,
    SCREEN_WIDTH,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    SCREEN_HEIGHT,
    PORTRAIT_WIDTH,
    PORTRAIT_DISTANCE,
    HP_OFFSET,
    HP_RECT_WIDTH,
    HP_RECT_HEIGHT,
)
from astral.entities import Portrait, Element, EndTurnButton
from astral.game_init import screen


class Player:
    def __init__(self, team: str) -> None:
        if team not in ["dire", "radiant"]:
            raise ValueError("team must be either 'dire' or 'radiant'")

        self._my_turn = False
        self._team = team
        self._elements = self.__create_element_buttons()
        self._fire = self._elements["fire"]
        self._air = self._elements["air"]
        self._water = self._elements["water"]
        self._earth = self._elements["earth"]
        self._spirit = self._elements["spirit"]
        self._portrait = self.__create_portrait()
        self._font = pygame.font.SysFont('Arial', 24)
        self._end_turn_button = EndTurnButton(team=team)
        self._hp = 50

    def change_hp(self, diff: int) -> None:
        self._hp += diff

    def update(self) -> None:

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        if mouse_click:
            for button in self._elements.values():
                if button.collidepoint(mouse_pos):
                    self.__unpress_all_elements()
                    button.press()

    def end_turn(self) -> None:
        self.__unpress_all_elements()
        self._my_turn = False

    def draw(self) -> None:
        for button in self._elements.values():
            button.draw()
        self._portrait.draw()
        self.__draw_hp()
        if self._my_turn:
            self._end_turn_button.draw()

    # Help methods
    def __create_element_buttons(self) -> dict[str, BaseElement]:
        match self._team:
            case "radiant":
                x = BUTTON_DISTANCE
            case "dire":
                x = SCREEN_WIDTH - BUTTON_WIDTH - BUTTON_DISTANCE
            case _:
                x = 0

        y = (SCREEN_HEIGHT - (BUTTON_HEIGHT + BUTTON_DISTANCE) * 5) // 2

        elements_dict = {}
        for element in ELEMENTS:
            elements_dict[element] = Element(
                x=x,
                y=y,
                element=element,
                team=self._team
            )
            y += BUTTON_HEIGHT + BUTTON_DISTANCE

        return elements_dict

    def __create_portrait(self) -> Portrait:
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

    def __draw_hp(self) -> None:
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

    def __unpress_all_elements(self) -> None:
        for el_button in self._elements.values():
            el_button.unpress()

    # Getters/setters
    @property
    def fire(self) -> BaseElement:
        return self._fire

    @property
    def water(self) -> BaseElement:
        return self._water

    @property
    def air(self) -> BaseElement:
        return self._air

    @property
    def earth(self) -> BaseElement:
        return self._earth

    @property
    def light(self) -> BaseElement:
        return self._spirit

    @property
    def end_turn_button(self) -> EndTurnButton:
        return self._end_turn_button

    @property
    def my_turn(self) -> bool:
        return self._my_turn

    @my_turn.setter
    def my_turn(self, value: bool) -> None:
        self._my_turn = value
