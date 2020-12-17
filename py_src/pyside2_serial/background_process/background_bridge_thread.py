import logging
from multiprocessing import Pipe
from queue import Queue
import serial

from PySide2.QtCore import QThread, Signal

from ._background_process import BackgroundProcess
from .cmd import CMD

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class BackgroundBridgeThread(QThread):
    recvFromSerialPortSignal = Signal(bytes)

    def __init__(self) -> None:
        super().__init__()
        self._parentConnection, childConnection = Pipe()
        self._backgroundProcess = BackgroundProcess(connection=childConnection)
        self._commandQueue = Queue()

    def run(self) -> None:
        log.debug("start")
        self._backgroundProcess.start()

        while not self._commandQueue.empty():
            self._commandQueue.get()

        runningCondition = True
        while runningCondition:
            if not self._commandQueue.empty():
                command = self._commandQueue.get()
                if command[0] == CMD.TERMINATE:
                    runningCondition = False
                    self._parentConnection.send([CMD.TERMINATE])
                    break
                elif command[0] == CMD.START_SERIAL_PORT:
                    self._backgroundProcess
                    pass

            if self._parentConnection.poll():
                # child -> parent
                command = self._parentConnection.recv()
                pass

            self.msleep(10)

        self._backgroundProcess.join()
        log.debug("finish")

    def terminateLoop(self) -> None:
        self._commandQueue.put([CMD.TERMINATE])
        while self.isRunning():
            self.msleep(100)

    def openSerialPort(
        self,
        port: str,
        baudrate: int = 115200,
        parity: str = serial.PARITY_NONE,
        bytesize: int = serial.EIGHTBITS,
        stopbits: float = serial.STOPBITS_ONE,
        xonxoff: bool = False,
        rtscts: bool = False,
        dsrdtr: bool = False,
    ) -> None:
        pass

    def closeSerialPort(self) -> None:
        pass

    def sendToSerialPort(self, data: bytes) -> None:
        pass