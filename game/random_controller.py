from game.controllers import Controller
import random

class RandomController(Controller):
    BLACK = 1
    WHITE = -1
    BOARD = 0

    def __init__(self, colour):
        self.colour = colour
        self.history = []

    def next_move(self, board):
        """ Will return a single valid move as an (x, y) tuple.
        """
        found_moves = [p.get_position() for p in board.get_move_pieces(self.get_colour())]
        return random.choice(found_moves)

    def get_colour(self):
        return self.colour

    def end_game(self, result):
        pass

    def __str__(self):
        return "Random"

    def __repr__(self):
        return "RandomController"

# This is a Python module defining a class called RandomController, which inherits from the Controller class defined in another module named game.controllers.

# RandomController is designed to control the actions of a player in a game. It is initialized with a colour parameter, which is set to either 1 (black) or -1 (white). The history instance variable is also initialized as an empty list.

# The next_move method returns a single valid move as an (x, y) tuple, chosen at random from all the available moves for the controller's color on the board. The get_colour method returns the controller's color.

# The end_game method takes a result parameter and does nothing with it.

# Finally, the __str__ and __repr__ methods return a string representation of the controller's name as "Random" and "RandomController", respectively.



