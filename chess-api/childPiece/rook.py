from ..parentPiece.piece import Piece


# This is the child class Rook, that inherits from the parent class piece
# Rook uses the methods provided in piece, and writes the abstract method move_loc
class Rook(Piece):
    def __init__(self, piece_move_cnt, piece_points, piece_color, piece_curr_loc, piece_first_move=False):
        self.first_move = piece_first_move
        super().__init__(piece_move_cnt, piece_points, piece_color, piece_curr_loc)

    # Takes in location: (y ,x) or (column, row) format
    # piece: each piece is a class; bishop, king, rook, pawn, queen, and knight
    # Dictionary of tiles: Key is a tuple of locations, while Value is a tile
    # returns a list of locations that the piece is able to move to
    def move_loc(self, location, piece, tiles):
        # should I set first_move here?
        # if not self.first_move:
        #     self.first_move = True

        loc_list = []

        y_V_up = location[0] + 1
        y_V_down = location[0] - 1
        x_V = location[1]

        x_H_left = location[1] + 1
        x_H_right = location[1] - 1
        y_H = location[0]

        loc_list = self.__add_V_up(y_V_up, x_V, piece, loc_list, tiles)  # Vertical up: Y + 1, X
        loc_list = self.__add_V_down(y_V_down, x_V, piece, loc_list, tiles)  # Vertical down: Y - 1, X
        loc_list = self.__add_H_left(y_H, x_H_left, piece, loc_list, tiles)  # Horizontal left: Y, X + 1
        loc_list = self.__add_H_right(y_H, x_H_right, piece, loc_list, tiles)  # Horizontal right: Y, X - 1

        piece.first_move = True

        return loc_list

    # Vertical up: Y + 1, X
    # Private helper method that is used in move_loc only
    # Takes in (y,x) coordinates or (column,row), as well as the piece, a location list, and tiles dictionary
    # Returns new loc_list, checks and adds locations to location list
    def __add_V_up(self, x_V, y_V_up, piece, tiles, loc_list):
        while x_V == range(0, 8) or y_V_up == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_V_up, x_V))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_V_up, x_V))
                else:
                    loc_list.append((y_V_up, x_V))
            y_V_up += 1
        return loc_list

    # Vertical down: Y - 1, X
    def __add_V_down(self, x_V, y_V_down, piece, tiles, loc_list):
        while x_V == range(0, 8) or y_V_down == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_V_down, x_V))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_V_down, x_V))
                else:
                    loc_list.append((y_V_down, x_V))
            y_V_down -= 1
        return loc_list

    # Horizontal left: Y, X + 1
    def __add_H_left(self, x_H_left, y_H, piece, tiles, loc_list):
        while x_H_left == range(0, 8) or y_H == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_H, x_H_left))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_H, x_H_left))
                else:
                    loc_list.append((y_H, x_H_left))
            x_H_left += 1
        return loc_list

    # Horizontal right: Y, X - 1
    def __add_H_right(self, x_H_right, y_H, piece, tiles, loc_list):
        while x_H_right == range(0, 8) or y_H == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            tile = tiles.get((y_H, x_H_right))
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y_H, x_H_right))
                else:
                    loc_list.append((y_H, x_H_right))
            x_H_right -= 1
        return loc_list
