"""Minimax Opponent"""
import math

from .ai import AIPlayer


class MinimaxPlayer(AIPlayer):
    """Minimax Computer Opponent

    Parameters
    ----------
    depth: int, optional
        Maximum search depth for the minimax algorithm. If no depth is
        specified, infinity (``math.inf``) will be used in the minimax
        algorithm. Default is ``None``.
    """

    def __init__(self, depth=None):
        super(MinimaxPlayer, self).__init__()
        self.symbol = None
        self.depth = depth if depth is not None else math.inf

    # pylint: disable=no-else-return
    def score(self, winner):
        """Calculate the game score for a winner node

        Return the score for a given winner. This will be a positive number if
        the winner is the AI, and a negative number if the winner is the human.

        Parameters
        ----------
        winner: str or int
            Symbol of the winner node. Can also be a ``0`` if the state is a
            tie.

        Returns
        -------
        int
            Score of the final game state
        """
        if winner == self.symbol:
            return 10
        elif winner == 0:
            return 0
        else:
            return -10

    # pylint: disable=duplicate-code
    def minimax(self, grid, depth: int, maximizing_player: bool):
        """Minimax algorithm

        Parameters
        ----------
        grid: Grid
            Current game state to calculate the minimax value from.
        depth: int
            Current search depth of the minimax algorithm.
        maximizing_player: bool
            Whether the current player is maximizing or minimizing his score.

        Returns
        -------
        int
            Score of the given grid layout.

        See also
        --------
        src.ai.ABPrunedMinimaxPlayer.minimax: minimax with alpha-beta pruning
        """
        winner = grid.is_end()
        if depth == 0 or (winner is not False):
            return self.score(winner)

        if maximizing_player:
            value = -math.inf
            for pos in grid.available_slots():
                grid[pos] = self.symbol
                score = self.minimax(grid, depth-1, False)
                grid[pos] = None

                value = max(value, score)
            return value
        else:
            value = +math.inf
            for pos in grid.available_slots():
                grid[pos] = 'O' if self.symbol == 'X' else 'X'
                score = self.minimax(grid, depth-1, True)
                grid[pos] = None

                value = min(value, score)
            return value

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
            Position on the board chosen by the algorithm.
        """
        self.symbol = game.turn
        best_score = -math.inf
        best_pos = None

        for pos in game.available_slots():

            game[pos] = self.symbol
            score = self.minimax(game, self.depth, maximizing_player=False)
            game[pos] = None

            if score > best_score:
                best_score = score
                best_pos = pos

        play_fn(best_pos)
        return best_pos
