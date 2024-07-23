import random
import sys
import pygame
from pygame import Surface
from pygame.color import THECOLORS

MAZE_MAP = [
    '#######@#####',
    '#  K#     #K#',
    '# ### # # # #',
    '# #   # #   #',
    '# # # #######',
    '# # #       #',
    '# # ####### #',
    '# #     #K# #',
    '# ##### # # #',
    '#   #   # # #',
    '### # ### # #',
    '#     #     #',
    '#X###########',
]

BLOCK_SIDE = 64
CELL_SIDE = 64
WIDTH = len(MAZE_MAP[0])
HEIGHT = len(MAZE_MAP)

SCREEN_WIDTH = WIDTH * BLOCK_SIDE
SCREEN_HEIGHT = HEIGHT * BLOCK_SIDE

wall_textures = []
for i in range(0, 16):
    wall_textures.append(pygame.image.load(f'img/wall_64x64_{i}.png'))

key_texture = pygame.image.load(f'img/key.png')
door_textures = []
for i in range(4):
    door_textures.append(pygame.image.load(f'img/door{i}.png'))
player_texture = pygame.image.load(f'img/player.png')


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('arial', 60)
text = font.render('You Win!', True, THECOLORS['green'])


class Wall:
    def __init__(self, x: int, y: int, texture: Surface) -> None:
        self.x = x
        self.y = y
        self.coordinates = (x, y)
        self.sprite = texture

    def draw(self):
        screen.blit(self.sprite, (self.x * CELL_SIDE, self.y * CELL_SIDE))


class Key:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.coordinates = (x, y)
        self.cell = pygame.Rect(x, y, CELL_SIDE, CELL_SIDE)
        self.sprite = key_texture
        self.is_taken = False

    def draw(self):
        screen.blit(self.sprite, (self.x * CELL_SIDE, self.y * CELL_SIDE))


class Door:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.coordinates = (x, y)
        self.cell = pygame.Rect(x, y, CELL_SIDE, CELL_SIDE)
        self.sprites = door_textures
        self.current_sprite = 0
        self.number_of_keys = 0
        self.is_open = False

    def draw(self):
        screen.blit(
            self.sprites[self.current_sprite],
            (self.x * CELL_SIDE, self.y * CELL_SIDE)
        )
    
    def open(self) -> None:
        self.current_sprite = -1
        self.is_open = True

    def change_sprite(self):
        if not self.sprites[self.current_sprite + 1] == self.sprites[-1]:
            self.current_sprite += 1

class Maze:
    def __init__(self) -> None:
        self.walls = []
        self.player = None
        self.door = None
        self.keys = []

        y = 0
        for line in MAZE_MAP:
            x = 0
            for block in line:
                match block:
                    case "#":
                        self.walls.append(
                            Wall(x=x, y=y, texture=random.choice(wall_textures))
                        )
                    case "@":
                        self.player = Player(x=x, y=y)
                    case "X":
                        self.door = Door(x=x, y=y)
                    case "K":
                        self.keys.append(Key(x=x, y=y))
                x += 1
            y += 1

    def move_player(self):
        self.set_player_direction(self.player.direction)
        self.player.move()
        for key in self.keys:
            if self.get_player_cell() == self.get_key_cell(key=key) and not key.is_taken:
                key.is_taken = True
                self.door.number_of_keys += 1
                self.door.change_sprite()
                if self.door.number_of_keys == len(self.keys):
                    self.door.open()

    def set_player_direction(self, direction: int) -> None:
        if self.player_can_move(direction):
            self.player.direction = direction
        else:
            self.player.direction = Direction.NONE

    def player_can_move(self, direction: int) -> bool:
        pcx, pcy = self.get_player_cell()
        match direction:
            case Direction.UP:
                new_x, new_y = pcx, pcy - 1
            case Direction.DOWN:
                new_x, new_y = pcx, pcy + 1
            case Direction.LEFT:
                new_x, new_y = pcx - 1, pcy
            case Direction.RIGHT:
                new_x, new_y = pcx + 1, pcy
            case _:
                return False

        if (
                new_x < 0 or new_x >= SCREEN_WIDTH // CELL_SIDE 
                or new_y < 0 or new_y >= SCREEN_HEIGHT // CELL_SIDE
        ):
            return False
        
        if (
                self.get_door_cell(door=self.door) == (new_x, new_y) 
                and not self.door.is_open
        ):
            return False

        for wall in self.walls:
            if wall.coordinates == (new_x, new_y):
                return False

        return True

    def draw(self) -> None:
        for wall in self.walls:
            wall.draw()
        self.door.draw()
        for key in self.keys:
            if not key.is_taken:
                key.draw()
        self.player.draw()


    def win(self) -> bool:
        if self.get_player_cell() == self.get_door_cell(door=self.door):
            return True

    def get_player_cell(self) -> tuple[int, int]:
        return self.player.x, self.player.y

    def get_key_cell(self, key: Key) -> tuple[int, int]:
        return key.x, key.y

    def get_door_cell(self, door: Door) -> tuple[int, int]:
        return door.x, door.y


class Direction:
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Player:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.sprite = player_texture
        self.step = 1
        self.direction = Direction.NONE

    def draw(self) -> None:
        screen.blit(self.sprite, (self.x * CELL_SIDE, self.y * CELL_SIDE))

    def move(self) -> None:
        match self.direction:
            case Direction.NONE:
                return
            case Direction.UP:
                self.y -= self.step
            case Direction.DOWN:
                self.y += self.step
            case Direction.LEFT:
                self.x -= self.step
            case Direction.RIGHT:
                self.x += self.step

def start_level():
    maze = Maze()

    while True:
        if maze.win():
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    maze.set_player_direction(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    maze.set_player_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    maze.set_player_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    maze.set_player_direction(Direction.RIGHT)
            elif event.type == pygame.KEYUP:
                maze.set_player_direction(Direction.NONE)

        maze.move_player()

        screen.fill((0, 0, 0))
        maze.draw()

        pygame.display.flip()
        pygame.time.wait(66)


def show_win_message():
    screen.blit(text, (CELL_SIDE * 2, SCREEN_HEIGHT - CELL_SIDE - 60))
    pygame.display.flip()
    pygame.time.wait(1000)


while True:
    start_level()
    show_win_message()
