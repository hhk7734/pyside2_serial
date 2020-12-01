import os
import logging
import serial

from PySide2.QtCore import QThread, Signal

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

if os.name == "nt":
    from serial.tools.list_ports_windows import comports
elif os.name == "posix":
    from serial.tools.list_ports_posix import comports


class BackgroundThread(QThread):
    def __init__(self):
        super().__init__()

    @classmethod
    def getPorts(cls):
        return {port: desc for port, desc, _ in comports()}
