from astral.entities import Element


class Card:
    def __init__(
            self,
            name: str,
            hp: int,
            attack: int,
            element: Element
    ) -> None:
        self._name = name
        self._hp = hp
        self._attack = attack
        self._element = element

    #Геттеры и Сеттеры
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой.")
        self._name = value

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
    def element(self) -> Element:
        return self._element

    def take_damage(self, amount: int) -> None:
        self._hp -= amount
        if self._hp < 0:
            self._hp = 0

    def is_alive(self) -> bool:
        return self.hp > 0

    def end_turn_ability(self) -> None:
        pass
