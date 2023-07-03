from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QRadioButton, QPushButton, QApplication, QVBoxLayout, QButtonGroup
from filelbl import SecondWindow
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задача о рюкзаке")
        self.setGeometry(300, 300, 1200, 900)
        self.vbox = QVBoxLayout(self)
        self.setLayout(self.vbox)
        self.listOfWeights, self.listOfCosts = [], []
        self.pathToFile = ''
        self.needOfDataGen = False
        self.defaultParams = False
        #page1 = Page1.Page1(self)
        self.page1withRadioButtons()

    def page1withRadioButtons(self):
        self.group1, self.group2, self.group3 = QButtonGroup(self), QButtonGroup(self), QButtonGroup(self)

        self.mainText1 = QLabel("Способ задания входных данных:", self)

        self.rdbtn1 = QRadioButton("через GUI", self)
        self.rdbtn2 = QRadioButton("чтение из файла", self)
        self.rdbtn3 = QRadioButton("генерация случайных данных", self)

        self.mainText2 = QLabel("Параметры алгоритма:", self)

        self.rdbtn4 = QRadioButton("задать самостоятельно", self)
        self.rdbtn5 = QRadioButton("значения по умолчанию", self)

        self.mainText3 = QLabel("Визуализация поиска решения:", self)

        self.rdbtn6 = QRadioButton("пошаговая", self)
        self.rdbtn7 = QRadioButton("сразу перейти к решению", self)

        self.radioButtons = [self.rdbtn1, self.rdbtn2, self.rdbtn3, self.rdbtn4, self.rdbtn5,
                        self.rdbtn6, self.rdbtn7]
        mainTexts = [self.mainText1, self.mainText2, self.mainText2, self.mainText3]
        for item in self.radioButtons:
            item.setStyleSheet("font: 25 12pt \"Umpush\";")
        for item in mainTexts:
            item.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.btnNext = QPushButton("далее", self)
        self.btnNext.setFixedSize(400, 80)
        self.btnNext.clicked.connect(self.choseTypeOfInput)

        for i in range(2):
            self.group1.addButton(self.radioButtons[i])
            self.group2.addButton(self.radioButtons[i+3])
            self.group3.addButton(self.radioButtons[i+5])
        self.group1.addButton(self.radioButtons[2])

        self.group1.buttonClicked.connect(self.group1Response)
        self.group2.buttonClicked.connect(self.group2Response)
        self.group3.buttonClicked.connect(self.group3Response)

        self.vbox.addWidget(self.mainText1)
        self.vbox.addWidget(self.rdbtn1)
        self.vbox.addWidget(self.rdbtn2)
        self.vbox.addWidget(self.rdbtn3)
        self.vbox.addWidget(self.mainText2)
        self.vbox.addWidget(self.rdbtn4)
        self.vbox.addWidget(self.rdbtn5)
        self.vbox.addWidget(self.mainText3)
        self.vbox.addWidget(self.rdbtn6)
        self.vbox.addWidget(self.rdbtn7)
        self.vbox.addWidget(self.btnNext)

    def group1Response(self, btn):
        self.group1res = btn.text()

    def group2Response(self, btn):
        self.group2res = btn.text()

    def group3Response(self, btn):
        self.group3res = btn.text()

    def choseTypeOfInput(self):
        if self.group1res == "через GUI":
            self.page2withDataInput()
        elif self.group1res == "чтение из файла":
            self.page2withFileInput()
        elif self.group1res == "генерация случайных данных":
            self.needOfDataGen = True
            self.choseTypeOfParam()

    def page2withDataInput(self):
        for i in reversed(range(self.vbox.count())):
            self.vbox.itemAt(i).widget().close()
            self.vbox.takeAt(i)

        self.mainText1 = QLabel("Входные данные: количество предметов, ограничение на суммарный вес, "
                                "вес и стоимость предметов.", self)
        self.mainText1.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.mainText2 = QLabel("Введите ограничение на суммарный вес:", self)
        self.mainText2.setStyleSheet("font: oblique 13pt \"Umpush\";")

        self.page2lvl = 1
        self.inputData = QtWidgets.QLineEdit(self, placeholderText = "сюда")
        self.inputData.setFixedSize(600, 80)
        self.inputData.returnPressed.connect(self.page2_mod, self.page2lvl)

        self.btnNext = QPushButton("далее", self)
        self.btnNext.setFixedSize(400, 80)
        self.btnNext.clicked.connect(self.choseTypeOfParam)

        self.vbox.addWidget(self.mainText1)
        self.vbox.addWidget(self.mainText2)
        self.vbox.addWidget(self.inputData)
        self.vbox.addWidget(self.btnNext)

    def page2_mod(self):
        if self.page2lvl == 1:
            if self.inputData.text().isdigit():
                self.weightLimit = int(self.inputData.text())
                self.mainText2.setText("Введите вес и стоимость предмета через пробел:")
                self.btnForCancelStep = QPushButton("отменить ввод последнего предмета", self)
                self.btnForCancelStep.setFixedSize(600, 80)
                self.btnForCancelStep.clicked.connect(self.deleteLastItem)
                self.vbox.insertWidget(3, self.btnForCancelStep)
                self.page2lvl = 2
            else:
                self.errorMes()
        elif self.page2lvl == 2:
            try:
                x, y = [int(i) for i in self.inputData.text().split()]
                self.listOfWeights.append(x)
                self.listOfCosts.append(y)
            except ValueError:
                self.errorMes()
        self.inputData.clear()
        print(self.listOfWeights, self.listOfCosts)

    def deleteLastItem(self):
        self.listOfCosts.pop()
        self.listOfWeights.pop()

    def choseTypeOfParam(self):
        if self.group2res == "задать самостоятельно":
            self.page3withParamsInput()
        if self.group2res == "значения по умолчанию":
            self.choseTypeOfVisual()

    def errorMes(self):
        msg = QtWidgets.QMessageBox()
        msg.setStyleSheet("color: rgb(244, 12, 12); font: 75 13pt \"Umpush\";")
        msg.setWindowTitle("неполадки...")
        msg.setText("Неверный формат данных!")
        msg.exec_()

    def page2withFileInput(self):
        self.file_window = SecondWindow(self)
        self.file_window.submitClicked.connect(self.getFilePath)
        self.file_window.show()

    def getFilePath(self, url):
        self.pathToFile = url
        print(self.pathToFile)
        self.choseTypeOfParam()

    def page3withParamsInput(self):
        for i in reversed(range(self.vbox.count())):
            self.vbox.itemAt(i).widget().close()
            self.vbox.takeAt(i)

        self.mainText1 = QLabel("Параметры алгоритма: вероятность кроссинговера, вероятность мутации, размер популяции.",
                                self)
        self.mainText1.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.mainText2 = QLabel("Введите вероятность кроссинговера (может принимать значения от 60% до 95%):", self)
        self.mainText2.setStyleSheet("font: oblique 13pt \"Umpush\";")

        self.spinParam = QtWidgets.QSpinBox(self, value = 80, maximum = 95, minimum = 60, singleStep = 5, suffix = "%")
        self.vbox.insertWidget(2, self.spinParam)

        self.btnNext = QPushButton("далее", self)
        self.btnNext.setFixedSize(400, 80)
        self.btnNext.clicked.connect(self.page3_mod)

        self.vbox.addWidget(self.mainText1)
        self.vbox.addWidget(self.mainText2)
        self.vbox.addWidget(self.spinParam)
        self.vbox.addWidget(self.btnNext)

    def page3_mod(self):
        self.crossoverProbability = self.spinParam.value()
        self.mainText2.setText("Введите размер популяции (может принимать значения от 20 до 100):")

        self.spinParam.setSuffix("")
        self.spinParam.setMinimum(20)
        self.spinParam.setMaximum(100)
        self.spinParam.setValue(30)

        self.btnNext.clicked.disconnect()
        self.btnNext.clicked.connect(self.choseTypeOfVisual)

    def choseTypeOfVisual(self):
        self.countOfPopulation = self.spinParam.value()
        #if self.group3res == "пошаговая"

    def preparingDataForAlg(self):
        pass


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
