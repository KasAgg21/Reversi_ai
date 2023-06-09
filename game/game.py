import os
from collections import deque
from game.board import Board
from game.controllers import PlayerController, AiController
from game.random_controller import RandomController
from game.settings import *

__author__ = 'kashish'


class Game(object):
    """Game ties everything together. It has a board,
    two controllers, and can draw to the screen."""

    def __init__(self, timeout=1,
                 display_moves=True,
                 players=['ai', 'ai'],
                 colour=False):

        self.board = Board(colour)
        self.timeout = timeout
        self.ai_counter = 0
        self.list_of_colours = [BLACK, WHITE]
        self.players = players
        self.display_moves = display_moves
        self.controllers = deque([self._make_controller(c, p) for c, p in zip(self.list_of_colours, self.players)])
        self.player = self.controllers[0].get_colour()
        self.board.set_black(4, 3)
        self.board.set_black(3, 4)
        self.board.set_white(4, 4)
        self.board.set_white(3, 3)
        self.board.mark_moves(self.player)
        self.previous_move = None
        self.previous_round_passed = False

    def _make_controller(self, colour, controller_type):
        """ Returns a controller with the specified colour.
            'player' == PlayerController,
            'ai' == AiController.
        """
        if controller_type == 'player':
            return PlayerController(colour)
        elif controller_type == 'random':
            return RandomController(colour)
        else:
            self.ai_counter += 1
            return AiController(self.ai_counter, colour, self.timeout)

    def show_info(self):
        """ Prints game information to stdout.
        """
        self.player = self.controllers[0].get_colour()
        print("Playing as:       " + self.player)
        print("Displaying moves: " + str(self.display_moves))
        print("Current turn:     " + str(self.controllers[0]))
        print("Number of Black:  " + str(
            len([p for p in self.board.pieces if p.get_state() == BLACK])))
        print("Number of White:  " + str(
            len([p for p in self.board.pieces if p.get_state() == WHITE])))

    def show_board(self):
        """ Prints the current state of the board to stdout.
        """
        self.board.mark_moves(self.player)
        print(self.board.draw())

    def show_commands(self):
        """ Prints the possible moves to stdout.
        """
        moves = [self.to_board_coordinates(piece.get_position()) for piece in self.board.get_move_pieces(self.player)]

        if not moves:
            raise NoMovesError

        print("Possible moves are: ", moves)
        self.board.clear_moves()

    def run(self):
        """ The game loop will print game information, the board, the possible moves, and then wait for the
            current player to make its decision before it processes it and then goes on repeating itself.
        """
        while True:
            os.system('clear')
            self.show_info()
            self.show_board()

            try:
                self.show_commands()
                next_move = self.controllers[0].next_move(self.board)
                self.board.make_move(next_move, self.controllers[0].get_colour())
                self.previous_round_passed = False
            except NoMovesError:
                if self.previous_round_passed:
                    print("Game Over")
                    blacks = len([p for p in self.board.pieces if p.get_state() == BLACK])
                    whites = len([p for p in self.board.pieces if p.get_state() == WHITE])

                    if blacks > whites:
                        print("Black won this game.")
                        exit()
                    elif blacks == whites:
                        print("This game was a tie.")
                        exit()
                    else:
                        print("White won this game.")
                        exit()
                else:
                    self.previous_round_passed = True

            self.controllers.rotate()

            print("Current move is: ", self.to_board_coordinates(next_move))

            self.previous_move = next_move

    def to_board_coordinates(self, coordinate):
        """ Transforms an (x, y) tuple into (a-h, 1-8) tuple.
        """
        x, y = coordinate
        return '{0}{1}'.format(chr(ord('a') + x), y + 1)


# This is the implementation of a simple command-line game called "Reversi" or "Othello". The code consists of a Game class that ties together a Board class, PlayerController class, AiController class, and RandomController class.

# When the Game object is created, it initializes the board, sets the timeout for the AI to make its move, and creates two controllers for the players. It then sets up the board with the starting positions and marks the possible moves for the first player.

# The game loop is run through the run() method, which displays the game information, the current state of the board, and the possible moves for the current player. It then waits for the current player to make a move, processes the move, and switches to the next player. If a player has no moves, the game switches to the next player. If both players have no moves, the game ends and the winner is determined based on the number of pieces on the board.

# The to_board_coordinates() method is used to transform an (x, y) tuple into (a-h, 1-8) tuple for display purposes.



