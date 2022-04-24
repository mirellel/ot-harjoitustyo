import pygame
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

defeat = largefont.render("You lost!", True, pink)
victory = largefont.render("You won!", True, pink)
play_again = largefont.render("Replay", True, pink)
quit_game = largefont.render("Quit", True, pink)
start_game = font.render("Start game", True, pink)
