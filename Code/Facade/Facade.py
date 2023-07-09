from PyQt5.QtWidgets import QApplication
from qt import *
import sys


class Facade:
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    facade = Facade()
