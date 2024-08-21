import pygame

from astral.constants.sizes import CARD_HEIGHT, CARD_WIDTH
from astral.game_init import screen


class BaseElement:
    def __init__(self, x: int, y: int, element: str, team: str) -> None:
        self._x = x
        self._y = y
        self._element = element
        self._team = team
        self._power = 3
        # Логика создания кнопок, меню и других элементов

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
        self._art = pygame.image.load(
                art
            ).convert()
        self._sprite = pygame.transform.scale(
            self._art,
            (CARD_HEIGHT, CARD_WIDTH)
        )

    def take_damage(self, amount: int) -> None:
        self._hp -= amount
        if self._hp < 0:
            self._hp = 0

    def is_alive(self) -> bool:
        return self.hp > 0

    def attack_ability(self) -> None:
        pass

    def end_turn_ability(self) -> None:
        pass

    def battle_cry_ability(self) -> None:
        pass

    def draw(self, x: int, y: int, show_stats: bool = False) -> None:
        screen.blit(source=self._sprite, dest=(x, y))

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
