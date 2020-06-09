import pygame, unittest,sys
from .king import King
sys.path.append('../chessboard_parts/')
from .tiles import Tiles

# import sys
# sys.path.append('../../chess-ui')
# from chessboard_parts.tiles import Tiles
# from window import ChessWindow
# import pygame

class Test_King(unittest.TestCase):
    def setUp(self):
        window = pygame.display.set_mode((0, 0))
        self.tile_board = Tiles(window)
    #     print(tile_board.tile_dict)

        self.wking = King(0,10, 'White', (3,0), False)


class Test_King_move(Test_King):
    def test_King_move_right(self):
        self.tile_board.update((3,0), 'King')
        self.assertEquals(self.wking.move_loc((3,0), King, self.tile_board), [(3,1),(4,0), (2,0), (4,1), (2,1)])
        self.tile_board.update((3,0), None)
        self.tile_board.update((2,0), 'King')
        self.assertEquals(self.wking.move_loc((2,0), King, self.tile_board), [(2,1),(3,0), (1,0), (3,1), (1,1)])
        self.tile_board.update((2,0), None)
        self.tile_board.update((1,0), 'King')
        self.assertEquals(self.wking.move_loc((1,0), King, self.tile_board), [(1,1),(2,0), (0,0), (2,1), (0,1)])
        self.tile_board.update((1,0), None)
        self.tile_board.update((0,0), 'King')
        self.assertEquals(self.wking.move_loc((0,0), King, self.tile_board), [(0,1), (1,0), (1,1)])

    def test_King_move_left(self):
        self.tile_board.update((5,0), )
        self.assertEquals(self.wking.move_loc((5,0), King, self.tile_board), [(5,1),(6,0), (4,0), (6,1), (4,1)])
        self.tile_board.update((5,0), None)
        self.tile_board.update((6,0), 'King')
        self.assertEquals(self.wking.move_loc((6,0), King, self.tile_board), [(6,1),(7,0), (5,0), (7,1), (5,1)])
        self.tile_board.update((6,0), None)
        self.tile_board.update((7,0), 'King')
        self.assertEquals(self.wking.move_loc((7,0), King, self.tile_board), [(7,1), (6,0), (6,1)])
    
    def test_King_move_diagonal(self):
        self.tile_board.update((3,3), 'King')
        self.assertEquals(self.wking.move_loc((3,3), King, self.tile_board), [(3,4),(3,2), (4,3), (2,3), (4,4), (2,4), (4,2), (2,2)])
        self.tile_board.update((3,3), None)
        self.tile_board.update((2,2), 'King')
        self.assertEquals(self.wking.move_loc((2,2), King, self.tile_board), [(2,3),(2,1), (3,2), (1,2), (3,3), (1,3), (3,1), (1,1)])
        self.tile_board.update((2,2), None)
        self.tile_board.update((1,3), 'King')
        self.assertEquals(self.wking.move_loc((1,3), King, self.tile_board), [(1,4),(1,2),(2,3), (0,3), (2,4), (0,4), (2,2), (0,2)])
        self.tile_board.update((1,3), None)
        self.tile_board.update((0,4), 'King')
        self.assertEquals(self.wking.move_loc((0,4), King, self.tile_board), [(4,1), (1,2), (2,3), (3,0), (2,4), (4,0), (2,2), (0,0)])