import sys

import pygame

from astral.entities.board import Board
from astral.entities.player import Player
from astral.game_init import screen

clock = pygame.time.Clock()


def start_game():
    game_board = Board()
    radiant = Player(team="radiant")
    dire = Player(team="dire")
    active_player = radiant
    unactive_player = dire
    active_player.my_turn = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == 1:
                    if active_player.end_turn_button.collidepoint(mouse_pos):
                        active_player.end_turn()
                        active_player, unactive_player = (
                            unactive_player, active_player
                        )
                        active_player.my_turn = True

        screen.fill((255, 255, 255))
        game_board.draw()
        active_player.update()

        radiant.draw()
        dire.draw()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    start_game()
