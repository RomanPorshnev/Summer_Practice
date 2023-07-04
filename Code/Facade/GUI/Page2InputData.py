from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit


class Page2InputData:
    """
    Отрисовка gui второй страницы (ввод входных данных пользователем).
    """
    def __init__(self, window):
        self.window = window
        for i in reversed(range(self.window.vbox.count())):
            self.window.vbox.itemAt(i).widget().close()
            self.window.vbox.takeAt(i)

        self.mainText1 = QLabel("Входные данные: количество предметов, ограничение на суммарный вес, "
                                "вес и стоимость предметов.", window)
        self.mainText1.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.mainText2 = QLabel("Введите ограничение на суммарный вес:", window)
        self.mainText2.setStyleSheet("font: oblique 13pt \"Umpush\";")

        self.page2lvl = 1
        self.inputData = QLineEdit(window, placeholderText = "сюда")
        self.inputData.setFixedSize(600, 80)
        self.inputData.returnPressed.connect(self.window.page2_mod)

        self.btnNext = QPushButton("далее", window)
        self.btnNext.setFixedSize(400, 80)
        self.btnNext.clicked.connect(self.window.choseTypeOfParam)

        self.window.vbox.addWidget(self.mainText1)
        self.window.vbox.addWidget(self.mainText2)
        self.window.vbox.addWidget(self.inputData)
        self.window.vbox.addWidget(self.btnNext)

    def page2_mod(self):
        if self.page2lvl == 1:
            if self.inputData.text().isdigit():
                self.window.weightLimit = int(self.inputData.text())
                self.mainText2.setText("Введите вес и стоимость предмета через пробел:")
                self.btnForCancelStep = QPushButton("отменить ввод последнего предмета", self.window)
                self.btnForCancelStep.setFixedSize(600, 80)
                self.btnForCancelStep.clicked.connect(self.window.deleteLastItem)
                self.window.vbox.insertWidget(3, self.btnForCancelStep)
                self.page2lvl = 2
            else:
                self.window.errorMes("Неверный формат данных!")
        elif self.page2lvl == 2:
            try:
                x, y = [int(i) for i in self.inputData.text().split()]
                self.window.listOfWeights.append(x)
                self.window.listOfCosts.append(y)
            except ValueError:
                self.window.errorMes("Неверный формат данных!")
        self.inputData.clear()
        print(self.window.listOfWeights, self.window.listOfCosts)