import pygame
import unittest
from ..chessApp.chess-api.childPiece.pawn import Pawn
from ..chessApp.chess-ui.chessboard_parts.tiles import Tiles

# from window import ChessWindow
# import pygame

class Test_Pawn(unittest.TestCase):
    def setUp(self):
        window = pygame.display.set_mode((0, 0))
        self.tile_board = Tiles(window)
    #     print(tile_board.tile_dict)

        self.wpawn = Pawn(0,1, 'White', (1,1), False)


class Test_Pawn_move(Test_Pawn):
    def test_Pawn_move_right(self):

        # no impediments
        self.tile_board.update((1,1), 'Pawn')
        self.assertEquals(self.wpawn.move_loc((1,1), Pawn, self.tile_board), [(1,2),(1,3)])
        self.tile_board.update((1,1), None)
        self.tile_board.update((1,3), 'Pawn')
        self.assertEquals(self.wpawn.move_loc((1,3), Pawn, self.tile_board), [(1,4)])
        self.tile_board.update((1,3), None)
        self.tile_board.update((1,4), 'Pawn')
        self.assertEquals(self.wpawn.move_loc((1,4), Pawn, self.tile_board), [(1,5)])
        self.tile_board.update((1,4), None)
        self.tile_board.update((1,5), 'Pawn')
        self.assertEquals(self.wpawn.move_loc((1,5), Pawn, self.tile_board), [(1,6)])

        # limiting chess piece moves
        self.tile_board.update((3,1), 'Pawn')
        self.tile_board.update((3,3), "Knight")
        self.assertEquals(self.wpawn.move_loc((3,1), Pawn, self.tile_board), [(3,2)])

    def test_Pawn_no_move(self):
        self.tile_board.update((0,1), 'Pawn')
        self.tile_board.update((0,2), 'Bishop')
        self.tile_board.update((0,3), 'Knight')

        #no valid moves to make
        self.assertEquals(self.wpawn.move_loc((0,1), Pawn, self.tile_board), [] )

        

