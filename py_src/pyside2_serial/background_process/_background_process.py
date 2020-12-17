import logging
from multiprocessing import connection, Process
import time

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class BackgroundProcess(Process):
    CMD_TERMINATE: int = 1

    def __init__(self, connection: connection.Connection) -> None:
        super().__init__(daemon=True)
        self._childConnection = connection

    def run(self) -> None:
        log.debug("start")
        runningCondition = True

        while runningCondition:
            if self._childConnection.poll():
                # parent -> child
                command = self._childConnection.recv()
                if command[0] == self.CMD_TERMINATE:
                    runningCondition = False
                    break

            time.sleep(0.01)

        log.debug("finish")
