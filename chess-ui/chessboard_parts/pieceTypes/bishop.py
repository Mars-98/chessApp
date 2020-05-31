import pygame
from pygame.sprite import Sprite
import os

# Class representing the bishop piece
class Bishop(Sprite):
    # Where the bishop is on the board using tile locations
    placement = (0, 0)

    # Whether the bishop is black or white
    color_black = True

    # Bishop image size
    piece_size = None

    # Bishop image location
    image = None

    # Tile size used to convert piece location and size to pixels
    tile_size = None

    # Board size used to convert piece location and size to pixels
    board_size = None

    # Initially makes the bishop
    def __init__(self, window, column, tile_size, board_size, color_black):
        pygame.sprite.Sprite.__init__(self)
        self.color_black = color_black
        self.piece_size = pygame.display.get_surface().get_height()/18
        self.tile_size = tile_size
        self.board_size = board_size
        if color_black:
            row = 0
            script_dir = os.path.dirname(__file__)
            rel_path = "../bit_pieces/chess_piece_2_black_bishop.bmp"
        else:
            row = 7
            script_dir = os.path.dirname(__file__)
            rel_path = "../bit_pieces/chess_piece_2_white_bishop.bmp"
        self.image = pygame.image.load(os.path.join(script_dir, rel_path))
        self.image = pygame.transform.scale(self.image, (int(self.piece_size), int(self.piece_size)))
        self.piecePlacement(window, column, row)

    # Used for placing and moving a bishop to a specific pixel place
    def piecePlacement(self, window, column, row):
        window.blit(self.image, (self.board_size-column*self.tile_size, self.board_size-row*self.tile_size))
        self.placement = (column, row)