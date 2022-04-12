import pygame
from pygame.locals import *  # pylint: disable=unused-wildcard-import, disable=wildcard-import
pygame.init()

# kaksi fonttikokoa
font = pygame.font.SysFont("Arial", 40)
largefont = pygame.font.SysFont("Arial", 60)

clock = pygame.time.Clock()
window = pygame.display.set_mode((500, 600))

# asetetaan muutama perusväri valmiiksi
white = (255, 255, 255)
black = (0, 0, 0)
green = (51, 212, 99)
yellow = (222, 224, 81)
grey = (127, 128, 122)
pink = (237, 140, 195)
red = (224, 13, 35)

unbelievable = largefont.render("Unbelievable!", True, pink)
splendid = largefont.render("Splendid!", True, pink)
wow = largefont.render("Wow!", True, pink)
great = largefont.render("Great!", True, pink)
good = largefont.render("Good!", True, pink)
phew = largefont.render("Phew!", True, pink)

defeat = largefont.render("You lost!", True, pink)
play_again = largefont.render("REPLAY", True, pink)
quit_game = largefont.render("QUIT", True, pink)
start_game = font.render("START GAME", True, pink)
