import pygame, sys
from scoreboard import chessScoreboard

# creates window for chess
class chessWindow:
    pygame.init()

    # function for creating window and calling other functions (e.i. scoreboard) inside the window
    # components are made in order, window must be first then scoreboard, etc.
    def createwindow():
        window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("chessApp")
        window.fill((128, 0, 0))
        chessScoreboard.createscoreboard(window)

        play_game = True

        # Loop for creating and exiting the window
        while play_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play_game = False
            pygame.display.flip()

# Currently what we are using as a 'main' function
if __name__ == "__main__":
    chessWindow.createwindow()