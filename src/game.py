
from curses import window
import random
import sys
import pygame
from pygame.locals import *  # pylint: disable=unused-wildcard-import, disable=wildcard-import
from checkguess import CheckGuess
from settings import *  # pylint: disable=unused-wildcard-import, disable=wildcard-import

pygame.init()

checkguess = CheckGuess()


class MainRun(): # pylint: disable=too-many-instance-attributes
    def __init__(self):
        self.time1 = 0
        self.time2 = 0
        self.turns = 0
        self.guess = ""
        self.win = False
        self.lost = False
        self.incorrect_word = False
        self.wrong_num_of_letters = False
        with open("src/wordlist.txt", encoding="utf-8") as file:
            self.wordlist = [word.replace("\n", "") for word in file]
        self.word = self.wordlist[random.randint(0, 2000)].upper()
        self.win_list = [green, green, green, green, green]

    def process_events(self): #pylint: disable=too-many-statements
        spacing = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                if event.type == pygame.KEYDOWN:
                    # arvauksen pyyhkiminen
                    if event.key == pygame.K_BACKSPACE:
                        if self.guess:
                            self.guess = self.guess[:-1]
                    # arvauksen tekeminen
                    elif event.key == pygame.K_RETURN:
                        # hyväksytään vain viisikirjaiminen arvaus
                        if len(self.guess) == 5:
                            print(self.guess.lower())
                            # tarkastetaan onko arvaus kelpaava sana
                            if self.guess.lower() in self.wordlist:
                                # kutsutaan checkguess luokkaa tarkastamaan arvaus
                                if checkguess.check(self.word, self.guess) == self.win_list:
                                    self.win = True
                                for j in range(0, 5):
                                    checkguess.renderlist[j] = font.render(
                                        self.guess[j], True, black)
                                    pygame.draw.rect(window, checkguess.guesscolourcode[j], pygame.Rect(  # pylint: disable=line-too-long
                                        60 + spacing, 50 + (self.turns*80), 50, 50))
                                    window.blit(
                                        checkguess.renderlist[j], (70 + spacing, 50 + (self.turns*80)))  # pylint: disable=line-too-long
                                    spacing += 80
                                self.turns += 1
                                self.guess = ""
                                window.fill(white, (0, 500, 500, 200))
                            else:
                                self.incorrect_word = True  # merkitsee kelpaamattoman sanan
                                self.time1 = 0
                        else:
                            self.wrong_num_of_letters = True
                            self.time2 = 0
                            # merkitsee, jos sanassa on liian vähän kirjaimia
                    # arvaus ilmestyy ruutuihin
                    else:
                        if len(self.guess) < 5:
                            if event.unicode.isalpha():
                                self.guess += event.unicode.upper()
                    window.fill(white, (0, 500, 500, 200))

    def run_logic(self): #pylint: disable=too-many-statements
        if self.incorrect_word is True:
            self.time2 = 0
            self.wrong_num_of_letters = False
            text_surface = font.render("Not in word list!", True, red)
            window.blit(text_surface, (105, 3))
            self.time1 += 1

        if self.wrong_num_of_letters is True:
            self.incorrect_word = False
            self.time1 = 0
            text_surface = font.render("Not enough letters!", True, red)
            window.blit(text_surface, (105, 0))
            self.time2 += 1

        if self.time1 == 60:
            self.incorrect_word = False
            self.time1 = 0
            self.guess = ""
            pygame.draw.rect(window, white, pygame.Rect(50, 10, 600, 40))

        if self.time2 == 60:
            self.wrong_num_of_letters = False
            self.time2 = 0
            self.guess = ""
            pygame.draw.rect(window, white, pygame.Rect(50, 10, 600, 40))
            pygame.draw.rect(window, white, pygame.Rect(272, 40, 28, 50))

    def display_frame(self): #pylint: disable=too-many-statements
        if self.guess:
            letterspacing = 0
            for i in range(len(self.guess)):
                word_surface = font.render(self.guess[i], True, black)
                window.blit(word_surface, (180+letterspacing, 530))
                letterspacing += 30
        if self.turns == 6 and not self.win:
            self.lost = True

            while True:
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 50 <= mouse[0] <= 450 and 400 <= mouse[1] <= 500:
                            pygame.quit()
                            sys.exit()
                        if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
                            main()
                pygame.draw.rect(window, pink, pygame.Rect(0, 0, 500, 600))
                window.blit(largefont.render(
                    self.word, True, white), (120, 30))
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
                window.blit(quit_game, (155, 420))
                pygame.display.update()
        if self.win is True:
            while True:
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 50 <= mouse[0] <= 450 and 400 <= mouse[1] <= 500:
                            pygame.quit()
                            sys.exit()
                        if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
                            main()
                pygame.draw.rect(window, pink, pygame.Rect(0, 0, 500, 600))
                window.blit(largefont.render(
                    self.word, True, white), (120, 30))
                pygame.draw.rect(window, white, pygame.Rect(50, 100, 400, 100))
                pygame.draw.rect(window, white, pygame.Rect(50, 250, 400, 100))
                pygame.draw.rect(window, white, pygame.Rect(50, 400, 400, 100))
                if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
                    pygame.draw.rect(window, (242, 242, 242),
                                     pygame.Rect(50, 250, 400, 100))
                pygame.draw.rect(window, white, pygame.Rect(50, 400, 400, 100))
                if 50 <= mouse[0] <= 450 and 400 <= mouse[1] <= 500:
                    pygame.draw.rect(window, (242, 242, 242),
                                     pygame.Rect(50, 400, 400, 100))
                if self.turns == 1:
                    window.blit(unbelievable, (100, 115))
                    window.blit(play_again, (120, 270))
                    window.blit(quit_game, (155, 420))
                if self.turns == 2:
                    window.blit(splendid, (100, 115))
                    window.blit(play_again, (120, 270))
                    window.blit(quit_game, (155, 420))
                if self.turns == 3:
                    window.blit(wow, (100, 115))
                    window.blit(play_again, (120, 270))
                    window.blit(quit_game, (155, 420))
                if self.turns == 4:
                    window.blit(great, (100, 115))
                    window.blit(play_again, (120, 270))
                    window.blit(quit_game, (155, 420))
                if self.turns == 5:
                    window.blit(good, (100, 115))
                    window.blit(play_again, (120, 270))
                    window.blit(quit_game, (155, 420))
                if self.turns == 6:
                    window.blit(phew, (100, 115))
                    window.blit(play_again, (120, 270))
                    window.blit(quit_game, (155, 420))
                pygame.display.update()

        pygame.display.flip()


