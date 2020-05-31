import pygame
from pygame.sprite import Sprite
import os

# Class representing the pawn piece
class Pawn(Sprite):
    # Where the pawn is on the board using tile locations
    placement = (0, 0)

    # Whether the pawn is black or white
    color_black = True

    # Pawn image size
    piece_size = None

    # Pawn image location
    image = None

    # Tile size used to convert piece location and size to pixels
    tile_size = None

    # Board size used to convert piece location and size to pixels
    board_size = None

    # Initially makes the pawn
    def __init__(self, window, column, tile_size, board_size, color_black):
        pygame.sprite.Sprite.__init__(self)
        self.color_black = color_black
        self.piece_size = pygame.display.get_surface().get_height()/18
        self.tile_size = tile_size
        self.board_size = board_size
        if color_black:
            row = 1 
            script_dir = os.path.dirname(__file__)
            rel_path = "../bit_pieces/chess_piece_2_black_pawn.bmp"
        else:
            row = 6
            script_dir = os.path.dirname(__file__)
            rel_path = "../bit_pieces/chess_piece_2_white_pawn.bmp"
        self.image = pygame.image.load(os.path.join(script_dir, rel_path))
        self.image = pygame.transform.scale(self.image, (int(self.piece_size), int(self.piece_size)))
        self.piecePlacement(window, column, row)

    # Used for placing and moving a Pawn to a specific pixel place
    def piecePlacement(self, window, column, row):
        window.blit(self.image, (self.board_size-column*self.tile_size, self.board_size-row*self.tile_size))
        self.placement = (column, row)
        print(self.placement)