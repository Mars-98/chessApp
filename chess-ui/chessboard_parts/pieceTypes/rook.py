import pygame
from pygame.sprite import Sprite

class Rook(Sprite):
    placement = (0,0)
    color_black = True
    piece_size = None

    def __init__(self, window, placement, color_black):
        pygame.sprite.Sprite.__init__(self)
        self.placement = placement
        self.color_black = color_black
        self.piece_size = pygame.display.get_surface().get_height()/14
        if color_black:
            pygame.image.load("/Users/Connor/Downloads/bit_pieces/chess_piece_2_black_rook.bmp")
        else:
            pygame.image.load("/Users/Connor/Downloads/bit_pieces/chess_piece_2_white_rook.bmp")