import logging
import serial

from PySide2.QtCore import QThread, QTimer
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

        self.portOpenClosePushButton.clicked.connect(self.openClosePort)

        self.serialThread.disconnectedAbnomally.connect(self.openClosePort)

    def refreshPortComboBox(self):
        self.portComboBox.clear()
        for key, value in self.serialThread.getPorts().items():
            self.portComboBox.addItem(key, userData=value)

    def openClosePort(self):
        if self.portOpenClosePushButton.text() == "Open":
            self.portOpenClosePushButton.setEnabled(False)
            self.portOpenClosePushButton.setText("Close")
            _port = self.portComboBox.currentText()
            _baudrate = int(
                self.portBaudrateComboBox.currentText().replace(",", "")
            )
            _parity = None
            if self.portNoParityRadioButton.isChecked():
                _parity = serial.PARITY_NONE
            elif self.portOddParityRadioButton.isChecked():
                _parity = serial.PARITY_ODD
            elif self.portEvenParityRadioButton.isChecked():
                _parity = serial.PARITY_EVEN
            _bytesize = None
            if self.port8BitsRadioButton.isChecked():
                _bytesize = serial.EIGHTBITS
            elif self.port7BitsRadioButton.isChecked():
                _bytesize = serial.SEVENBITS
            elif self.port6BitsRadioButton.isChecked():
                _bytesize = serial.SIXBITS
            elif self.port5BitsRadioButton.isChecked():
                _bytesize = serial.FIVEBITS
            _stopbits = None
            if self.port1StopBitRadioButton.isChecked():
                _stopbits = serial.STOPBITS_ONE
            elif self.port2StopBitRadioButton.isChecked():
                _stopbits = serial.STOPBITS_TWO
            # TODO: Control

            self.serialThread.start(
                port=_port,
                baudrate=_baudrate,
                parity=_parity,
                bytesize=_bytesize,
                stopbits=_stopbits,
            )
        else:
            self.portOpenClosePushButton.setEnabled(False)
            self.serialThread.terminateEventLoop()
            self.portOpenClosePushButton.setText("Open")

        QTimer.singleShot(100, self.enablePortOpenClosePushButton)

    def enablePortOpenClosePushButton(self):
        if self.portOpenClosePushButton.text() == "Open":
            if self.serialThread.isRunning():
                QTimer.singleShot(100, self.enablePortOpenClosePushButton)
            else:
                self.portOpenClosePushButton.setEnabled(True)
        else:
            if self.serialThread.isRunning():
                self.portOpenClosePushButton.setEnabled(True)
            else:
                QTimer.singleShot(100, self.enablePortOpenClosePushButton)

    def closeEvent(self, event):
        self.serialThread.terminateEventLoop()
        QThread.msleep(300)
        log.debug("Finished MainWindow")
        super().closeEvent(event)