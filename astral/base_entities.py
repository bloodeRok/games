import pygame

from astral.constants.sizes import (
    CARD_HEIGHT,
    CARD_WIDTH,
    STATS_BORDER_DISTANCE,
    STATS_FONT_HEIGHT,
    ELEMENT_POWER_FONT_HEIGHT
)
from astral.constants.sounds import SUMMON_SOUNDS
from astral.game_init import screen


class BaseElement:
    def __init__(
            self,
            x: int,
            y: int,
            element: str,
            team: str,
            power: int
    ) -> None:
        self._x = x
        self._y = y
        self._element = element
        self._team = team
        self._power = power
        self._font_power = pygame.font.SysFont(
            'Arial',
            ELEMENT_POWER_FONT_HEIGHT
        )

    def draw(self) -> None:
        # Логика для отрисовки элемента
        pass

    def press(self) -> None:
        # Логика для нажатия на элемент
        pass

    def unpress(self) -> None:
        # Логика для снятия нажатия
        pass

    def collidepoint(self, pos: tuple[int, int]) -> bool:
        # Логика для определения коллизии точки с элементом
        pass

    @property
    def element(self) -> str:
        return self._element

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Сила должна быть целым числом.")
        if value < 0:
            raise ValueError("Сила не может быть отрицательной.")
        self._power = value


class BaseCreature:
    def __init__(
            self,
            name: str,
            hp: int,
            attack: int,
            element: BaseElement,
            art: str
    ) -> None:
        self._name = name
        self._hp = hp
        self._max_hp = hp
        self._attack = attack
        self._element = element
        self.art = pygame.image.load(
                art
            ).convert()
        self._sprite = pygame.transform.scale(
            self.art,
            (CARD_HEIGHT, CARD_WIDTH)
        )
        self._font = pygame.font.SysFont('Arial', STATS_FONT_HEIGHT)  # Определение шрифта для текста
        self._summon_sound = pygame.mixer.Sound(
            SUMMON_SOUNDS.format(
                element=self._element.element,
                name=self._name
            )
        )

    def take_damage(self, amount: int) -> None:
        self._hp -= amount
        if self._hp < 0:
            self._hp = 0

    def is_alive(self) -> bool:
        return self._hp > 0

    def attack_ability(self) -> None:
        pass

    def end_turn_ability(self) -> None:
        pass

    def battle_cry_ability(self) -> None:
        pass

    def draw(self, x: int, y: int, show_stats: bool = False) -> None:
        # Отображаем карту
        screen.blit(source=self._sprite, dest=(x, y))

        if show_stats:
            attack_text = f"ATK: {self._attack}"
            hp_text = f"HP: {self._hp}/{self._max_hp}"
            attack_width, attack_height = self._font.size(attack_text)
            hp_width, hp_height = self._font.size(hp_text)

            # Рендеринг черного прямоугольника для атаки
            attack_rect = pygame.Rect(
                x + STATS_BORDER_DISTANCE,
                y + CARD_HEIGHT - attack_height - STATS_BORDER_DISTANCE,
                attack_width,
                attack_height
            )
            pygame.draw.rect(screen, (0, 0, 0), attack_rect)

            # Рендеринг текста для атаки
            attack_render = self._font.render(
                attack_text,
                True,
                (255, 0, 0)
            )
            attack_pos = (
                x + STATS_BORDER_DISTANCE,
                y + CARD_HEIGHT - attack_height - STATS_BORDER_DISTANCE
            )
            screen.blit(attack_render, attack_pos)

            # Рендеринг черного прямоугольника для здоровья
            hp_rect = pygame.Rect(
                x + CARD_WIDTH - hp_width - STATS_BORDER_DISTANCE,
                y + CARD_HEIGHT - hp_height - STATS_BORDER_DISTANCE,
                hp_width,
                hp_height
            )
            pygame.draw.rect(screen, (0, 0, 0), hp_rect)

            # Рендеринг текста для здоровья
            hp_render = self._font.render(
                hp_text,
                True,
                (0, 255, 0)
            )
            hp_pos = (
                x + CARD_WIDTH - hp_width - STATS_BORDER_DISTANCE,
                y + CARD_HEIGHT - hp_height - STATS_BORDER_DISTANCE,
            )
            screen.blit(hp_render, hp_pos)

    def play_summon_sound(self) -> None:
        self._summon_sound.play()

    # Getters/setters
    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int):
        if not isinstance(value, int):
            raise ValueError("HP быть целым числом.")
        if value < 0:
            raise ValueError("HP не может быть отрицательным.")
        self._hp = value

    @property
    def max_hp(self) -> int:
        return self._hp

    @max_hp.setter
    def max_hp(self, value: int):
        if not isinstance(value, int):
            raise ValueError("HP быть целым числом.")
        if value < 0:
            raise ValueError("HP не может быть отрицательным.")
        self._max_hp = value

    @property
    def attack(self) -> int:
        return self._attack

    @attack.setter
    def attack(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Атака быть целым числом.")
        if value < 0:
            self._attack = 0
            return
        self._attack = value

    @property
    def element(self) -> BaseElement:
        return self._element
