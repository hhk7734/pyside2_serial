import logging
from multiprocessing import connection, Process
import serial
import time

from .cmd import CMD

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class BackgroundProcess(Process):
    def __init__(self, connection: connection.Connection) -> None:
        super().__init__(daemon=True)
        self._childConnection = connection

    def run(self) -> None:
        log.debug("start")
        runningCondition = True

        uart = serial.Serial()
        uart.timeout = 0

        while runningCondition:
            if self._childConnection.poll():
                # parent -> child
                command = self._childConnection.recv()
                if command[0] == CMD.SEND_SERIAL_PORT:
                    uart.write(command[1])
                elif command[0] == CMD.TERMINATE:
                    runningCondition = False
                    if uart.is_open:
                        uart.close()
                    break
                elif command[0] == CMD.OPEN_SERIAL_PORT:
                    uart.port = command[1]["port"]
                    uart.baudrate = command[1]["baudrate"]
                    uart.parity = command[1]["parity"]
                    uart.bytesize = command[1]["bytesize"]
                    uart.stopbits = command[1]["stopbits"]
                    uart.xonxoff = command[1]["xonxoff"]
                    uart.rtscts = command[1]["rtscts"]
                    uart.dsrdtr = command[1]["dsrdtr"]
                    try:
                        uart.open()
                        self._childConnection.send([CMD.OPEN_SERIAL_PORT, True])
                        log.debug("serial open")
                    except serial.serialutil.SerialException:
                        self._childConnection.send(
                            [CMD.OPEN_SERIAL_PORT, False]
                        )
                        log.debug("failed to open serial")
                elif command[0] == CMD.CLOSE_SERIAL_PORT:
                    uart.close()
                    self._childConnection.send([CMD.CLOSE_SERIAL_PORT, True])
                    log.debug("serial close")

            if uart.is_open:
                data = b""
                try:
                    data = uart.read(100)
                except serial.serialutil.SerialException:
                    uart.close()
                    self._childConnection.send([CMD.CLOSE_SERIAL_PORT, True])

                if data != b"":
                    self._childConnection.send([CMD.RECV_SERIAL_PORT, data])

            time.sleep(0.01)

        if uart.is_open:
            uart.close()
        log.debug("finish")
