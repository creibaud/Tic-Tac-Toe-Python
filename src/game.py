from src.grid import Grid
from src.panel import Panel
from src.line import Line
from src.restart import Restart

class Game:
    def __init__(self):
        self.grid = Grid()
        self.panel = Panel()
        self.line = Line()
        self.restart = Restart()
        self.player = "X"
        self.gameOver = False

    def handleMouseHover(self, pos):
        self.grid.handleMouseHover(pos, self.gameOver)
        if self.gameOver:
            self.restart.handleMouseHover(pos)

    def handleMouseClick(self, pos):
        if self.grid.handleMouseClick(pos, self.player, self.gameOver):
            self.isGameOver()
            self.player = "O" if self.player == "X" else "X"
            self.panel.update(self.player)
        if self.gameOver:
            if self.restart.handleMouseClick(pos):
                self.grid.restart()
                self.panel.restart()
                self.line.restart()
                self.player = "X"
                self.gameOver = False

    def isGameOver(self):
        winner = self.grid.checkWinner(self.player)
        if winner:
            self.panel.winner = self.player
            self.gameOver = True
        else:
            tie = self.grid.checkTie()
            if tie:
                self.panel.tie = True
                self.gameOver = True
    
    def draw(self, screen):
        self.panel.draw(screen)
        self.grid.draw(screen)
        if self.gameOver:
            self.line.draw(screen, self.grid.grid)
            self.restart.draw(screen)