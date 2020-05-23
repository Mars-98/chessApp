import pygame, sys


class chessWindow:
    pygame.init()

    def createwindow():
        window = pygame.display.set_mode((800, 650))
        pygame.display.set_caption("chessApp")
        window.fill((128, 0, 0))

        play_game = True

        # Loop for creating and exiting the window
        while play_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play_game = False
            pygame.display.flip()


    if __name__ == "__main__":
        createwindow()