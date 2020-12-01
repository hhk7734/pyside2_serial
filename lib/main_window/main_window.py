import logging

from PySide2.QtWidgets import QMainWindow

from .ui_main_window import Ui_MainWindow

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


BAUDRATE = (
    300,
    1_200,
    2_400,
    4_800,
    9_600,
    19_200,
    38_400,
    57_600,
    74_880,
    115_200,
    230_400,
    250_000,
    460_800,
    500_000,
    576_000,
    921_600,
    1_000_000,
    2_000_000,
)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for baudrate in BAUDRATE:
            self.portBaudrateComboBox.addItem(f"{baudrate}")
        self.portBaudrateComboBox.setCurrentIndex(BAUDRATE.index(115200))