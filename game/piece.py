import sys
from game.settings import *
from game import color as clr

__author__ = 'kashish'


class Piece(object):
    """Pieces are laid out on the board on an 8x8 grid."""

    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.state = 'BOARD'
        self.flipped = False
        self.colour = colour

        self.drawing = {
            "WHITE": self.draw_white,
            "BLACK": self.draw_black,
            "BOARD": self.draw_board,
            "MOVE": self.draw_move}

    def draw(self):
        """ Returns a string representation of the piece in its current state.
        """
        result = ''
        if self.state in self.drawing:
            result = self.drawing[self.state]()

        return result

    def draw_white(self):
        """ Returns a string representation of a white piece.
        """
        if self.flipped:
            if self.colour:
                return clr.format_color('><', fg=clr.rgb(4, 4, 4), bg=clr.rgb(5, 5, 5))

            return 'WF'
        else:
            if self.colour:
                return clr.format_color('  ', bg=clr.rgb(5, 5, 5))

            return 'WW'

    def draw_black(self):
        """ Returns a string representation of a black piece.
        """
        if self.flipped:
            if self.colour:
                return clr.format_color('><', fg=clr.rgb(2, 2, 2), bg=clr.rgb(1, 1, 1))
            return 'BF'
        else:
            if self.colour:
                return clr.format_color('  ', bg=clr.rgb(1, 1, 1))

            return 'BB'

    def draw_board(self):
        """ Returns a string representation of a board piece.
        """
        if self.colour:
            return clr.format_color('  ', bg=clr.rgb(0, 3, 0))
        else:
            return '..'

    def draw_move(self):
        """ Returns a string representation of a move piece.
        """
        if self.colour:
            return clr.format_color('><', fg=clr.rgb(5, 0, 0), bg=clr.rgb(0, 3, 0))

        return 'MM'

    def set_black(self):
        """ Sets a piece's state to be BLACK.
        """
        self.state = 'BLACK'

    def set_white(self):
        """ Sets a piece's state to be WHITE.
        """
        self.state = 'WHITE'

    def set_move(self):
        """ Sets a piece's state to be MOVE.
        """
        self.state = MOVE

    def set_board(self):
        """ Sets the piece's state to be BOARD.
        """
        self.state = BOARD

    def get_state(self):
        """ Returns the piece's current state.
        """
        return self.state

    def flip(self):
        """ Flips a piece from WHITE<->BLACK and marks it as flipped.
            Otherwise it returns a ValueError. (You can't flip a move/board piece)
        """
        if self.state == BLACK:
            self.state = WHITE
        elif self.state == WHITE:
            self.state = BLACK
        else:
            raise ValueError

        self.flipped = True

    def set_flipped(self):
        """ Sets the piece to flipped.
        """
        self.flipped = True

    def reset_flipped(self):
        """ Sets the piece to not be flipped.
        """
        self.flipped = False

    def is_flipped(self):
        """ Returns True if the piece is flipped, otherwise False.
        """
        return self.flipped

    def get_position(self):
        """ Returns the piece's coordinates as an (x, y).
        """
        return self.x, self.y

    def __repr__(self):
        return '({0},{1})'.format(self.x, self.y)
    

#     This is a Python class called Piece, which represents a game piece on an 8x8 grid. The class has methods for initializing a piece's position and color, drawing the piece on the board in its current state, changing the piece's state (i.e. from WHITE to BLACK), flipping the piece between black and white, and checking the piece's position and flipped state.

# The draw() method returns a string representation of the piece in its current state, which is determined by the state attribute. The drawing dictionary holds references to drawing functions based on the piece's color and state.

# The set_ methods change the state attribute of the piece to the corresponding state (WHITE, BLACK, MOVE, BOARD).

# The flip() method flips a piece from BLACK to WHITE and vice versa, and marks it as flipped. A ValueError is raised if an attempt is made to flip a MOVE or BOARD piece.

# The is_flipped() method returns True if the piece is flipped, otherwise False.

# The get_position() method returns the piece's current position as a tuple of (x, y).

# The __repr__() method returns a string representation of the piece's current position as "(x,y)".