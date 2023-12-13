import pygame
from src.constants import *

class Line:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.color = PANEL_BG_END

    def checkHowVictory(self, grid):
        for i in range(0, ROWS):
            if grid[i][0] == grid[i][1] and grid[i][0] == grid[i][2] and grid[i][0] != "":
                self.x1 = MARGIN_LEFT + CELL_SPACE_BETWEEN + 20
                self.y1 = CELL_SIZE * i + MARGIN_TOP + CELL_SIZE / 2
                self.x2 = CELL_SIZE * 3 + MARGIN_LEFT - CELL_SPACE_BETWEEN - 20
                self.y2 = self.y1
                return True
                
        for i in range(0, COLS):
            if grid[0][i] == grid[1][i] and grid[0][i] == grid[2][i] and grid[0][i] != "":
                self.x1 = CELL_SIZE * i + MARGIN_LEFT + CELL_SIZE / 2
                self.y1 = MARGIN_TOP + CELL_SPACE_BETWEEN + 20
                self.x2 = self.x1
                self.y2 = CELL_SIZE * 3 + MARGIN_TOP - CELL_SPACE_BETWEEN - 20
                return True
                
        if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0] != "":
            self.x1 = MARGIN_LEFT + CELL_SPACE_BETWEEN + 20
            self.y1 = MARGIN_TOP + CELL_SPACE_BETWEEN + 15
            self.x2 = CELL_SIZE * 3 + MARGIN_LEFT - CELL_SPACE_BETWEEN - 20
            self.y2 = CELL_SIZE * 3 + MARGIN_TOP - CELL_SPACE_BETWEEN - 15
            return True
        
        if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0] and grid[0][2] != "":
            self.x1 = MARGIN_LEFT + CELL_SPACE_BETWEEN + 20
            self.y1 = CELL_SIZE * 3 + MARGIN_TOP - CELL_SPACE_BETWEEN - 15
            self.x2 = CELL_SIZE * 3 + MARGIN_LEFT - CELL_SPACE_BETWEEN - 20
            self.y2 = MARGIN_TOP + CELL_SPACE_BETWEEN + 15
            return True

        return False
    
    def restart(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
    
    def draw(self, screen, grid):
        if self.checkHowVictory(grid):
            pygame.draw.lines(screen, self.color, True, [(self.x1, self.y1), (self.x2, self.y2)], 10)