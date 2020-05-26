from parentPiece.piece import Piece


class Queen(Piece):
    def __init__(self, piece_move_cnt, piece_points, piece_color, piece_curr_loc):
        self.move_count = piece_move_cnt
        self.points = piece_points
        self.color = piece_color
        self.curr_loc = piece_curr_loc

    def move_loc(self):
        pass
