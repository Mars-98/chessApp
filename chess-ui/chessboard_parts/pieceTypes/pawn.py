import pygame
from pygame.sprite import Sprite
import os

class Pawn(Sprite):
    placement = (0,0)
    color_black = True
    piece_size = None

    def __init__(self, window, placement, color_black):
        pygame.sprite.Sprite.__init__(self)
        self.placement = placement
        self.color_black = color_black
        self.piece_size = pygame.display.get_surface().get_height()/14 # This division probably works or equivalent integer @Connor
        if color_black:
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "../bit_pieces/chess_piece_2_black_pawn.bmp"
            os.path.join(script_dir, rel_path)
        else:
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "../bit_pieces/chess_piece_2_white_pawn.bmp"
            os.path.join(script_dir, rel_path)