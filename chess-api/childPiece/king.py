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

        # vertical up
        y_up = location[0] + 1
        x = location[1]

        loc_list = self.__add_loc(y_up, x, piece, loc_list, tiles)

        # vertical down
        y_down = location[0] - 1

        loc_list = self.__add_loc(y_down, x, piece, loc_list, tiles)

        # horizontal left
        y = location[0]
        x_left = location[1] + 1

        loc_list = self.__add_loc(y, x_left, piece, loc_list, tiles)

        # horizontal right
        x_right = location[1] - 1

        loc_list = self.__add_loc(y, x_right, piece, loc_list, tiles)

        loc_list = self.__add_loc(y_up, x_left, piece, loc_list, tiles)  # Diagonal up left: Y + 1, X + 1
        loc_list = self.__add_loc(y_up, x_right, piece, loc_list, tiles)  # Diagonal up right: Y + 1, X - 1
        loc_list = self.__add_loc(y_down, x_left, piece, loc_list, tiles)  # Diagonal down left: Y - 1, X + 1
        loc_list = self.__add_loc(y_down, x_right, piece, loc_list, tiles)  # Diagonal down right: Y - 1, X - 1

        return loc_list

    # Private helper method that is used in move_loc only
    # Takes in (y,x) coordinates or (column,row), as well as the piece, a location list, and a single tile
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
