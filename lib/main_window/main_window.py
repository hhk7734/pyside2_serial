import logging
import serial

from PySide2.QtWidgets import QMainWindow

from .ui_main_window import Ui_MainWindow
from ..background_thread.serial_thread import SerialThread

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class MainWindow(QMainWindow, Ui_MainWindow):
    serialThread = SerialThread()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.refreshPortComboBox()

        self.portRefreshPushButton.clicked.connect(self.refreshPortComboBox)

        _BAUDRATES = serial.Serial.BAUDRATES
        for baudrate in _BAUDRATES:
            self.portBaudrateComboBox.addItem(f"{baudrate:,}")
        self.portBaudrateComboBox.setCurrentIndex(_BAUDRATES.index(115200))

    def refreshPortComboBox(self):
        self.portComboBox.clear()
        for key, value in self.serialThread.getPorts().items():
            self.portComboBox.addItem(key, userData=value)
