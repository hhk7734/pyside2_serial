import logging
import os
import queue
import serial

from PySide2.QtCore import QThread, Signal

if os.name == "nt":
    from serial.tools.list_ports_windows import comports
elif os.name == "posix":
    from serial.tools.list_ports_posix import comports


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class SerialThread(QThread):
    CMD_TERMINATE = 1
    CMD_TRANSMIT = 2

    receivedData = Signal(bytes)
    disconnectedAbnomally = Signal()

    def __init__(self):
        super().__init__()
        self._cmdQueue = queue.Queue()
        self._uart = serial.Serial()
        self._uart.timeout = 0  # Non-blocking

    def start(
        self,
        port,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        bytesize=serial.EIGHTBITS,
        stopbits=serial.STOPBITS_ONE,
        xonxoff=False,
        rtscts=False,
        dsrdtr=False,
    ):
        if self.isRunning():
            raise RuntimeError("Already running.")
        else:
            self._uart.port = port
            self._uart.baudrate = baudrate
            self._uart.parity = parity
            self._uart.bytesize = bytesize
            self._uart.stopbits = stopbits
            self._uart.xonxoff = xonxoff
            self._uart.rtscts = rtscts
            self._uart.dsrdtr = dsrdtr
            super().start()

    def run(self):
        log.info("SerialThread Starts.")
        try:
            self._uart.open()
            runningCondition = True
        except serial.serialutil.SerialException:
            self.disconnectedAbnomally.emit()
            runningCondition = False

        while not self._cmdQueue.empty():
            self._cmdQueue.get()

        while runningCondition:
            if not self._cmdQueue.empty():
                cmd = self._cmdQueue.get()
                if cmd[0] == self.CMD_TERMINATE:
                    runningCondition = False
                elif cmd[0] == self.CMD_TRANSMIT:
                    log.debug(cmd[1])
                    self._uart.write(cmd[1])
            try:
                data = self._uart.read(100)
            except serial.serialutil.SerialException:
                self.disconnectedAbnomally.emit()
                break

            if data != b"":
                log.debug(data)
                self.receivedData.emit(data)

        self._uart.close()
        log.info("SerialThread is Finished.")

    def putCmdQueue(self, *args):
        if self.isRunning():
            self._cmdQueue.put(args)
        else:
            raise RuntimeError("Not running.")

    def terminateEventLoop(self):
        self.putCmdQueue(self.CMD_TERMINATE)

    def transmit(self, data: bytes):
        self.putCmdQueue(self.CMD_TRANSMIT, data)

    @classmethod
    def getPorts(cls):
        return {port: desc for port, desc, _ in comports()}