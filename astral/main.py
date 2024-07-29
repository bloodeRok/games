import sys

import pygame

from astral.entities.board import Board
from astral.game_init import screen


def start_game():
    game_board = Board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        game_board.draw()

        pygame.display.update()

if __name__ == "__main__":
    start_game()
