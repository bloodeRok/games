import math
import sys

import pygame
from pygame.color import THECOLORS
from pygame.time import Clock

pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

circle_center = (WIDTH // 2, HEIGHT // 2)
circle_radius = 50
circle_color = THECOLORS['purple2']
clock = Clock()
SPEED = 5
bump_sound = pygame.mixer.Sound(file="bump.mp3")

current_angle = -30


def get_move(angle):
    angle = angle / 180. * math.pi
    return (
        int(SPEED * math.cos(angle)),
        int(SPEED * math.sin(angle))
    )


def move_circle(center, move):
    return center[0] + move[0], center[1] + move[1]


def get_angle(center, move):
    x, y = center
    mx, my = move
    if x - circle_radius <= 0 and mx < 0:
        bump_sound.play()
        return 180 - current_angle
    if x + circle_radius >= WIDTH and mx > 0:
        bump_sound.play()
        return 180 - current_angle
    if y - circle_radius <= 0 and my < 0:
        bump_sound.play()
        return -current_angle
    if y + circle_radius >= HEIGHT and my > 0:
        bump_sound.play()
        return -current_angle
    return current_angle


move = get_move(current_angle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(THECOLORS['black'])

    current_angle = get_angle(center=circle_center, move=move)
    move = get_move(angle=current_angle)
    circle_center = move_circle(center=circle_center, move=move)

    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

    pygame.display.flip()
    clock.tick(60)
