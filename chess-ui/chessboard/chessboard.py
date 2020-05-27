import pygame
from .tiles import Tiles

class Board:
    tile_board = None

    def __init__(self, window):
        self.tile_board = Tiles(window)


