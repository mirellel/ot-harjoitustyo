from settings import *
import pygame, random

class CheckGuess():
    def __init__(self):
        pass

    def check(self, turns, word, userQuess, window, font):
        renderlist = ["", "", "", "", ""]
        spacing = 0
        # arvauksen värit alussa
        guessColourCode = [grey, grey, grey, grey, grey]
        

        # tarkastaa, onko arvauksessa oikeita kirjaimia
        for i in range (0, 5):
            # oikea kirjain väärällä paikalla merkitään keltaisella
            if userQuess[i] in word:
                guessColourCode[i] = yellow
            # oikea kirjain oikealla paikalla merkitään vihreällä
            if userQuess[i] == word[i]:
                guessColourCode[i] = green

        list(userQuess)
        # piirtää ruudut
        for i in range(0, 5):
            renderlist[i] = font.render(userQuess[i], True, black)
            pygame.draw.rect(window, guessColourCode[i], pygame.Rect(60 + spacing, 50 + (turns*80), 50, 50))
            window.blit(renderlist[i], (70 + spacing, 50 + (turns*80)))
            spacing+=80
        # jos kaikki vihreää, voitto
        if guessColourCode == [green, green, green, green, green]:
            return True


        
    # Sama kuin ylempi, mutta muokattu testausta varten
    def test_check(self, word, userQuess):
        # arvauksen värit alussa
        guessColourCode = [grey, grey, grey, grey, grey]
        

        # tarkastaa, onko arvauksessa oikeita kirjaimia
        for i in range (0, 5):
            # oikea kirjain väärällä paikalla merkitään keltaisella
            if userQuess[i] in word:
                guessColourCode[i] = yellow
            # oikea kirjain oikealla paikalla merkitään vihreällä
            if userQuess[i] == word[i]:
                guessColourCode[i] = green

        list(userQuess)
        # jos kaikki vihreää, voitto
        return guessColourCode