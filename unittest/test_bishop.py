import pygame, unittest,sys
from ..childPiece.bishop import Bishop
# from ..childPiece.Bishop import Bishop

# import sys
sys.path.append('../../chess-ui')
from .chessboard_parts.tiles import Tiles
# from window import ChessWindow
# import pygame

class test_bishop(unittest.TestCase):
    def setUp(self):
        window = pygame.display.set_mode((0, 0))
        self.tile_board = Tiles(window)
    #     print(tile_board.tile_dict)

        self.wbishop = Bishop(0, 3, 'White', (0,1), False)


class test_bishop_move(test_bishop):
    def test_bishop_move(self):
        # all other spaces are open
        self.tile_board.update((0,0), 'Bishop')
        self.assertEquals(self.wbishop.move_loc((0,0), Bishop, self.tile_board), [(1,1),(2,2), (3,3), (4,4), (5,5), (6,6), (7,7)])
        self.tile_board.update((0,0), None)
        self.tile_board.update((4,4), 'Bishop')
        self.assertEquals(self.wbishop.move_loc((4,4), Bishop, self.tile_board), [(5,3),(6,4), (7,2), (5,5), (6,6), (7,7), (3,3), 
                                                                                  (2,2), (1,1), (0,0), (5,3), (6,2), (7,1)])
        self.tile_board.update((4,4), None)
        self.tile_board.update((7,1), 'Bishop')
        self.assertEquals(self.wbishop.move_loc((7,1), Bishop, self.tile_board), [(6,2),(5,3), (4,4), (3,5), (2,6), (1,7), (6,0) ])
        self.tile_board.update((7,1), None)
        self.tile_board.update((6,0), 'Bishop')
        self.assertEquals(self.wbishop.move_loc((6,0), Bishop, self.tile_board), [(5,1), (4,2), (3,3), (2,4), (1,5), (0,6), (7,1)])

    def test_bishop_no_move(self):
        self.tile_board.update((0,0), 'Bishop')
        self.tile_board.update((2,2), 'King')
        self.assertEquals(self.wbishop.move_loc((0,0), Bishop, self.tile_board), [(1,1)])
        self.tile_board.update((0,0), None)
        self.tile_board.update((1,1), 'Bishop')
        self.assertEquals(self.wbishop.move_loc((1,1), Bishop, self.tile_board), [(0,2), (1,1), (0,0)]