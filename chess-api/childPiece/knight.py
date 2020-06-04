from ..parentPiece.piece import Piece


# This is the child class Knight, that inherits from the parent class piece
# Knight uses the methods provided in piece, and writes the abstract method move_loc
class Knight(Piece):
    def __init__(self, piece_move_cnt, piece_points, piece_color, piece_curr_loc):
        super().__init__(piece_move_cnt, piece_points, piece_color, piece_curr_loc)

    def move_loc(self, location, piece, tiles):
        loc_list = []

        y_up = location[0] + 3
        y_down = location[0] - 3
        x_mid_left = location[1] + 1
        x_mid_right = location[1] - 1
        x_left = location[1] + 3
        x_right = location[1] - 3
        y_mid_up = location[0] + 1
        y_mid_down = location[0] - 1

        loc_list = self.__add_loc(y_up, x_mid_left, piece, loc_list, tiles)  # up left, Y + 3, X + 1
        loc_list = self.__add_loc(y_up, x_mid_right, piece, loc_list, tiles)  # up right, Y + 3, X - 1
        loc_list = self.__add_loc(y_down, x_mid_left, piece, loc_list, tiles)  # down left, Y - 3, X + 1
        loc_list = self.__add_loc(y_down, x_mid_right, piece, loc_list, tiles)  # down right, Y - 3, X - 1

        loc_list = self.__add_loc(y_mid_up, x_left, piece, loc_list, tiles)  # left up, Y + 1, X + 3
        loc_list = self.__add_loc(y_mid_down, x_left, piece, loc_list, tiles)  # down right, Y - 1, X + 3
        loc_list = self.__add_loc(y_mid_up, x_right, piece, loc_list, tiles)  # down right, Y + 1, X - 3
        loc_list = self.__add_loc(y_mid_down, x_right, piece, loc_list, tiles)  # down right, Y - 1, X - 3

        return loc_list

    # Private helper method that is used in move_loc only
    # Takes in (y,x) coordinates or (column,row), as well as the piece, a location list, and tiles dictionary
    # Returns new loc_list, checks and adds locations to location list
    def __add_loc(self, y, x, piece, tiles, loc_list):
        if x == range(0, 8) or y == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y, x))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y, x))
                else:
                    loc_list.append((y, x))
        return loc_list
