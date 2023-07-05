from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem


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
        self.btnNext.setFixedSize(600, 80)
        self.btnNext.clicked.connect(self.window.choseTypeOfParam)

        self.window.vbox.addWidget(self.mainText1)
        self.window.vbox.addWidget(self.mainText2)
        self.window.vbox.addWidget(self.inputData)
        self.window.vbox.addWidget(self.btnNext)

    def page2_mod(self):
        if self.page2lvl == 1:
            if self.inputData.text().isdigit() and int(self.inputData.text()) > 0:
                self.window.weightLimit = int(self.inputData.text())
                self.mainText2.setText("Введите вес и стоимость предмета через пробел:")
                self.btnForCancelStep = QPushButton("отменить ввод последнего предмета", self.window)
                self.btnForCancelStep.setFixedSize(600, 80)
                self.btnForCancelStep.clicked.connect(self.window.deleteLastItem)
                self.window.vbox.insertWidget(3, self.btnForCancelStep)

                self.mainText3 = QLabel("Текущий набор предметов:", self.window)
                self.mainText3.setStyleSheet("font: oblique 13pt \"Umpush\";")
                self.window.vbox.addWidget(self.mainText3)

                self.itemsTable = QTableWidget(self.window)
                self.itemsTable.setColumnCount(0)
                self.itemsTable.setRowCount(2)
                self.itemsTable.setVerticalHeaderLabels(["вес", "цена"])
                self.itemsTable.setEditTriggers(QTableWidget.NoEditTriggers)
                self.window.vbox.addWidget(self.itemsTable)

                self.counter = 0
                self.page2lvl = 2
            else:
                self.window.errorMes("Неверный формат данных!")
        elif self.page2lvl == 2:
            try:
                x, y = [int(i) for i in self.inputData.text().split()]
                self.window.listOfWeights.append(x)
                self.window.listOfCosts.append(y)

                self.itemsTable.insertColumn(self.counter)
                self.itemsTable.setColumnWidth(self.counter, 8)
                self.itemsTable.setItem(0, self.counter, QTableWidgetItem(str(x)))
                self.itemsTable.setItem(1, self.counter, QTableWidgetItem(str(y)))
                self.counter += 1
            except ValueError:
                self.window.errorMes("Неверный формат данных!")
        self.inputData.clear()