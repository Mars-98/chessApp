from ..parentPiece.piece import Piece


# This is the child class Bishop, that inherits from the parent class piece
# Bishop uses the methods provided in piece, and writes the abstract method move_loc
class Bishop(Piece):
    def __init__(self, piece_move_cnt, piece_points, piece_color, piece_curr_loc):
        super().__init__(piece_move_cnt, piece_points, piece_color, piece_curr_loc)

    # Takes in location: (y ,x) or (column, row) format
    # piece: each piece is a class; bishop, king, rook, pawn, queen, and knight
    # Dictionary of tiles: Key is a tuple of locations, while Value is a tile
    # returns a list of locations that the piece is able to move to
    def move_loc(self, location, piece, tiles):
        loc_list = []

        y_up = location[0] + 1
        y_down = location[0] - 1
        x_left = location[1] + 1
        x_right = location[1] - 1

        loc_list = self.__add_diag_right(y_up, x_right, piece, loc_list,
                                         tiles)  # Diagonal positive right: Y + 1, X - 1
        loc_list = self.__add_diag_left(y_up, x_left, piece, loc_list,
                                        tiles)  # Diagonal positive left: Y + 1, X + 1
        loc_list = self.__add_negDiag_right(y_down, x_right, piece, loc_list,
                                            tiles)  # Diagonal negative right: Y - 1, X - 1
        loc_list = self.__add_negDiag_left(y_down, x_left, piece, loc_list,
                                           tiles)  # Diagonal negative left: Y - 1, X + 1

        return loc_list

    # Diagonal positive right: Y + 1, X - 1
    # Private helper method that is used in move_loc only
    # Takes in (y,x) coordinates or (column,row), as well as the piece, a location list, and tiles dictionary
    # Returns new loc_list, checks and adds locations to location list
    def __add_diag_right(self, y_up, x_right, piece, tiles, loc_list):
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
    def __add_diag_left(self, y_up, x_left, piece, tiles, loc_list):
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
    def __add_negDiag_right(self, y_down, x_right, piece, tiles, loc_list):
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
    def __add_negDiag_left(self, y_down, x_left, piece, tiles, loc_list):
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
