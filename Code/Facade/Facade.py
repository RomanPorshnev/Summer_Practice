from PyQt5.QtWidgets import QApplication
from qt import *
import sys


class Facade:
    def run(self):
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())
