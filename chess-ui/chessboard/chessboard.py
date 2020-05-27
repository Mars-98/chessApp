import pygame
from .tiles import Tiles

# Creates the chessboard
class Board:
    # A replicate of the 2d Tiles_Map
    tile_board = None

    # Constructor for chessboard of tiles and (later) pieces
    def __init__(self, window):
        self.tile_board = Tiles(window)


