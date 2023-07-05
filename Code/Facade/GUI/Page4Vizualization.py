from PyQt5.QtWidgets import QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout
from pyqtgraph import PlotWidget

class Page4Vizualization:
    """
    Отрисовка gui четвертой страницы (визуализация работы алгоритма).
    """
    def __init__(self, window):
        self.window = window
        self.data = self.window.dataForALg.input_data
        for i in reversed(range(self.window.vbox.count())):
            self.window.vbox.itemAt(i).widget().close()
            self.window.vbox.takeAt(i)

        self.mainText1 = QLabel("Функция качества решения", window)
        self.mainText1.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.graphic = PlotWidget()
        self.graphic.plot(x = self.data.weights, y = self.data.costs, pen = {'color':'black', 'width':5})
        self.graphic.setBackground('w')

        self.mainText2 = QLabel("Лучшее решение", window)
        self.mainText2.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.itemsTable = QTableWidget(self.window)
        self.itemsTable.setColumnCount(len(self.data.weights))
        self.itemsTable.setRowCount(2)
        self.itemsTable.setVerticalHeaderLabels(["вес", "цена"])
        self.itemsTable.setEditTriggers(QTableWidget.NoEditTriggers)

        for i in range(len(self.data.weights)):
            self.itemsTable.setColumnWidth(i, 6)
            self.itemsTable.setItem(0, i, QTableWidgetItem(str(self.data.weights[i])))
            self.itemsTable.setItem(1, i, QTableWidgetItem(str(self.data.costs[i])))

        self.mainText3 = QLabel(f"Вес: {10}, стоимость: {200}", window)
        self.mainText3.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.hbox = QHBoxLayout()

        self.btnPrev = QPushButton("ПРЕД ШАГ", window)
        self.btnPrev.setFixedSize(400, 80)

        self.btnRes = QPushButton("РЕЗУЛЬТАТ", window)
        self.btnRes.setFixedSize(400, 80)

        self.btnRestart = QPushButton("НОВЫЕ ПАРАМЕТРЫ", window)
        self.btnRestart.setFixedSize(400, 80)

        self.btnNext = QPushButton("СЛЕД ШАГ", window)
        self.btnNext.setFixedSize(400, 80)

        self.hbox.addWidget(self.btnPrev)
        self.hbox.addWidget(self.btnRes)
        self.hbox.addWidget(self.btnRestart)
        self.hbox.addWidget(self.btnNext)

        self.window.vbox.addWidget(self.mainText1)
        self.window.vbox.addWidget(self.graphic)
        self.window.vbox.addWidget(self.mainText2)
        self.window.vbox.addWidget(self.itemsTable)
        self.window.vbox.addLayout(self.hbox)