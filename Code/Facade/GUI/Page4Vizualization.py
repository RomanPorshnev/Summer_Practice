from PyQt5.QtWidgets import QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout
from PyQt5.QtGui import QColor
from pyqtgraph import PlotWidget
from dataclasses import dataclass


@dataclass
class PopulationData:
    best_chromosome: str
    price_of_best_chromosome: int
    weight_of_best_chromosome: float
    average_cost: int
    bad_population: bool

class Page4Vizualization:
    """
    Отрисовка gui четвертой страницы (визуализация работы алгоритма).
    """
    def __init__(self, window, steps):
        self.window = window
        self.data = self.window.dataForALg.input_data

        # step1 = PopulationData('110100001', 130, 100, 100, False)
        # step2 = PopulationData('100101001', 140, 105, 110, False)
        # step3 = PopulationData('110101101', 150, 110, 120, False)

        self.steps = steps
        # self.steps.append(step1)
        # self.steps.append(step2)
        # self.steps.append(step3)

        for i in reversed(range(self.window.vbox.count())):
            self.window.vbox.itemAt(i).widget().close()
            self.window.vbox.takeAt(i)

        self.mainText1 = QLabel("Функция качества решения", window)
        self.mainText1.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.textStep = QLabel("шаг 1", window)
        self.textStep.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.graphic = PlotWidget()
        self.graphic.addLegend()
        self.stepCounter = 1
        self.curve = self.graphic.plot(x = [0, self.stepCounter], y = [0, self.steps[0].price_of_best_chromosome],
                                       pen = {'color':'black', 'width':5}, name = "best cost")
        self.curveAvg = self.graphic.plot(x = [0, 1, 2, 3, 4], y = [10, 20, 5, 6, 10],
                                       pen = {'color':'red', 'width':5}, name = "average cost")
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

        self.changeRowColor(self.steps[0].best_chromosome)

        self.mainText3 = QLabel(f"Вес: {10}, стоимость: {200}", window)
        self.mainText3.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.hbox = QHBoxLayout()

        self.btnPrev = QPushButton("ПРЕД ШАГ", window)
        self.btnPrev.setFixedSize(400, 80)
        self.btnPrev.clicked.connect(self.window.PrevStepOfAlg)

        self.btnRes = QPushButton("РЕЗУЛЬТАТ", window)
        self.btnRes.setFixedSize(400, 80)
        self.btnRes.clicked.connect(self.window.ShowLastStepOfAlf)

        self.btnRestart = QPushButton("НОВЫЕ ПАРАМЕТРЫ", window)
        self.btnRestart.setFixedSize(400, 80)
        self.btnRestart.clicked.connect(self.window.RestartAlgWithNewParams)

        self.btnNext = QPushButton("СЛЕД ШАГ", window)
        self.btnNext.setFixedSize(400, 80)
        self.btnNext.clicked.connect(self.window.NextStepOfAlg)

        self.hbox.addWidget(self.btnPrev)
        self.hbox.addWidget(self.btnRes)
        self.hbox.addWidget(self.btnRestart)
        self.hbox.addWidget(self.btnNext)

        self.window.vbox.addWidget(self.mainText1)
        self.window.vbox.addWidget(self.textStep)
        self.window.vbox.addWidget(self.graphic)
        self.window.vbox.addWidget(self.mainText2)
        self.window.vbox.addWidget(self.itemsTable)
        self.window.vbox.addWidget(self.mainText3)
        self.window.vbox.addLayout(self.hbox)

    def changeRowColor(self, chromosome: str):
        for rowInd in range(len(chromosome)):
            if int(chromosome[rowInd]):
                self.itemsTable.item(0, rowInd).setBackground(QColor(175, 235, 184))
                self.itemsTable.item(1, rowInd).setBackground(QColor(175, 235, 184))
            else:
                self.itemsTable.item(0, rowInd).setBackground(QColor(255, 255, 255))
                self.itemsTable.item(1, rowInd).setBackground(QColor(255, 255, 255))