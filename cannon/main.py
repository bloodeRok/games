"""
+-----------------------+
|   ||||||              | <- target
|                       |
|                       |
|           *           | <- bullet
|                       |
|                       |
|          /'\          | <- cannon
+-----------------------+
"""

import random
import sys

import pygame
from pygame import Surface
from pygame.color import THECOLORS

pygame.init()

WIDTH = 640
HEIGHT = 480
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
shoot_sound = pygame.mixer.Sound("shoot.mp3")

dmg_sound_1 = pygame.mixer.Sound("dmg1.mp3")
dmg_sound_2 = pygame.mixer.Sound("dmg2.mp3")
dmg_sound_3 = pygame.mixer.Sound("dmg3.mp3")
dmg_sounds = [dmg_sound_1, dmg_sound_2, dmg_sound_3]

class Cannon:
    def __init__(self, color: tuple[int] = THECOLORS["yellow"]) -> None:
        self.color = color
        cannon_center = WIDTH // 2
        self.points = [
            (cannon_center - 25, HEIGHT),
            (cannon_center + 25, HEIGHT),
            (cannon_center, HEIGHT - 50)
        ]

    def draw(self) -> None:
        pygame.draw.lines(
            surface=screen,
            color=self.color,
            closed=True,
            points=self.points
        )


class Bullet:
    def __init__(
            self,
            radius: int,
            center: tuple[int, int] = (WIDTH // 2, HEIGHT - 50),
            color: tuple[int] = THECOLORS["white"],
            speed: int = 5
    ) -> None:
        self.center = center
        self.radius = radius
        self.color = color
        self.speed = speed

    def draw(self) -> None:
        pygame.draw.circle(
            surface=screen,
            color=self.color,
            center=self.center,
            radius=self.radius
        )

    def move(self):
        self.center = (self.center[0], self.center[1] - self.speed)


class Target:
    def __init__(
            self,
            speed: int,
            start_pos: tuple[int, int],
            width: int,
            height: int,
            color: tuple[int] = THECOLORS["red"]
    ) -> None:
        self.color = color
        self.speed = speed
        self.width = width
        self.rect = pygame.Rect(start_pos[0], start_pos[1], width, height)

    def draw(self):
        pygame.draw.rect(surface=screen, color=self.color, rect=self.rect)

    def move(self):
        if self.rect.x + self.speed < 0 \
                or self.rect.x + self.rect.width + self.speed > WIDTH:
            self.speed = -self.speed
        self.rect.move_ip(self.speed, 0)



colors = list(THECOLORS.values())

def get_random_color():
    return random.choice(colors)

cannon = Cannon()
target = Target(speed=2, start_pos=(20, 20), width=200, height=20)
bullets = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullet = Bullet(radius=2)
                bullets.append(bullet)
                shoot_sound.play()

    screen.fill(THECOLORS['black'])

    target.move()

    for bullet in bullets[:]:
        bullet.move()
        if bullet.center[1] <= 0:
            bullets.remove(bullet)
        elif target.rect.collidepoint(bullet.center):
            bullets.remove(bullet)
            target.color = random.choice(colors)
            random.choice(dmg_sounds).play()

    cannon.draw()
    target.draw()
    for bullet in bullets:
        bullet.draw()

    pygame.display.flip()
    clock.tick(60)