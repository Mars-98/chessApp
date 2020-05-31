import pygame
from .tiles import Tiles
from .pieces import Pieces

# Creates the chessboard
class Board:
    # A replicate of the 2d Tiles_Map
    tile_board = None
    pieces = None

    # Constructor for chessboard of tiles and (later) pieces
    def __init__(self, window):
        self.tile_board = Tiles(window)
        self.pieces = Pieces(window, 
            self.tile_board.tile_map.sprites()[0].tile_size, self.tile_board.tile_map.sprites()[0].window_size)


