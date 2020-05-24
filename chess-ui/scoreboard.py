import pygame

# creates scoreboard for chess window
class chessScoreboard:

    # function for creating the scoreboard rect: (window, (color RGB), ((placement x, y), (width, height)))
    def createscoreboard(window):
        pygame.draw.rect(window, (128, 128, 128), ((430, 10), (150, 90)))
    # createscoreboard(window)