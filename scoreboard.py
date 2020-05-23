import pygame
from window import chessWindow


class chessScoreboard:
    pygame.init()

    def createscoreboard(window):
        pygame.draw.rect(chessWindow.window, (128, 128, 128), (1, 1, 100, 100))
    createscoreboard(window)