import pygame
from .pieceTypes.pawn import Pawn
from .pieceTypes.rook import Rook
from .pieceTypes.knight import Knight
from .pieceTypes.bishop import Bishop
from .pieceTypes.queen import Queen
from .pieceTypes.king import King

# Creates the Pieces of the chessboard
class Pieces:
    # 2d Map where each element is a Tile
    piece_map = None
    
    # Constructor for tiles that specifically makes all of the tiles that reside inside of tile map
    def __init__(self, window, tile_size, board_size):
        self.piece_map = pygame.sprite.Group()
        self.__make_pieces(window, tile_size, board_size, True)
        self.__make_pieces(window, tile_size, board_size, False)

    # Private method to initially make the pieces
    def __make_pieces(self, window, tile_size, board_size, color_black):
        colored_pieces = pygame.sprite.Group()
        for index in range(8):
            colored_pieces.add(Pawn(window, index, tile_size, board_size, color_black))
        colored_pieces.add(Rook(window, 0, tile_size, board_size, color_black))
        colored_pieces.add(Knight(window, 1, tile_size, board_size, color_black))
        colored_pieces.add(Bishop(window, 2, tile_size, board_size, color_black))
        if color_black:
            colored_pieces.add(Queen(window, 3, tile_size, board_size, color_black))
            colored_pieces.add(King(window, 4, tile_size, board_size, color_black))
        else:
            colored_pieces.add(King(window, 3, tile_size, board_size, color_black))
            colored_pieces.add(Queen(window, 4, tile_size, board_size, color_black))
        colored_pieces.add(Bishop(window, 5, tile_size, board_size, color_black))
        colored_pieces.add(Knight(window, 6, tile_size, board_size, color_black))
        colored_pieces.add(Rook(window, 7, tile_size, board_size, color_black))
        self.piece_map.add(colored_pieces)