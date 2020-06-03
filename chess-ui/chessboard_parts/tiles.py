import pygame
from .tile import Tile

# Creates the Tiles of the chessboard
class Tiles:
    # 2d Map where each element is a Tile
    tile_map = None

    # Dictionary of the tiles as a key of the location tuple and a value of the tile object
    tile_dict = {}

    # All the initial tiles where the pieces will be placed
    pieces_on_tiles = None
    
    # Constructor for tiles that specifically makes all of the tiles that reside inside of tile map
    def __init__(self, window):
        color_black = False
        self.tile_map = pygame.sprite.Group()
        self.pieces_on_tiles = pygame.sprite.Group()
        for row in range(8):
            row_sprites = pygame.sprite.Group()
            for column in range(8):
                tile_square = Tile((0, 0, 0), (column, row), window) if color_black else Tile((255, 255, 255), (column, row), window)
                color_black = not color_black
                self.tile_dict[tile_square.parent_link] = tile_square
                row_sprites.add(tile_square)
            color_black = not color_black
            self.tile_map.add(row_sprites)
            if row < 2 or row > 5:
                self.pieces_on_tiles.add(row_sprites)

