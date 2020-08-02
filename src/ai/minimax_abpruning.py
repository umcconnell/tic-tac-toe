"""Minimax Opponent with Alpha-Beta-Pruning"""
import math

from .minimax import MinimaxPlayer


class ABPrunedMinimaxPlayer(MinimaxPlayer):
    """Alpha-Beta-Pruned Minimax Computer Opponent

    Parameters
    ----------
    depth: int, optional
        Maximum search depth for the minimax algorithm. If no depth is
        specified, infinity (``math.inf``) will be used in the minimax
        algorithm. Default is ``None``.
    """

    def __init__(self, depth=None):
        super(ABPrunedMinimaxPlayer, self).__init__(depth)

    # pylint: disable=too-many-arguments, arguments-differ, no-else-return
    # pylint: disable=duplicate-code
    def minimax(self, grid, depth: int, alpha: int = None, beta: int = None,
                maximizing_player: bool = False):
        """Alpha-beta-pruned minimax algorithm

        Parameters
        ----------
        grid: Grid
            Current game state to calculate the minimax value from.
        depth: int
            Current search depth of the minimax algorithm.
        alpha, beta: int
            Values used for alpha-beta pruning.
        maximizing_player: bool
            Whether the current player is maximizing or minimizing his score.

        Returns
        -------
        int
            Score of the given grid layout.

        See also
        --------
        src.ai.MinimaxPlayer.minimax: minimax without alpha-beta pruning
        """
        if alpha is None:
            alpha = -math.inf
        if beta is None:
            beta = +math.inf

        winner = grid.is_end()
        if depth == 0 or (winner is not False):
            return self.score(winner)

        if maximizing_player:
            value = -math.inf
            for pos in grid.available_slots():
                grid[pos] = self.symbol
                score = self.minimax(grid, depth-1, alpha, beta, False)
                grid[pos] = None

                value = max(value, score)
                alpha = max(alpha, score)

                if beta <= alpha:
                    return value

            return value
        else:
            value = +math.inf
            for pos in grid.available_slots():
                grid[pos] = 'O' if self.symbol == 'X' else 'X'
                score = self.minimax(grid, depth - 1, alpha, beta, True)
                grid[pos] = None

                value = min(value, score)
                beta = min(beta, score)

                if beta <= alpha:
                    return value

            return value
