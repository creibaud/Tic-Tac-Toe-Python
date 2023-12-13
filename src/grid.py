import pygame
from src.constants import *
from src.cell import Cell

class Grid:
    def __init__(self):
        self.grid = self.initGrid()
        self.cells = self.initCells()

    def initGrid(self):
        grid = []
        for i in range(0, ROWS):
            grid.append([])
            for j in range(0, COLS):
                grid[i].append("")
        return grid

    def initCells(self):
        cells = []
        for i in range(0, ROWS):
            cells.append([])
            for j in range(0, COLS):
                cells[i].append(Cell(i, j, self.grid[i][j]))
        return cells
    
    def restart(self):
        self.grid = self.initGrid()
        self.cells = self.initCells()
    
    def handleMouseHover(self, pos, gameOver):
        for i in range(0, ROWS):
            for j in range(0, COLS):
                if self.cells[i][j].rect.collidepoint(pos) and self.grid[i][j] == "" and not gameOver:
                    self.cells[i][j].color = CELL_BG_HOVER
                else:
                    self.cells[i][j].color = CELL_BG

    def handleMouseClick(self, pos, player, gameOver):
        for i in range(0, ROWS):
            for j in range(0, COLS):
                if self.cells[i][j].rect.collidepoint(pos) and self.grid[i][j] == "" and not gameOver:
                    self.grid[i][j] = player
                    self.cells[i][j].content = player
                    return True
        return False
    
    def checkWinner(self, player):
        for i in range(0, ROWS):
            if self.grid[i][0] == self.grid[i][1] and self.grid[i][0] == self.grid[i][2] and self.grid[i][0] == player:
                return True
                
        for i in range(0, COLS):
            if self.grid[0][i] == self.grid[1][i] and self.grid[0][i] == self.grid[2][i] and self.grid[0][i] == player:
                return True
                
        if self.grid[0][0] == self.grid[1][1] and self.grid[0][0] == self.grid[2][2] and self.grid[0][0] == player:
            return True
        
        if self.grid[0][2] == self.grid[1][1] and self.grid[0][2] == self.grid[2][0] and self.grid[0][2] == player:
            return True

        return False
    
    def checkTie(self):
        for i in range(0, ROWS):
            for j in range(0, COLS):
                if self.grid[i][j] == "":
                    return False
        return True
    
    def draw(self, screen):
        for i in range(0, ROWS):
            for j in range(0, COLS):
                self.cells[i][j].draw(screen)