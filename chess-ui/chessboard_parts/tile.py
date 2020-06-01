import pygame
from pygame.sprite import Sprite

# Each tile is made up of a color tuple, whether or not a piece is there,
# where they exist in the parent array, and a rectangle representing the tile. 
# 
class Tile(Sprite):
    # The current color of the tile. Consists of white: (0,0,0), black: (255,255,255) or blue: (0,0,255)
    color = (0,0,0)

    # Either (0,0,0) for white or (255,255,255) for black
    original_color = (0,0,0)

    # Whether or not there is a piece on top of it
    piece_here = None

    # Where it exists in the chessboard
    parent_link = (0,0)

    # Unmade pygame.rect()
    rectangle = None

    # Size of the tile
    tile_size = 0

    # Placement of the lower right corner of the board based on tile_size.
    # Starts with middle of window. I divide by 2.25 because of maths I guess.
    window_size = 0

    # Constructor of Tile
    def __init__(self, color, parent_link, window, piece_here=False):
        pygame.sprite.Sprite.__init__(self)
        self.color = self.original_color = color
        self.parent_link = parent_link
        self.piece_here = piece_here
        self.tile_size = pygame.display.get_surface().get_height()/17
        self.window_size = (pygame.display.get_surface().get_height()/2.25) + (self.tile_size*4)
        self.rectangle = self.__setRectangle(window)

    # A private method to set the rectangle
    def __setRectangle(self, window):
        length, width = self.parent_link
        return pygame.draw.rect(window, self.color, 
            ((self.window_size-length*self.tile_size, self.window_size-width*self.tile_size),(self.tile_size, self.tile_size)))

    def newColor(self, window, color):
        length, width = self.parent_link
        self.color = color
        self.rectangle = pygame.draw.rect(window, color, 
            ((self.window_size-length*self.tile_size, self.window_size-width*self.tile_size),(self.tile_size, self.tile_size)))
        self.__recreatePiece(window)
    
    def __recreatePiece(self, window):
        if self.piece_here:
            self.piece_here.recreate(window)
