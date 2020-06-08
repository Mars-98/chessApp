import pygame, sys
from scoreboard import chessScoreboard
from chessboard_parts.chessboard import Board

# creates window for chess
class ChessWindow:
    pygame.init()

    # function for creating window and calling other functions (e.i. scoreboard) inside the window
    # components are made in order, window must be first then scoreboard, etc.
    def createWindow(self):
        window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("chessApp")
        window.fill((128, 0, 0))
        scoreboard_display = chessScoreboard('player1', 'player2')
        scoreboard_display.createScoreboard(window)
        board = Board(window)
        tiles = board.tile_board.tile_map
        pieces = board.pieces.piece_map
        
        play_game = True
        clicked_once = False
        current_piece = None

        # Loop for creating and exiting the window
        while play_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play_game = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    # get a list of all sprites that are under the mouse cursor
                    clicked_tile = self.getTileSprite(pos, tiles)
                    clicked_piece = self.getPieceSprite(pos, pieces)
                    
                    if clicked_tile and clicked_piece:
                        column, row = clicked_tile.parent_link
                        # Current dummy values below until the api has the calls for each piece
                        potentential_moves = [(column, row + 1), (column + 1, row)]
                        if clicked_once and clicked_piece is current_piece:
                            for tile in tiles:
                                if tile.parent_link in potentential_moves:
                                    tile.newColor(window, tile.original_color)
                            clicked_once = False
                            current_piece = None

                        elif not clicked_once and current_piece is None:
                            for tile in tiles:
                                if tile.parent_link in potentential_moves:
                                    tile.newColor(window, (0, 0, 255))
                            clicked_once = True
                            current_piece = clicked_piece

            pygame.display.flip()

    def getTileSprite(self, position, tiles):
        for tile in tiles:
            if tile.rectangle.collidepoint(position):
                return tile
    
    def getPieceSprite(self, position, pieces):
        for piece in pieces:
            if piece.rectangle_placement.collidepoint(position):
                return piece
