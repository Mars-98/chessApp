import pygame, sys
from scoreboard import chessScoreboard
from chessboard_parts.chessboard import Board

# creates window for chess
class ChessWindow:
    pygame.init()

    # function for creating window and calling other functions (e.i. scoreboard) inside the window
    # components are made in order, window must be first then scoreboard, etc.
    def createWindow():
        window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("chessApp")
        window.fill((128, 0, 0))
        scoreboard_display = chessScoreboard('player1', 'player2')
        scoreboard_display.createScoreboard(window)
        board = Board(window)
        tiles = board.tile_board.tile_map

        play_game = True

        # Loop for creating and exiting the window
        while play_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play_game = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    # get a list of all sprites that are under the mouse cursor
                    clicked_tiles = [tile for tile in tiles if tile.rectangle.collidepoint(pos)]
                    for sprite in clicked_tiles:
                        print(sprite.parent_link)
                        pass
                        # TEMPORARY: Here we will later make check for what tile the player is choosing it.
                        # The tile of the sprite is save in parent_link.
                        # Refer to the ChessboardIndexing.png in the design_ui folder

                    # LATER: This is where we will check the type of the piece to see which one it is.
                    # We can check this via checking the type of a Sprite.
                    # This will be done when the parent Piece class and its respective children are made.
                    
            pygame.display.flip()
