"""Tic-Tac-Toe Grid"""
from src.config import GRID_SIZE


class Grid:
    """Tic-Tac-Toe Grid Base Class

    Base tic-tac-toe grid supporting pretty-printing, object subscription,
    winner detection, etc.

    Parameters
    ----------
    turn: str, optional {'X', 'O'   }
        First player's symbol, which can be either 'X' or 'O'. Default is 'X'.
    size: int, optional
        Playing field grid size. Defaults to ``GRID_SIZE`` config.

    Attributes
    ----------
    grid: `list` [`list` [str or `None`]]
        Actual tic-tac-toe grid as a 2D list.
    turn: str {'X', 'O'}
        Current player's symbol.
    size: int
        Size of the grid.

    Examples
    --------
    Printing to console:

    >>> grid = Grid()
    >>> grid[0, 1] = 'X'
    >>> print(grid)
    . . .
    X . .
    . . .

    Object subscription:

    >>> grid = Grid()
    >>> grid[2, 1] = 'O'
    >>> print(grid[2, 1])
    O

    Iteration over available slots:

    >>> grid = Grid()
    >>> grid[0, 0] = 'X'
    >>> grid[2, 2] = 'O'
    >>> for x, y in game.logic.available_slots():
    ...     print('%d, %d' % (x, y))
    0, 1
    0, 2
    ...
    2, 1
    """

    def __init__(self, turn: str = 'X', size: int = GRID_SIZE):
        super(Grid, self).__init__()

        if turn not in ['O', 'X']:
            raise ValueError("'turn' must be 'O' or 'X'")

        self.grid = [[None for x in range(size)] for y in range(size)]
        self.turn = turn
        self.size = size

    def __str__(self):
        turn = 'Turn: %s\n' % self.turn
        grid = [' '.join([col or '.' for col in row]) for row in self.grid]

        return turn + '\n'.join(grid)

    def __getitem__(self, pos: int):
        x, y = pos
        return self.grid[y][x]

    def __setitem__(self, pos: int, val):
        x, y = pos
        self.grid[y][x] = val
        return val

    def available_slots(self):
        """Iterate through available slots in the grid

        Yields
        ------
        `tuple` [int, int]
            Position (x, y) on the grid of available slot.
        """
        for x in range(self.size):
            for y in range(self.size):
                curr = self[x, y]
                if curr is None:
                    yield (x, y)

    def is_valid(self, player: str, pos: tuple):
        """Check whether a move is valid.

        Checks if it's the specified player's turn and the move is on an empty
        field on the grid.

        Parameters
        ----------
        player: str
            Symbol of the player trying to make a move.
        pos: `tuple` [int, int]
            Position (x, y) of the desired move.

        Returns
        -------
        bool
            Whether or not the move is valid.

        Notes
        -----

        """
        x, y = pos
        in_bounds = 0 <= x <= self.size and 0 <= y <= self.size

        return self.turn == player and in_bounds and self.grid[y][x] is None

    def _check_row(self, row):
        prev = self.grid[row][0]
        for col in range(self.size):
            curr = self.grid[row][col]
            if curr is None or curr != prev:
                return False
        return prev

    def _check_col(self, col):
        prev = self.grid[0][col]
        for row in range(self.size):
            curr = self.grid[row][col]
            if curr is None or curr != prev:
                return False
        return prev

    # pylint: disable=anomalous-backslash-in-string, too-many-branches
    # pylint: disable=too-many-return-statements, no-else-return
    def is_end(self):
        """Check if the board is full

        Test rows, columns, diagonals and anti-diagonals for a possible winner

        Returns
        -------
        bool or str or int
            - Returns ``False`` if the game is not over
            - Returns ``0`` if the game is a tie
            - Returns the symbol of the winning player if a player has won

        Notes
        -----
        This method starts by walking along the diagonal of the grid, while
        ruling out impossible rows. Therefore, the minimum possible runtime is
        ``n``, where ``n`` is the size of the grid.

        .. math:: \Omega(is\_end()) \in n

        However, in unlucky situations, the algorithm could possibly have to
        check every row, column, and the entire board again! This results in
        a maximum time complexity of:

        .. math::

            O(is\_end()) = n + 3n^2 \\
            O(is\_end()) \in n^2

        """
        rows = list()
        cols = list()
        diagonal = self.grid[0][0]
        anti_diagonal = self.grid[0][-1]

        # Move along a diagonal and save possible winning rows or cols
        # while skipping impossible, i.e. non-matching, rows and cols
        for diag in range(self.size):
            curr = self.grid[diag][diag]
            anti_curr = self.grid[diag][-1 - diag]

            if curr and curr == self.grid[diag][0]:
                rows.append(diag)
            if curr and curr == self.grid[0][diag]:
                cols.append(diag)
            if diagonal and diagonal != curr:
                diagonal = False
            if anti_diagonal and anti_diagonal != anti_curr:
                anti_diagonal = False

        # Return winning diagonal or anti-diagonal
        if diagonal not in [False, None]:
            return diagonal
        elif anti_diagonal not in [False, None]:
            return anti_diagonal

        # Check remaining possible rows and cols
        for row in rows:
            wins = self._check_row(row)
            if wins:
                return wins

        for col in cols:
            wins = self._check_col(col)
            if wins:
                return wins

        # Short-circuit tie checker
        if diagonal is None or anti_diagonal is None:
            return False

        # Check for tie
        for row in self.grid:
            for col in row:
                if col is None:
                    return False

        return 0  # tie
