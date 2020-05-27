import pygame
from .tile import Tile

# Creates the Tiles of the chessboard
class Tiles:
    # 2d Map where each element is a Tile
    tile_map = None
    
    # Constructor for tiles that specifically makes all of the tiles that reside inside of tile map
    def __init__(self, window):
        color_black = False
        self.tile_map = pygame.sprite.Group()
        for length in range(8):
            row_sprites = pygame.sprite.Group()
            for width in range(8):
                tile_square = Tile((0,0,0), (length,width), window) if color_black else Tile((255, 255, 255), (length,width), window)
                color_black = not color_black
                row_sprites.add(tile_square)
            color_black = not color_black
            self.tile_map.add(row_sprites)

