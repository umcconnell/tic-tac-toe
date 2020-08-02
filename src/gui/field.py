"""GUI Field"""
from PySide2 import QtCore, QtWidgets

from src.config import GRID_SIZE, WINDOW_SIZE


# pylint: disable=too-few-public-methods
class Field:
    """Field Class

    Parameters
    ----------
    pos: `tuple` [int, int]
        Position (x, y) of the field in the grid.
    text: str, optional
        String to display in the field. Default is ''.
    onclick: `callable` [Field, Any], optional
        Function to be called with the clicked field when this field is clicked.
        Default is `None`.

    Attributes
    ----------
    pos: `tuple` [int, int]
        Position (x, y) of the field in the grid.
    btn: QtWidgets.QPushbutton
        The actual QtWidget representing the field.
    onclick: `callable` [Field, Any] or None
        Click listener function to be called with the current field when the
        field is clicked.
    """

    def __init__(self, pos, text="", onclick=None):
        super(Field, self).__init__()

        self.pos = pos

        self.btn = QtWidgets.QPushButton(text)
        self.btn.setFixedSize(WINDOW_SIZE//GRID_SIZE, WINDOW_SIZE//GRID_SIZE)

        self.onclick = onclick
        self.btn.clicked.connect(lambda: self.onclick and self.onclick(self))

    @QtCore.Slot()
    def set_text(self, text):
        """Set field text

        Parameters
        ----------
        text: str
            Desired text.
        """
        self.btn.setText(text)
