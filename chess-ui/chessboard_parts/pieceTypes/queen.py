import pygame
from pygame.sprite import Sprite
import os

# Class representing the queen piece
class Queen(Sprite):
    # Where the queen is on the board using tile locations
    placement = (0, 0)

    # Whether the queen is black or white
    color_black = True

    # Queen image size
    piece_size = None

    # Queen image location
    image = None

    # Tile size used to convert piece location and size to pixels
    tile_size = None

    # Board size used to convert piece location and size to pixels
    board_size = None

    # Where the piece's pixels exist in the ui
    rectangle_placement = None

    # Link to Tile the pawn is on top of
    tile_underneath = None
    
    # Initially makes the queen
    def __init__(self, window, column, tile_size, board_size, color_black, tile_links):
        pygame.sprite.Sprite.__init__(self)
        self.color_black = color_black
        self.piece_size = pygame.display.get_surface().get_height()/18
        self.tile_size = tile_size
        self.board_size = board_size
        
        if color_black:
            row = 0
            script_dir = os.path.dirname(__file__)
            rel_path = "../bit_pieces/chess_piece_2_black_queen.bmp"
        else:
            row = 7
            script_dir = os.path.dirname(__file__)
            rel_path = "../bit_pieces/chess_piece_2_white_queen.bmp"
        self.image = pygame.image.load(os.path.join(script_dir, rel_path))
        self.image = pygame.transform.scale(self.image, (int(self.piece_size), int(self.piece_size)))
        self.piecePlacement(window, column, row)

        for tile in tile_links:
            if (column, row) == tile.parent_link:
                tile.piece_here = self
                self.tile_underneath = tile

    # Used for placing and moving a queen to a specific pixel place
    def piecePlacement(self, window, column, row):
        self.rectangle_placement = window.blit(self.image, (self.board_size-column*self.tile_size, self.board_size-row*self.tile_size))
        self.placement = (column, row)

    def recreate(self, window):
        column, row  = self.placement
        self.rectangle_placement = window.blit(self.image, (self.board_size-column*self.tile_size, self.board_size-row*self.tile_size))
