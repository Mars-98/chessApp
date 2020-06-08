from ..parentPiece.piece import Piece


# This is the child class king, that inherits from the parent class piece
# King uses the methods provided in piece, and writes the abstract method move_loc
class King(Piece):

    # constructor
    def __init__(self, piece_move_cnt, piece_points, piece_color, piece_curr_loc, piece_first_move=False):
        self.first_move = piece_first_move
        super().__init__(piece_move_cnt, piece_points, piece_color, piece_curr_loc)

    # Takes in location: (y ,x) or (column, row) format
    # piece: each piece is a class; bishop, king, rook, pawn, queen, and knight
    # Dictionary of tiles: Key is a tuple of locations, while Value is a tile
    # returns a list of locations that the piece is able to move to
    def move_loc(self, location, piece, tiles):
        loc_list = []
        tile = tiles.get(location)

        # vertical up
        y_V_up = location[0] + 1
        x_V_up = location[1]
        loc_list = self.add_loc(y_V_up, x_V_up, piece, loc_list, tile)

        # vertical down
        y_V_down = location[0] - 1
        x_V_down = location[1]
        loc_list = self.add_loc(y_V_down, x_V_down, piece, loc_list, tile)

        # horizontal left
        y_H_left = location[0]
        x_H_left = location[1] + 1
        loc_list = self.add_loc(y_H_left, x_H_left, piece, loc_list, tile)

        # horizontal right
        y_H_right = location[0]
        x_H_right = location[1] - 1
        loc_list = self.add_loc(y_H_right, x_H_right, piece, loc_list, tile)

        return loc_list

    # Private helper method that is used in move_loc only
    # Takes in (y,x) coordinates or (column,row), as well as the piece, a location list, and a single tile
    # Does not return anything, only checks and adds locations to location list
    def __add_loc(self, x, y, piece, tile, loc_list):
        if x == range(0, 8) or y == range(0, 8):  # in range method, 0 is inclusive and 1 is exclusive
            if tile:
                if tile.piece_here:
                    if tile.piece_here.color != piece.color:
                        loc_list.append((y, x))
                else:
                    loc_list.append((y, x))
        return loc_list
