import sys
import logging

from PySide2.QtWidgets import QApplication

from .main_window.main_window import MainWindow


logging.basicConfig(
    format="[%(levelname)-8s] %(asctime)s %(threadName)s %(filename)s %(lineno) 4d 행 : %(message)s",
)


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
