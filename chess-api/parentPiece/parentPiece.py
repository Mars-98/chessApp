from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, piece_move_cnt, piece_points, piece_color, piece_curr_loc):
        self.move_count = piece_move_cnt
        self.points = piece_points
        self.color = piece_color
        self.curr_loc = piece_curr_loc

    def __del__(self, piece_move_cnt, piece_points, piece_color, piece_crnt_loc):
        del piece_move_cnt
        del piece_points
        del piece_color
        del piece_crnt_loc

    @abstractmethod
    def move_loc(self, location, type, player):
        # player can only move when it his/her turn first checks if king is in check:
        # each piece has its own movement rules cannot move through its own piece(except for the knight)
        pass

    def move(self, new_loc, piece):
        piece.curr_loc = new_loc
        return

    def capture(self, my_piece, enemy_piece):
        if not my_piece.color == enemy_piece.color:
            my_piece.curr_loc = enemy_piece.curr_loc
            enemy_piece.curr_loc = None
        return