def main_menu(): #pylint: disable=too-many-statements
    pygame.init()
    pygame.display.set_caption("Word.py")
    pygame.mouse.set_visible(True)
    window.fill(pink)
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= mouse[0] <= 450 and 400 <= mouse[1] <= 500:
                    pygame.quit()
                    sys.exit()
                if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
                    main()
        pygame.draw.rect(window, white, pygame.Rect(50, 100, 400, 100))
        pygame.draw.rect(window, white, pygame.Rect(50, 250, 400, 100))
        if 50 <= mouse[0] <= 450 and 250 <= mouse[1] <= 350:
            pygame.draw.rect(window, (242, 242, 242),
                             pygame.Rect(50, 250, 400, 100))
        window.blit(start_game, (120, 270))
        pygame.draw.rect(window, white, pygame.Rect(50, 400, 400, 100))
        if 50 <= mouse[0] <= 450 and 400 <= mouse[1] <= 500:
            pygame.draw.rect(window, (242, 242, 242),
                             pygame.Rect(50, 400, 400, 100))
        window.blit(quit_game, (155, 420))
        window.blit(font.render("Log In", True, pink), (100, 115))
        pygame.display.update()


def main():
    window.fill(white)
    for i in range(0, 5):
        for j in range(0, 6):
            pygame.draw.rect(window, grey, pygame.Rect(
                60 + (i*80), 50 + (j*80), 50, 50), 2)

    done = False

    game = MainRun()
    while not done:
        game.run_logic()
        game.process_events()
        game.display_frame()
        clock.tick(30)
        pygame.display.update()
    pygame.quit()


main_menu()
