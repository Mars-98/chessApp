from abc import ABC, abstractmethod


class Piece(ABC):
    totalPieces = 16

    def __init__(self, piece_move_cnt, piece_points, piece_color, piece_curr_loc, piece_first_move):
        self.move_count = piece_move_cnt
        self.points = piece_points
        self.color = piece_color
        self.curr_loc = piece_curr_loc
        self.first_move = piece_first_move

    def __del__(self, piece_move_cnt, piece_points, piece_color, piece_curr_loc):
        del piece_move_cnt
        del piece_points
        del piece_color
        del piece_curr_loc

    @abstractmethod
    def move_loc(self, location, type, player):
        # player can only move when it his/her turn first checks if king is in check:
        # each piece has its own movement rules cannot move through its own piece(except for the knight)
        pass

    def capture(self, enemy_piece):
        if not self.color == enemy_piece.color:
            self.curr_loc = enemy_piece.curr_loc
            enemy_piece.curr_loc = None
            self.totalPieces -= 1

        return  self.totalPieces
