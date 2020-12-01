import logging

from PySide2.QtWidgets import QMainWindow

from .ui_main_window import Ui_MainWindow

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)