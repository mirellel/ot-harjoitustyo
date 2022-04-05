
import pygame, random, sys
from pygame.locals import *
from checkguess import CheckGuess
from settings import *

pygame.init()

checkguess = CheckGuess()

def main():
    

    height = 600
    width = 500

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    window.fill(white)

    file = open("/home/mirelle/ot-harjoitustyö/src/wordlist.txt", "r")
    wordlist = [word.replace("\n", "") for word in file]
    word = wordlist[random.randint(0, 2000)].upper()

    text = pygame.font.SysFont("arial", 40)

    guess = ""
    curr_letter=0
    for i in range(0, 5):
        for j in range(0, 6):
            pygame.draw.rect(window, grey, pygame.Rect(60 + (i*80), 50 + (j*80), 50, 50), 2)
    pygame.display.set_caption("Word.py")

    time1 = 0
    time2 = 0

    turns = 0
    win = False
    lost = False
    incorrect_word = False
    wrong_num_of_letters = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # pelin lopussa voi poistua tai pelata uuden vuoron
            if win or lost:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

            else:
                if event.type == pygame.KEYDOWN:

                    # arvauksen pyyhkiminen
                    if event.key == pygame.K_BACKSPACE:
                        if guess:
                            guess = guess[:-1]
                            curr_letter-=1

                    #arvauksen tekeminen
                    elif event.key == pygame.K_RETURN:
                        #hyväksytään vain viisikirjaiminen arvaus
                        if len(guess) == 5:
                            print(guess.lower())
                            #tarkastetaan onko arvaus kelpaava sana
                            if guess.lower() in wordlist:
                                #kutsutaan checkguess luokkaa tarkastamaan arvaus
                                win = checkguess.check(turns, word, guess, window, font)
                                turns+=1
                                guess = ""
                                curr_letter = 0
                                window.fill(white, (0, 500, 500, 200))
                            else:
                                incorrect_word = True  # merkitsee kelpaamattoman sanan
                        else:
                            wrong_num_of_letters = True # merkitsee, jos sanassa on liian vähän kirjaimia
                    # arvaus ilmestyy ruutuihin
                    else:
                        if len(guess) < 5:
                            if event.unicode.isalpha():
                                guess += event.unicode.upper()
                                curr_letter+=1
                    window.fill(white, (0, 500, 500, 200))
        window.fill(white, (0, 500, 500, 400))
        renderGuess = font.render(guess, True, black)
        window.blit(renderGuess, (190, 530))

        # väärästä sanasta tulee ilmoitus kahdeksi sekunniksi
        if incorrect_word == True:
            time2=0
            wrong_num_of_letters = False
            text_surface = font.render("Not in word list!", True, red)
            window.blit(text_surface, (100, 3))
            time1+=1
            
        if wrong_num_of_letters == True:
            incorrect_word = False
            time1=0
            text_surface = font.render("Not enough letters!", True, red)
            window.blit(text_surface, (100, 0))
            time2+=1

        
        if time1 == 2*FPS:
            incorrect_word = False
            time1 = 0
            guess = ""
            pygame.draw.rect(window, white, pygame.Rect(50, 10, 600, 40))


        if time2 == 2*FPS:
            wrong_num_of_letters = False
            time2 = 0
            guess = ""
            pygame.draw.rect(window, white, pygame.Rect(50, 10, 600, 40))

        # voittoessa loppukommentti riippuu vuorojen määrästä
        if win == True:
            pygame.draw.rect(window, grey, pygame.Rect(60, 210, 371, 211))
            if turns == 1:
                window.blit(unbelievable,(90, 200))
                window.blit(play_again, (60, 300))
            if turns == 2:
                window.blit(splendid,(90, 200))
                window.blit(play_again, (60, 300))
            if turns == 3:
                window.blit(wow,(90, 200))
                window.blit(play_again, (60, 300))
            if turns == 4:
                window.blit(great,(90, 200))
                window.blit(play_again, (60, 300))
            if turns == 5:
                window.blit(good,(90, 200))
                window.blit(play_again, (60, 300))
            if turns == 6:
                window.blit(phew,(90, 200))
                window.blit(play_again, (60, 300))
        # jos kuudennella vuorolla ei tule vielä voittoa, pelaaja häviää
        if turns == 6 and win != True:
            lost = True
            pygame.draw.rect(window, grey, pygame.Rect(60, 210, 371, 211))
            window.blit(defeat, (90, 200))
            window.blit(play_again, (60, 300))

        pygame.display.update()
        clock.tick(FPS)
main()
    