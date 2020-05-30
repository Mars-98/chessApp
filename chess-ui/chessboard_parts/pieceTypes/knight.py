import pygame
from pygame.sprite import Sprite
import os

class Knight(Sprite):
    placement = (0, 0)
    color_black = True
    piece_size = None

    def __init__(self, window, placement, color_black):
        pygame.sprite.Sprite.__init__(self)
        self.color_black = color_black
        self.piece_size = pygame.display.get_surface().get_height()/14
        if color_black:
            self.placement = (0, placement) 
            script_dir = os.path.dirname(__file__)
            rel_path = "../bit_pieces/chess_piece_2_black_knight.bmp"
            os.path.join(script_dir, rel_path)
        else:
            self.placement = (7, placement) 
            script_dir = os.path.dirname(__file__)
            rel_path = "../bit_pieces/chess_piece_2_white_knight.bmp"
            os.path.join(script_dir, rel_path)