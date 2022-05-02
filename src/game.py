
import random
import sys
import pygame
from checkguess import CheckGuess
from settings import green, white, font, black, red, window, grey
pygame.init()

checkguess = CheckGuess()


class MainRun():
    def __init__(self):
        self.time1 = 0
        self.time2 = 0
        self.turns = 0
        self.guess = ""
        self.win = False
        self.lost = False
        self.incorrect_word = False
        self.wrong_num_of_letters = False
        with open("wordlist.txt", encoding="utf-8") as file:
            self.wordlist = [word.replace("\n", "") for word in file]
        self.word = self.wordlist[random.randint(0, 2000)].upper()
        self.win_list = [green, green, green, green, green]
        window.fill(white)
        for i in range(0, 5):
            for j in range(0, 6):
                pygame.draw.rect(window, grey, pygame.Rect(
                    60 + (i*80), 50 + (j*80), 50, 50), 2)

    def check_win(self):
        if checkguess.check(self.word, self.guess) == self.win_list:
            self.win = True

    def check_guess(self):
        spacing = 0
        for j in range(0, 5):
            checkguess.renderlist[j] = font.render(
                self.guess[j], True, black)
            pygame.draw.rect(window, checkguess.guesscolourcode[j],
                             pygame.Rect(
                60 + spacing, 50 + (self.turns*80), 50, 50))
            window.blit(
                checkguess.renderlist[j], (70 + spacing,
                                           50 + (self.turns*80)))
            spacing += 80
        self.turns += 1
        self.guess = ""
        window.fill(white, (0, 500, 500, 200))

    def process_events(self):
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
                    # arvauksen tekeminen enteriä painamalla
                    elif event.key == pygame.K_RETURN:
                        # hyväksytään vain viisikirjaiminen arvaus
                        if len(self.guess) == 5:
                            print(self.guess.lower())
                            # tarkastetaan onko arvaus kelpaava sana
                            if self.guess.lower() in self.wordlist:
                                # kutsutaan checkguess luokkaa tarkastamaan arvaus
                                self.check_win()
                                self.check_guess()
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

    def not_in_list(self):
        if self.incorrect_word is True:
            self.time2 = 0
            self.wrong_num_of_letters = False
            text_surface = font.render("Not in word list!", True, red)
            window.blit(text_surface, (105, 3))
            self.time1 += 1
        if self.time1 == 60:
            self.incorrect_word = False
            self.time1 = 0
            self.guess = ""
            pygame.draw.rect(window, white, pygame.Rect(50, 10, 600, 40))

    def too_short(self):
        if self.wrong_num_of_letters is True:
            self.incorrect_word = False
            self.time1 = 0
            text_surface = font.render("Not enough letters!", True, red)
            window.blit(text_surface, (105, 0))
            self.time2 += 1

        if self.time2 == 60:
            self.wrong_num_of_letters = False
            self.time2 = 0
            self.guess = ""
            pygame.draw.rect(window, white, pygame.Rect(50, 0, 600, 40))
            pygame.draw.rect(window, white, pygame.Rect(265, 35, 28, 10))

    def display_frame(self):
        if self.guess:
            letterspacing = 0
            for i in range(len(self.guess)):  # pylint: disable=consider-using-enumerate
                word_surface = font.render(self.guess[i], True, black)
                window.blit(word_surface, (180+letterspacing, 530))
                letterspacing += 30
        if self.turns == 6 and not self.win:
            self.lost = True
