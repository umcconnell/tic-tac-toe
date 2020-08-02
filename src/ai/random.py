"""Random Opponent"""
import random

from .ai import AIPlayer


# pylint: disable=too-few-public-methods
class RandomPlayer(AIPlayer):
    """Randomly Playing Computer Opponent"""

    def __init__(self):
        super(RandomPlayer, self).__init__()

    # pylint: disable=no-self-use
    def play(self, play_fn, game):
        """Play the AI opponent

        Parameters
        ----------
        play_fn: `callable` [tuple[int, int]]
            Play function receiving a board position (x, y) on which to place
            the AI's symbol.
        game: Game
            Game object containing the game logic and the current game state.

        Returns
        -------
        tuple[int, int]
            Random position on the board chosen by the algorithm.
        """
        available = []

        for pos in game.available_slots():
            available.append(pos)

        pos = random.choice(available)
        play_fn(pos)
        return pos
