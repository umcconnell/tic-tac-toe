"""Main Tic-Tac-Toe GUI"""
import sys

from PySide2 import QtWidgets

from src.config import GRID_SIZE, WINDOW_SIZE, WINDOW_TITLE

from .field import Field


class Gui:
    """Tic-Tac-Toe GUI Class

    Parameters
    ----------
    game: Game
        Tic-tac-toe main game instance used to coordinate logic and GUI

    Attributes
    ----------
    app: QtWidgets.QApplication
        Main Qt Application
    window: QtWidgets.QWidget
        Qt Widget representing the GUI window
    grid: QtWidgets.QGridLayout
        Qt grid layout containing the tic-tac-toe grid
    game: Game
        Main tic-tac-toe game instance
    fields: `dict` [`tuple` [int, int], Field]
        Mapping from grid position (x, y) to GUI field elements
    """

    def __init__(self, game):
        super(Gui, self).__init__()

        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QWidget()
        self.grid = QtWidgets.QGridLayout()

        self.game = game
        self.fields = {}

    def _click_handler(self, field):
        field.onclick = None
        self.game.play(field.pos, play_ai=True)

    def game_over(self, winner):
        """Show a game over dialog

        Parameters
        ----------
        winner: str or int
            Winner of the game:
            - ``0`` if the game is a tie
            - The symbol of the winning player if a player has won
        """
        winner_msg = "'%s' wins!" % self.game.turn if winner else "It's a tie!"
        choice = QtWidgets.QMessageBox.question(
            self.window, 'GAME OVER!', winner_msg + '\nRestart?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if choice == QtWidgets.QMessageBox.Yes:
            self.game.restart()
        else:
            sys.exit()

    def layout(self):
        """Layout the window

        Position the fields on the window and attach click handlers.
        """
        self.window.resize(WINDOW_SIZE, WINDOW_SIZE)
        self.window.setWindowTitle(WINDOW_TITLE)

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                pos = x, y
                field = Field(pos, onclick=self._click_handler)
                self.fields[pos] = field
                # field.set_text("row %i, col %i" % (y, x))
                self.grid.addWidget(field.btn, y, x)

        self.grid.setRowStretch(0, GRID_SIZE)
        self.window.setLayout(self.grid)

    def stop(self):
        """Stop the app"""
        self.app.shutdown()

    def start(self):
        """Start the GUI and exit on close"""
        self.layout()
        self.window.show()

        sys.exit(self.app.exec_())
