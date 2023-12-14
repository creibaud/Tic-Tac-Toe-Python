import pygame
from src.constants import *

class Restart:
    def __init__(self):
        self.font = pygame.font.Font("assets/fonts/Roboto/Roboto-Medium.ttf", 40)
        self.rect = pygame.Rect(0, 0, 200, 120)
        self.rect.center = (SCREEN_WIDTH / 2, 735)
        self.content = self.font.render("Restart", True, RESTART_TEXT)
        self.color = RESTART_BG

    def handleMouseHover(self, pos):
        if self.rect.collidepoint(pos):
            self.color = RESTART_BG_HOVER
        else:
            self.color = RESTART_BG

    def handleMouseClick(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius = 10)
        screen.blit(self.content, (self.rect.centerx - self.content.get_width() / 2, self.rect.centery - self.content.get_height() / 2))