"""Tic-Tac-Toe Game Module"""
from src.gui import Gui
from src.logic import Logic


class Game:
    """Tic-Tac-Toe Game Base Class

    `One class to rule them all`. Unifies the game logic and GUI in one central
    class

    Parameters
    ----------
    ai: `AIPlayer` or None
        User-selected computer opponent. Can be any of the classes defined in
        ``src.ai`` or ``None`` for a classic turn-taking game

    Attributes
    ----------
    logic: Logic
        Tic-tac-toe game logic
    gui: Gui
        Tic-tac-toe GUI
    ai: `AIPlayer` or None
        Possible computer opponent
    """

    def __init__(self, ai=None):
        super(Game, self).__init__()

        self.logic = Logic(self)
        self.gui = Gui(self)
        self.ai = ai

    @property
    def turn(self):
        """Get the symbol of the current player"""
        return self.logic.turn

    @property
    def size(self):
        """Get the size of the grid"""
        return self.logic.size

    def play(self, pos, play_ai=False):
        """Play a round in the game

        This method is called by the human and the AI computer opponent to place
        their symbol and update the GUI and game logic.

        Parameters
        ----------
        pos: `tuple` [int, int]
            Position on which to place current player's symbol
        play_ai: bool, optional
            Whether to let the computer opponnent player play immediately after
            this turn. Defaults to ``False``

        Returns
        -------
        bool
            Whether or not the game is over
        """
        self.gui.fields[pos].set_text(self.turn)

        is_over = self.logic.play(*pos)
        if is_over:
            winner = self.logic.is_end()
            self.gui.game_over(winner)
            return True

        if play_ai:
            return self.play_ai()

        return False

    def play_ai(self):
        """Play the AI if selected by the user

        Returns
        -------
        bool
            Whether or not the AI played
        """
        if not self.ai:
            return False
        self.ai.play(play_fn=self.play, game=self.logic)
        return True

    def restart(self):
        """Reset the GUI and game logic"""
        self.logic = Logic(self)
        self.gui.layout()

    def start(self):
        """Start the GUI"""
        return self.gui.start()
