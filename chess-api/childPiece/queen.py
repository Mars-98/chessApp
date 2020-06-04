from ..parentPiece.piece import Piece


# This is the child class Queen, that inherits from the parent class piece
# Queen uses the methods provided in piece, and writes the abstract method move_loc
class Queen(Piece):
    def __init__(self, piece_move_cnt, piece_points, piece_color, piece_curr_loc):
        super().__init__(piece_move_cnt, piece_points, piece_color, piece_curr_loc)

    def move_loc(self, location, piece, tiles):
        loc_list = []

        y_up = location[0] + 1
        y_down = location[0] - 1
        x_left = location[1] + 1
        x_right = location[1] - 1
        y = location[0]
        x = location[1]

        loc_list = self.__add_diag_right(y_up, x_right, piece, loc_list,
                                         tiles)  # Diagonal positive right: Y + 1, X - 1
        loc_list = self.__add_diag_left(y_up, x_left, piece, loc_list,
                                        tiles)  # Diagonal positive left: Y + 1, X + 1
        loc_list = self.__add_negDiag_right(y_down, x_right, piece, loc_list,
                                            tiles)  # Diagonal negative right: Y - 1, X - 1
        loc_list = self.__add_negDiag_left(y_down, x_left, piece, loc_list,
                                           tiles)  # Diagonal negative left: Y - 1, X + 1

        loc_list = self.__add_up(y_up, x, piece, loc_list, tiles)  # Vertical up: Y + 1, X
        loc_list = self.__add_down(y_down, x, piece, loc_list, tiles)  # Vertical down: Y - 1, X
        loc_list = self.__add_left(y, x_left, piece, loc_list, tiles)  # Horizontal left: Y, X + 1
        loc_list = self.__add_right(y, x_right, piece, loc_list, tiles)  # Horizontal right: Y, X - 1

        return loc_list

    # Diagonal positive right: Y + 1, X - 1
    # Private helper method that is used in move_loc only
    # Takes in (y,x) coordinates or (column,row), as well as the piece, a location list, and tiles dictionary
    # Returns new loc_list, checks and adds locations to location list
    def __add_diag_right(self, x_right, y_up, piece, tiles, loc_list):
        while x_right == range(0, 8) or y_up == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_up, x_right))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_up, x_right))
                else:
                    loc_list.append((y_up, x_right))
            x_right -= 1
            y_up += 1
        return loc_list

    # Diagonal positive left: Y + 1, X + 1
    def __add_diag_left(self, x_left, y_up, piece, tiles, loc_list):
        while x_left == range(0, 8) or y_up == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_up, x_left))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_up, x_left))
                else:
                    loc_list.append((y_up, x_left))
            x_left += 1
            y_up += 1
        return loc_list

    # Diagonal negative right: Y - 1, X - 1
    def __add_negDiag_right(self, x_right, y_down, piece, tiles, loc_list):
        while x_right == range(0, 8) or y_down == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_down, x_right))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_down, x_right))
                else:
                    loc_list.append((y_down, x_right))
            x_right -= 1
            y_down -= 1
        return loc_list

    # Diagonal negative left: Y - 1, X + 1
    def __add_negDiag_left(self, x_left, y_down, piece, tiles, loc_list):
        while x_left == range(0, 8) or y_down == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_down, x_left))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_down, x_left))
                else:
                    loc_list.append((y_down, x_left))
            x_left += 1
            y_down -= 1
        return loc_list

    # Vertical up: Y + 1, X
    def __add_up(self, x, y_up, piece, tiles, loc_list):
        while x == range(0, 8) or y_up == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_up, x))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_up, x))
                else:
                    loc_list.append((y_up, x))
            y_up += 1
        return loc_list

    # Vertical down: Y - 1, X
    def __add_down(self, x, y_down, piece, tiles, loc_list):
        while x == range(0, 8) or y_down == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_down, x))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_down, x))
                else:
                    loc_list.append((y_down, x))
            y_down -= 1
        return loc_list

    # Horizontal left: Y, X + 1
    def __add_left(self, x_left, y, piece, tiles, loc_list):
        while x_left == range(0, 8) or y == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y, x_left))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y, x_left))
                else:
                    loc_list.append((y, x_left))
            x_left += 1
        return loc_list

    # Horizontal right: Y, X - 1
    def __add_right(self, x_right, y, piece, tiles, loc_list):
        while x_right == range(0, 8) or y == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y, x_right))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y, x_right))
                else:
                    loc_list.append((y, x_right))
            x_right -= 1
        return loc_list
