import sys
import logging

from PySide2.QtWidgets import QApplication

from .main_window.main_window import MainWindow

logging.basicConfig(
    format='[%(levelname)-8s] %(asctime)s | PID %(process)d | %(thread)d | "%(filename)s", %(lineno)d line :%(message)s',
)


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
