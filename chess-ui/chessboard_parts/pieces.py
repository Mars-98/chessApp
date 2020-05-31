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
    def __init__(self, window):
        self.piece_map = pygame.sprite.Group()
        self.__make_pieces(window, True)
        self.__make_pieces(window, False)

    def __make_pieces(self, window, color_black):
        colored_pieces = pygame.sprite.Group()
        for index in range(8):
            colored_pieces.add(Pawn(window, index, color_black))
        for index in range(2):
            colored_pieces.add(Rook(window, index, color_black))
            colored_pieces.add(Knight(window, index, color_black))
            colored_pieces.add(Bishop(window, index, color_black))
            colored_pieces.add(Queen(window, index, color_black))
            colored_pieces.add(King(window, index, color_black))
        self.piece_map.add(colored_pieces)