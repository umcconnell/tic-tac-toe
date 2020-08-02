"""Tic-Tac-Toe Logic"""
from .grid import Grid


class Logic(Grid):
    """Tic-Tac-Toe Logic Class

    Parameters
    ----------
    _game: Game
        Game instance passed from Game initializer.
    turn: str, optional {'X', 'O'}
        Beginning player's turn. Must be either 'X' or 'O'. Default is 'X'.
    """

    def __init__(self, _game, turn: str = "X"):
        super(Logic, self).__init__(turn)

    def next_turn(self):
        """Switch current player's turn to next player"""
        self.turn = "X" if self.turn == "O" else "O"

    def set_at(self, x, y, val):
        """Set a valid value at a given point on the grid

        Parameters
        ----------
        x, y: int
            Position on the grid.
        val: str
            Value to be set.
        """
        assert self.is_valid(val, (x, y)), 'Move is not valid!'
        self.grid[y][x] = val

    def play(self, x, y) -> bool:
        """Execute a player's turn on the board

        Place a player's symbol on a specified position on the board and change
        turns.

        Parameters
        ----------
        x, y: int
            Position on the board at which to place player's symbol.

        Returns
        -------
        bool or str or int
            - Returns ``False`` if the game is not over
            - Returns ``0`` if the game is a tie
            - Returns the symbol of the winning player if a player has won
        """
        self.set_at(x, y, self.turn)

        if self.is_end() is not False:
            print("Game Over! %s wins" % self.is_end())
            print(self)
            return True

        self.next_turn()
        return False
