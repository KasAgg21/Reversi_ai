import datetime
import threading
from game.ai import AlphaBetaPruner

__author__ = 'kashish'


class Brain(threading.Thread):
    def __init__(self, duration, mutex, q, pieces, first_player, second_player):
        self.mutex = mutex
        self.q = q
        self.duration = duration
        self.pieces = pieces
        self.first_player = first_player
        self.second_player = second_player
        self.has_started = False
        self.lifetime = None
        threading.Thread.__init__(self)

    def run(self):
        """ Starts the Minimax algorithm with the Alpha-Beta Pruning optimization
            and puts the result in a queue once done.
        """
        pruner = AlphaBetaPruner(self.mutex, self.duration, self.pieces, self.first_player, self.second_player)
        result = pruner.alpha_beta_search()
        self.q.put(result)


# This code defines a class Brain that inherits from threading.Thread and runs a Minimax algorithm with Alpha-Beta Pruning optimization on a Reversi game board.

# The __init__ method initializes the instance variables for the class, including the duration for the Minimax search, a mutex for locking, a queue q for storing the result, the pieces on the game board, and the first_player and second_player who will take turns playing.

# The run method starts the Minimax algorithm with the Alpha-Beta Pruning optimization by creating an instance of the AlphaBetaPruner class and calling its alpha_beta_search method. The result is stored in the q queue.

# The Brain class is designed to be run as a separate thread, allowing the main thread to continue running other tasks while the Minimax algorithm searches for the best move on the game board.



