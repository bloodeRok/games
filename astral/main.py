import sys

import pygame

from astral.entities.board import Board
from astral.entities.player import Player
from astral.game_init import screen

clock = pygame.time.Clock()


def start_game():
    game_board = Board()
    radiant = Player(team="radiant", board_side=game_board.radiant_side)
    dire = Player(team="dire", board_side=game_board.dire_side)
    active_player = radiant
    unactive_player = dire
    active_player.my_turn = True
    while True:
        mouse_pos = pygame.mouse.get_pos()  # Получаем положение мыши один раз за цикл
        events = pygame.event.get()  # Получаем все события за цикл

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Левая кнопка мыши
                    if active_player.clean_board_button.collidepoint(mouse_pos):
                        for card in active_player.board_side.card_places:
                            card.remove_creature()
                    if active_player.end_turn_button.collidepoint(mouse_pos):
                        active_player.end_turn()
                        active_player, unactive_player = unactive_player, active_player
                        active_player.my_turn = True
                    else:
                        active_player.update(mouse_pos)

        screen.fill((255, 255, 255))
        game_board.draw()
        radiant.draw()
        dire.draw()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    start_game()
