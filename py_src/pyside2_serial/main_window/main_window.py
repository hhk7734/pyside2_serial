import logging
import os
import serial

from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMainWindow

from .ui_main_window import Ui_MainWindow
from ..background_process.background_bridge_thread import BackgroundBridgeThread

if os.name == "nt":
    from serial.tools.list_ports_windows import comports
elif os.name == "posix":
    from serial.tools.list_ports_posix import comports

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class MainWindow(QMainWindow, Ui_MainWindow):
    backgroundBridgeThread = BackgroundBridgeThread()

    def __init__(self) -> None:
        super().__init__()
        log.debug("start")
        self.setupUi(self)

        """
        portTab
        """
        self.refreshPortComboBox()
        self.portRefreshPushButton.clicked.connect(self.refreshPortComboBox)

        _BAUDRATES = serial.Serial.BAUDRATES
        for baudrate in _BAUDRATES:
            self.portBaudrateComboBox.addItem(f"{baudrate:,}")
        self.portBaudrateComboBox.setCurrentIndex(_BAUDRATES.index(115200))

        self.portOpenClosePushButton.clicked.connect(self.openClosePort)

        """
        textViewTab
        """
        self.textViewEnableCheckBox.clicked.connect(self.enableTextView)

        self.textViewClearPushButton.clicked.connect(
            self.textViewPlainTextEdit.clear
        )

        self.textViewMaxNumLinesSpinBox.valueChanged.connect(
            self.textViewPlainTextEdit.setMaximumBlockCount
        )

        self.textViewPlainTextEdit.setMaximumBlockCount(
            self.textViewMaxNumLinesSpinBox.value()
        )
        self.textViewPlainTextEdit.mouseDoubleClickEvent = (
            self.textViewMouseEvent
        )
        self.textViewPlainTextEdit.mouseMoveEvent = self.textViewMouseEvent
        self.textViewPlainTextEdit.mousePressEvent = self.textViewMouseEvent
        self.textViewPlainTextEdit.mouseReleaseEvent = self.textViewMouseEvent

        self.textViewSendPushButton.clicked.connect(
            self.sendTextViewToSerialPort
        )
        self.textViewSendLineEdit.returnPressed.connect(
            self.sendTextViewToSerialPort
        )

        self.textViewSendLineEndingComboBox.setCurrentIndex(1)

        """
        backgroundBridgeThread
        """
        self.backgroundBridgeThread.start()
        self.backgroundBridgeThread.opendSerialPort.connect(
            self.opendSerialPort
        )
        self.backgroundBridgeThread.closedSerialPort.connect(
            self.closedSerialPort
        )

    def refreshPortComboBox(self):
        self.portComboBox.clear()
        for port, desc, _ in comports():
            self.portComboBox.addItem(port, userData=desc)

    def openSerialPort(self) -> None:
        self.portOpenClosePushButton.setEnabled(False)
        port = self.portComboBox.currentText()
        baudrate = int(self.portBaudrateComboBox.currentText().replace(",", ""))
        parity = serial.PARITY_NONE
        if self.portOddParityRadioButton.isChecked():
            parity = serial.PARITY_ODD
        elif self.portEvenParityRadioButton.isChecked():
            parity = serial.PARITY_EVEN
        bytesize = serial.EIGHTBITS
        if self.port7BitsRadioButton.isChecked():
            bytesize = serial.SEVENBITS
        elif self.port6BitsRadioButton.isChecked():
            bytesize = serial.SIXBITS
        elif self.port5BitsRadioButton.isChecked():
            bytesize = serial.FIVEBITS
        stopbits = serial.STOPBITS_ONE
        if self.port2StopBitRadioButton.isChecked():
            stopbits = serial.STOPBITS_TWO
        # TODO: Control

        self.backgroundBridgeThread.openSerialPort(
            port=port,
            baudrate=baudrate,
            parity=parity,
            bytesize=bytesize,
            stopbits=stopbits,
        )

    def opendSerialPort(self) -> None:
        self.portOpenClosePushButton.setText("Close")
        self.portOpenClosePushButton.setEnabled(True)

    def closeSerialPort(self) -> None:
        self.portOpenClosePushButton.setEnabled(False)
        self.backgroundBridgeThread.closeSerialPort()

    def closedSerialPort(self) -> None:
        self.portOpenClosePushButton.setText("Open")
        self.portOpenClosePushButton.setEnabled(True)

    def openClosePort(self):
        if self.portOpenClosePushButton.text() == "Open":
            self.openSerialPort()
        else:
            self.closeSerialPort()

    def enableTextView(self):
        if self.textViewEnableCheckBox.isChecked():
            self.backgroundBridgeThread.recvFromSerialPortSignal.connect(
                self.appendTextView
            )
        else:
            self.backgroundBridgeThread.recvFromSerialPortSignal.disconnect(
                self.appendTextView
            )

    def textViewMouseEvent(self, event):
        pass

    def appendTextView(self, data: bytes):
        try:
            _temp = data.decode().replace("\r", "")
        except UnicodeDecodeError:
            return
        self.textViewPlainTextEdit.insertPlainText(_temp)
        self.textViewPlainTextEdit.centerCursor()

    def sendTextViewToSerialPort(self) -> None:
        if self.portOpenClosePushButton.text() == "Close":
            # When serial port already opened.
            _endingIndex = self.textViewSendLineEndingComboBox.currentIndex()
            _ending = b""
            if _endingIndex == 1:
                _ending = b"\n"
            elif _endingIndex == 2:
                _ending = b"\r"
            elif _endingIndex == 3:
                _ending = b"\r\n"

            self.backgroundBridgeThread.sendToSerialPort(
                self.textViewSendLineEdit.text().encode() + _ending
            )

    def closeEvent(self, event: QCloseEvent) -> None:
        self.backgroundBridgeThread.terminateLoop()
        log.debug("finish")
        super().closeEvent(event)