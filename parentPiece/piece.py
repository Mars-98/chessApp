from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, piece_move_cnt, piece_points, piece_color, piece_crnt_loc):
        self.move_count = piece_move_cnt
        self.points = piece_points
        self.color = piece_color
        self.curr_loc = piece_crnt_loc

    def __del__(self):
        pass

    @abstractmethod
    def move_loc(self):
        # player can only move when it his/her turn first checks if king is in check:
        # each piece has its own movement rules cannot move through its own piece(except for the knight)
        pass

    def move(self):
        pass

    def capture(self):
        pass
