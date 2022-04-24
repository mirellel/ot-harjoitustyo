import sys
import pygame
from game import MainRun
from settings import clock, window, white, pink, start_game, \
     font, largefont, victory, play_again, defeat
class Main():
    def __init__(self):
        pygame.init()
        self.game = MainRun()

    def run_game(self):
        done = False
        self.game = MainRun()
        while not done:
            self.game.run_logic()
            self.game.process_events()
            self.game.display_frame()
            clock.tick(30)
            if self.game.lost is True:
                self.lose_menu()
            if self.game.win is True:
                self.win_menu()
            pygame.display.update()

    def start_menu(self):
        pygame.display.set_caption("Word.py")
        pygame.mouse.set_visible(True)
        window.fill(pink)
        while True: # pylint: disable=too-many-nested-blocks
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
                        self.run_game()
            pygame.draw.rect(window, white, pygame.Rect(50, 100, 400, 100))
            pygame.draw.rect(window, white, pygame.Rect(50, 250, 400, 100))
            if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
                pygame.draw.rect(window, (242, 242, 242),
                                 pygame.Rect(50, 250, 400, 100))
            window.blit(start_game, (120, 270))
            window.blit(font.render("Log In", True, pink), (100, 115))
            pygame.display.update()

    def win_menu(self):
        while True: # pylint: disable=too-many-nested-blocks
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 450 and 400 <= mouse[1] <= 500:
                        self.start_menu()
                    if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
                        self.run_game()
            pygame.draw.rect(window, pink, pygame.Rect(0, 0, 500, 600))
            window.blit(largefont.render(
                self.game.word, True, white), (120, 30))
            pygame.draw.rect(window, white, pygame.Rect(50, 100, 400, 100))
            window.blit(victory, (100, 115))
            pygame.draw.rect(window, white, pygame.Rect(50, 250, 400, 100))
            if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
                pygame.draw.rect(window, (242, 242, 242),
                                 pygame.Rect(50, 250, 400, 100))
            window.blit(play_again, (120, 270))
            pygame.draw.rect(window, white, pygame.Rect(50, 400, 400, 100))
            if 50 <= mouse[0] <= 450 and 400 <= mouse[1] <= 500:
                pygame.draw.rect(window, (242, 242, 242),
                                 pygame.Rect(50, 400, 400, 100))
            window.blit(font.render("Main menu", True, pink), (155, 420))
            pygame.display.update()

    def lose_menu(self):
        while True: # pylint: disable=too-many-nested-blocks
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 450 and 400 <= mouse[1] <= 500:
                        self.start_menu()
                    if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
                        self.run_game()
            pygame.draw.rect(window, pink, pygame.Rect(0, 0, 500, 600))
            window.blit(largefont.render(
                self.game.word, True, white), (120, 30))
            pygame.draw.rect(window, white, pygame.Rect(50, 100, 400, 100))
            window.blit(defeat, (100, 115))
            pygame.draw.rect(window, white, pygame.Rect(50, 250, 400, 100))
            if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
                pygame.draw.rect(window, (242, 242, 242),
                                 pygame.Rect(50, 250, 400, 100))
            window.blit(play_again, (120, 270))
            pygame.draw.rect(window, white, pygame.Rect(50, 400, 400, 100))
            if 50 <= mouse[0] <= 450 and 400 <= mouse[1] <= 500:
                pygame.draw.rect(window, (242, 242, 242),
                                 pygame.Rect(50, 400, 400, 100))
            window.blit(font.render("Main menu", True, pink), (155, 420))
            pygame.display.update()


main = Main()

main.start_menu()
