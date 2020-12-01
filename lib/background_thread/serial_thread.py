import logging
import os
import queue
import serial

from PySide2.QtCore import QThread

if os.name == "nt":
    from serial.tools.list_ports_windows import comports
elif os.name == "posix":
    from serial.tools.list_ports_posix import comports


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class SerialThread(QThread):
    CMD_TERMINATE = 1

    def __init__(self):
        super().__init__()
        self._cmdQueue = queue.Queue()

    @classmethod
    def getPorts(cls):
        return {port: desc for port, desc, _ in comports()}

    def run(self):
        runningCondition = True
        while runningCondition:
            if not self._cmdQueue.empty():
                cmd = self._cmdQueue.get()
                if cmd[0] == self.CMD_TERMINATE:
                    runningCondition = False

    def putCmdQueue(self, *args):
        self._cmdQueue.put(args)