from ..parentPiece.piece import Piece


# This is the child class Pawn, that inherits from the parent class piece
# Pawn uses the methods provided in piece, and writes the abstract method move_loc
class Pawn(Piece):
    def __init__(self, piece_move_cnt, piece_points, piece_color, piece_curr_loc, piece_first_move=False):
        self.first_move = piece_first_move
        super().__init__(piece_move_cnt, piece_points, piece_color, piece_curr_loc)

    def move_loc(self, location, piece, tiles):
        loc_list = []

        y_1 = location[0] + 1
        y_2 = location[0] + 2
        x_left = location[1] + 1
        x_right = location[1] - 1
        x = location[1]

        loc_list = self.__add_loc_diag(y_1, x_left, piece, loc_list, tiles)  # Diagonal left
        loc_list = self.__add_loc_diag(y_1, x_right, piece, loc_list, tiles)  # Diagonal right

        if not piece.first_move:
            loc_list = self.__add_loc_up(y_2, x, loc_list, tiles)  # Up 2 only on first move

        loc_list = self.__add_loc_up(y_1, x, loc_list, tiles)  # UP 1


        return loc_list

    # Private helper method that is used in move_loc only
    # Takes in (y,x) coordinates or (column,row), as well as the piece, a location list, and a single tile
    # Returns new loc_list, checks and adds locations to location list
    def __add_loc_up(self, y, x, loc_list, tiles):
        if x == range(0, 8) or y == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y, x))
            if tile:
                if not tile.piece_here:
                    loc_list.append((y, x))
        return loc_list

    def __add_loc_diag(self, y, x, piece, tiles, loc_list):
        if x == range(0, 8) or y == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y, x))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y, x))
        return loc_list

    def en_passant(self):
        pass

    def promotion(self):
        pass
