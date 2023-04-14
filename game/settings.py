__author__ = 'kashish'

BOARD, WHITE, BLACK, MOVE = 'BOARD', 'WHITE', 'BLACK', 'MOVE'
WIDTH, HEIGHT = 8, 8
NORTH = -HEIGHT
NORTHEAST = -HEIGHT + 1
EAST = 1
SOUTHEAST = HEIGHT + 1
SOUTH = HEIGHT
SOUTHWEST = HEIGHT - 1
WEST = - 1
NORTHWEST = -HEIGHT - 1

DIRECTIONS = (NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST)


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]


def get_opponent(player):
    if player == WHITE:
        return BLACK
    elif player == BLACK:
        return WHITE
    else:
        raise ValueError


class NoMovesError(Exception):
    pass


def outside_board(tile, direction):
    tile_top = 0 <= tile <= 7
    tile_bot = 56 <= tile <= 63
    tile_right = tile % WIDTH == 7
    tile_left = tile % WIDTH == 0
    return  (direction in (NORTH, NORTHEAST, NORTHWEST) and tile_top)   or \
            (direction in (SOUTH, SOUTHWEST, SOUTHEAST) and tile_bot)   or \
            (direction in (NORTHEAST, EAST, SOUTHEAST)  and tile_right) or \
            (direction in (NORTHWEST, WEST, SOUTHWEST)  and tile_left)


# This is a module containing various utility functions and constants used in a game.

# The constants defined are:

# BOARD: a string representing the game board
# WHITE: a string representing the white player
# BLACK: a string representing the black player
# MOVE: a string representing a move
# WIDTH: an integer representing the width of the game board
# HEIGHT: an integer representing the height of the game board
# NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, and NORTHWEST: integers representing the possible directions of movement on the game board.
# The functions defined are:

# chunks(l, n): a generator function that yields successive n-sized chunks from list l
# get_opponent(player): returns the opponent of the player passed as an argument
# outside_board(tile, direction): checks whether a move in a given direction from a given tile would take the player outside the game board. It returns a boolean value.


