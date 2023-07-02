from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QRadioButton, QPushButton, QApplication, QVBoxLayout, QButtonGroup
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задача о рюкзаке")
        self.setGeometry(300, 300, 1200, 900)
        self.box = QVBoxLayout(self)
        self.listOfWeights, self.listOfCosts = [], []
        self.page1()

    def page1(self):
        self.group1, self.group2, self.group3 = QButtonGroup(self), QButtonGroup(self), QButtonGroup(self)

        self.mainText1 = QLabel("Способ задания входных данных:", self)

        self.inputType1 = QRadioButton("через GUI", self)
        self.inputType2 = QRadioButton("чтение из файла", self)
        self.inputType3 = QRadioButton("генерация случайных данных", self)

        self.mainText2 = QLabel("Параметры алгоритма:", self)

        self.inputType4 = QRadioButton("задать самостоятельно", self)
        self.inputType5 = QRadioButton("значения по умолчанию", self)

        self.mainText3 = QLabel("Визуализация поиска решения:", self)

        self.inputType6 = QRadioButton("пошаговая", self)
        self.inputType7 = QRadioButton("сразу перейти к решению", self)

        inputTypes = [self.inputType1, self.inputType2, self.inputType3, self.inputType4, self.inputType5,
                      self.inputType6, self.inputType7]
        mainTexts = [self.mainText1, self.mainText2, self.mainText2, self.mainText3]
        for item in inputTypes:
            item.setStyleSheet("font: 25 12pt \"Umpush\";")
        for item in mainTexts:
            item.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.btn = QPushButton("далее", self)
        self.btn.setFixedSize(400, 80)
        self.btn.clicked.connect(self.page2)

        self.group1.addButton(self.inputType1)
        self.group1.addButton(self.inputType2)
        self.group1.addButton(self.inputType3)
        self.group2.addButton(self.inputType4)
        self.group2.addButton(self.inputType5)
        self.group3.addButton(self.inputType6)
        self.group3.addButton(self.inputType7)

        self.group1.buttonClicked.connect(self.group1Response)
        self.group2.buttonClicked.connect(self.group2Response)
        self.group3.buttonClicked.connect(self.group3Response)

        self.box.addWidget(self.mainText1)
        self.box.addWidget(self.inputType1)
        self.box.addWidget(self.inputType2)
        self.box.addWidget(self.inputType3)
        self.box.addWidget(self.mainText2)
        self.box.addWidget(self.inputType4)
        self.box.addWidget(self.inputType5)
        self.box.addWidget(self.mainText3)
        self.box.addWidget(self.inputType6)
        self.box.addWidget(self.inputType7)
        self.box.addWidget(self.btn)
        self.setLayout(self.box)

    def group1Response(self, btn):
        self.group1res = btn.text()
        print(self.group1res)

    def group2Response(self, btn):
        self.group2res = btn.text()
        print(self.group2res)

    def group3Response(self, btn):
        self.group3res = btn.text()
        print(self.group3res)

    def page2(self):
        for i in reversed(range(self.box.count())):
            self.box.itemAt(i).widget().close()
            self.box.takeAt(i)

        self.mainText1 = QLabel("Входные данные: количество предметов, ограничение на суммарный вес, "
                                "вес и стоимость предметов.", self)
        self.mainText1.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.mainText2 = QLabel("Введите количество предметов:", self)
        self.mainText2.setStyleSheet("font: oblique 13pt \"Umpush\";")

        self.page2lvl = 1
        self.inputData = QtWidgets.QLineEdit(self, placeholderText = "сюда")
        self.inputData.setFixedSize(600, 80)
        self.inputData.returnPressed.connect(self.page2_mod, self.page2lvl)

        self.btn = QPushButton("далее", self)
        self.btn.setFixedSize(400, 80)
        self.btn.clicked.connect(self.page3)

        self.box.addWidget(self.mainText1)
        self.box.addWidget(self.mainText2)
        self.box.addWidget(self.inputData)
        self.box.addWidget(self.btn)

    def page2_mod(self):
        print(self.inputData.text())
        if self.page2lvl == 1:
            self.numOfItems = int(self.inputData.text())
            self.mainText2.setText("Введите ограничение на суммарный вес:")
            self.page2lvl = 2
        elif self.page2lvl == 2:
            self.weightLimit = int(self.inputData.text())
            self.mainText2.setText("Введите вес и стоимость предмета через пробел:")
            self.page2lvl = 3
        elif self.page2lvl == 3:
            x, y = [int(i) for i in self.inputData.text().split()]
            self.listOfWeights.append(x)
            self.listOfCosts.append(y)
        self.inputData.clear()

    def page3(self):
        self.mainText1.setText("Параметры алгоритма: вероятность кроссинговера, вероятность мутации, размер популяции.")
        self.mainText2.setText("Введите вероятность кроссинговера (может принимать значения от 0,6 до 0,95):")


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
