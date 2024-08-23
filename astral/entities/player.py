import random
import time

import pygame

from astral.base_entities import BaseElement
from astral.constants.defaults import ELEMENTS, ANIMATION_DURATION
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
    HP_RECT_HEIGHT, HP_FONT_HEIGHT,
)
from astral.entities import Portrait, Element, EndTurnButton, BoardSide, \
    CleanBoardButton
from astral.game_init import screen


class Player:
    def __init__(self, team: str, board_side: BoardSide) -> None:
        if team not in ["dire", "radiant"]:
            raise ValueError("team must be either 'dire' or 'radiant'")

        self._my_turn = False
        self._team = team
        self._board_side = board_side
        self._elements = self.__create_element_buttons()
        self._fire = self._elements["fire"]
        self._air = self._elements["air"]
        self._water = self._elements["water"]
        self._earth = self._elements["earth"]
        self._spirit = self._elements["spirit"]
        self._portrait = self.__create_portrait()
        self._font = pygame.font.SysFont('Arial', HP_FONT_HEIGHT)
        self._end_turn_button = EndTurnButton(team=team)
        self._clean_board_button = CleanBoardButton(team=team) # TODO test!
        self._active_card_slot = None
        self._active_element = None
        self._hp = 50

        self._animating_creature = None
        self._animation_start_time = None
        self._start_position = None
        self._end_position = None
        self._animation_in_progress = False

    def change_hp(self, diff: int) -> None:
        self._hp += diff

    def start_animation(self, creature, start_pos, end_pos):
        self._animating_creature = creature
        self._animating_creature.play_summon_sound()
        self._animation_start_time = time.time()
        self._start_position = start_pos
        self._end_position = end_pos
        self._animation_in_progress = True

    def update_animation(self):
        if self._animating_creature and self._animation_start_time:
            elapsed_time = time.time() - self._animation_start_time
            progress = min(elapsed_time / ANIMATION_DURATION, 1.0)

            current_x = (1 - progress) * self._start_position[0] + progress * self._end_position[0]
            current_y = (1 - progress) * self._start_position[1] + progress * self._end_position[1]

            self._animating_creature.draw(current_x, current_y, show_stats=True)

            # Завершение анимации
            if progress >= 1.0:
                self._active_card_slot.put_creature(
                    creature=self._animating_creature
                )
                self._active_card_slot.unpress()
                self._active_card_slot = None
                self._animating_creature = None
                self._animation_start_time = None
                self._animation_in_progress = False

    def update(self, mouse_pos) -> None:
        if self._animation_in_progress:
            return

        new_active_card_slot = self._board_side.get_active_card_slot(mouse_pos)
        if new_active_card_slot:
            self._active_card_slot = new_active_card_slot

        for element in self._elements.values():
            if element.collidepoint(mouse_pos):
                self.__unpress_all_elements()
                self._active_element = element
                element.press()

        if self._active_element:
            collided_creature = self._active_element.menu.get_collided_creature(mouse_pos)
            if (
                    collided_creature
                    and self._active_card_slot
                    and self._active_card_slot.empty
            ):
                print(collided_creature.art)

                new_creature = type(collided_creature)(
                    element=self._active_element
                )

                self.start_animation(
                    creature=new_creature,
                    start_pos=self._portrait.get_position(),
                    end_pos=self._active_card_slot.get_position(),
                )

    def end_turn(self) -> None:
        self._active_element = None
        self.__unpress_all_elements()
        self._active_card_slot = None
        self._board_side.unpress_all_card_slots()
        self._my_turn = False

    def draw(self) -> None:
        for button in self._elements.values():
            button.draw()
        self._portrait.draw()
        self.__draw_hp()
        self.update_animation()
        if self._my_turn:
            self._end_turn_button.draw()
            self._clean_board_button.draw()

    # Help methods
    def __create_element_buttons(self) -> dict[str, Element]:
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
                team=self._team,
                power=random.randint(1, 6)
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
        portrait_x, portrait_y = self._portrait.get_position()
        match self._team:
            case "radiant":
                return (
                    portrait_x + PORTRAIT_WIDTH + HP_OFFSET,
                    portrait_y
                )
            case "dire":
                return (
                    portrait_x - HP_RECT_WIDTH - HP_OFFSET,
                    portrait_y
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
    def clean_board_button(self) -> CleanBoardButton:
        return self._clean_board_button

    @property
    def board_side(self) -> BoardSide:
        return self._board_side


    @property
    def my_turn(self) -> bool:
        return self._my_turn

    @my_turn.setter
    def my_turn(self, value: bool) -> None:
        self._my_turn = value
