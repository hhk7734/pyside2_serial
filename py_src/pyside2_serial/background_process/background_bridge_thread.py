import logging
from multiprocessing import Pipe
from queue import Queue

from PySide2.QtCore import QThread

from .background_process import BackgroundProcess

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class BackgroundBridgeThread(QThread):
    CMD_TERMINATE: int = 1

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
                if command[0] == self.CMD_TERMINATE:
                    runningCondition = False
                    self._parentConnection.send([self.CMD_TERMINATE])
                    break

            if self._parentConnection.poll():
                # child -> parent
                pass

            self.msleep(10)

        self._backgroundProcess.join()
        log.debug("finish")

    def terminateLoop(self) -> None:
        self._commandQueue.put([self.CMD_TERMINATE])
        while self.isRunning():
            self.msleep(100)
