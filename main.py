import pygame
from src.constants import *
from src.game import Game

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe Game")

pygame.display.set_icon(pygame.image.load("assets/images/icon.png"))

clock = pygame.time.Clock()

game = Game()

run = True
while run:
    mousePos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                game.handleMouseClick(mousePos)

    screen.fill(BG_COLOR)
    
    game.handleMouseHover(mousePos)
    game.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()