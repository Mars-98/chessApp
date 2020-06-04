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

        loc_list = self.__add_up_left(y_up, x_mid_left, piece, loc_list, tiles)  # up left, Y + 3, X + 1
        loc_list = self.__add_up_right(y_up, x_mid_right, piece, loc_list, tiles)  # up right, Y + 3, X - 1
        loc_list = self.__add_down_left(y_down, x_mid_left, piece, loc_list, tiles)  # down left, Y - 3, X + 1
        loc_list = self.__add_down_right(y_down, x_mid_right, piece, loc_list, tiles)  # down right, Y - 3, X - 1

        loc_list = self.__add_left_up(y_mid_up, x_left, piece, loc_list, tiles)  # left up, Y + 1, X + 3
        loc_list = self.__add_left_down(y_mid_down, x_left, piece, loc_list, tiles)  # down right, Y - 1, X + 3
        loc_list = self.__add_right_up(y_mid_up, x_right, piece, loc_list, tiles)  # down right, Y + 1, X - 3
        loc_list = self.__add_right_down(y_mid_down, x_right, piece, loc_list, tiles)  # down right, Y - 1, X - 3

        return loc_list

    # up left, Y + 3, X + 1
    # Private helper method that is used in move_loc only
    # Takes in (y,x) coordinates or (column,row), as well as the piece, a location list, and tiles dictionary
    # Returns new loc_list, checks and adds locations to location list
    def __add_up_left(self, y_up, x_mid_left, piece, tiles, loc_list):
        if x_mid_left == range(0, 8) or y_up == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_up, x_mid_left))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_up, x_mid_left))
                else:
                    loc_list.append((y_up, x_mid_left))
        return loc_list

    # up right, Y + 3, X - 1
    def __add_up_right(self, y_up, x_mid_right, piece, tiles, loc_list):
        if x_mid_right == range(0, 8) or y_up == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_up, x_mid_right))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_up, x_mid_right))
                else:
                    loc_list.append((y_up, x_mid_right))
        return loc_list

    # down left, Y - 3, X + 1
    def __add_down_left(self, y_down, x_mid_left, piece, tiles, loc_list):
        if x_mid_left == range(0, 8) or y_down == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_down, x_mid_left))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_down, x_mid_left))
                else:
                    loc_list.append((y_down, x_mid_left))
        return loc_list

    # down right, Y - 3, X - 1
    def __add_down_right(self, y_down, x_mid_right, piece, tiles, loc_list):
        if x_mid_right == range(0, 8) or y_down == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_down, x_mid_right))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_down, x_mid_right))
                else:
                    loc_list.append((y_down, x_mid_right))
        return loc_list

    # left up, Y + 1, X + 3
    def __add_left_up(self, y_mid_up, x_left, piece, tiles, loc_list):
        if x_left == range(0, 8) or y_mid_up == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_mid_up, x_left))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_mid_up, x_left))
                else:
                    loc_list.append((y_mid_up, x_left))
        return loc_list

    # down right, Y - 1, X + 3
    def __add_left_down(self, y_mid_down, x_left, piece, tiles, loc_list):
        if x_left == range(0, 8) or y_mid_down == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_mid_down, x_left))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_mid_down, x_left))
                else:
                    loc_list.append((y_mid_down, x_left))
        return loc_list

    # down right, Y + 1, X - 3
    def __add_right_up(self, y_mid_up, x_right, piece, tiles, loc_list):
        if x_right == range(0, 8) or y_mid_up == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_mid_up, x_right))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_mid_up, x_right))
                else:
                    loc_list.append((y_mid_up, x_right))
        return loc_list

    # down right, Y - 1, X - 3
    def __add_right_down(self, y_mid_down, x_right, piece, tiles, loc_list):
        if x_right == range(0, 8) or y_mid_down == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_mid_down, x_right))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_mid_down, x_right))
                else:
                    loc_list.append((y_mid_down, x_right))
        return loc_list
