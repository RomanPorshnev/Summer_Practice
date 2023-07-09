from PyQt5.QtWidgets import QLabel, QPushButton, QSpinBox, QRadioButton, QButtonGroup


class Page3ParamsOfAlg:
    """
    Отрисовка gui третьей страницы (ввод параметров алгоритма пользователем).
    """
    def __init__(self, window):
        self.window = window

        for i in reversed(range(self.window.vbox.count())):
            self.window.vbox.itemAt(i).widget().close()
            self.window.vbox.takeAt(i)

        self.group1, self.group2, self.group3 = QButtonGroup(self.window), QButtonGroup(self.window), QButtonGroup(self.window)
        self.group4, self.group5 = QButtonGroup(self.window), QButtonGroup(self.window)

        self.mainText1 = QLabel("Оператор выбора родителей:", self.window)

        self.rdbtn1 = QRadioButton("турнирный", self.window)
        self.rdbtn2 = QRadioButton("рулеточный", self.window)

        self.mainText2 = QLabel("Составитель пар:", self.window)

        self.rdbtn3 = QRadioButton("аутбридинг + инбридинг", self.window)
        self.rdbtn4 = QRadioButton("панмиксия", self.window)

        self.mainText3 = QLabel("Рекомбинатор:", self.window)

        self.rdbtn5 = QRadioButton("однородный", self.window)
        self.rdbtn6 = QRadioButton("одноточечный", self.window)

        self.mainText4 = QLabel("Мутатор:", self.window)

        self.rdbtn7 = QRadioButton("самоадоптирующийся", self.window)
        self.rdbtn8 = QRadioButton("двоичный", self.window)

        self.mainText5 = QLabel("Селектор:", self.window)

        self.rdbtn9 = QRadioButton("элитарный", self.window)
        self.rdbtn10 = QRadioButton("вытеснение", self.window)

        self.radioButtons = [self.rdbtn1, self.rdbtn2, self.rdbtn3, self.rdbtn4, self.rdbtn5, self.rdbtn6, self.rdbtn7,
                             self.rdbtn8, self.rdbtn9, self.rdbtn10]
        mainTexts = [self.mainText1, self.mainText2, self.mainText3, self.mainText4, self.mainText5]
        for item in self.radioButtons:
            item.setStyleSheet("font: 25 12pt \"Umpush\";")
        for item in mainTexts:
            item.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.btnNext = QPushButton("далее", self.window)
        self.btnNext.setFixedSize(400, 80)
        self.btnNext.clicked.connect(self.window.page3_mod1)

        for i in range(2):
            self.group1.addButton(self.radioButtons[i])
            self.group2.addButton(self.radioButtons[i + 2])
            self.group3.addButton(self.radioButtons[i + 4])
            self.group4.addButton(self.radioButtons[i + 6])
            self.group5.addButton(self.radioButtons[i + 8])

        self.group1.buttonClicked.connect(self.window.group1algResponse)
        self.group2.buttonClicked.connect(self.window.group2algResponse)
        self.group3.buttonClicked.connect(self.window.group3algResponse)
        self.group4.buttonClicked.connect(self.window.group4algResponse)
        self.group5.buttonClicked.connect(self.window.group5algResponse)

        window.vbox.addWidget(self.mainText1)
        window.vbox.addWidget(self.rdbtn1)
        window.vbox.addWidget(self.rdbtn2)
        window.vbox.addWidget(self.mainText2)
        window.vbox.addWidget(self.rdbtn3)
        window.vbox.addWidget(self.rdbtn4)
        window.vbox.addWidget(self.mainText3)
        window.vbox.addWidget(self.rdbtn5)
        window.vbox.addWidget(self.rdbtn6)
        window.vbox.addWidget(self.mainText4)
        window.vbox.addWidget(self.rdbtn7)
        window.vbox.addWidget(self.rdbtn8)
        window.vbox.addWidget(self.mainText5)
        window.vbox.addWidget(self.rdbtn9)
        window.vbox.addWidget(self.rdbtn10)
        window.vbox.addWidget(self.btnNext)

    def page3_mod1(self):
        for i in reversed(range(self.window.vbox.count())):
            self.window.vbox.itemAt(i).widget().close()
            self.window.vbox.takeAt(i)

        self.mainText1 = QLabel("Параметры алгоритма: вероятность кроссинговера, вероятность мутации, размер популяции.",
                                self.window)
        self.mainText1.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.mainText2 = QLabel("Введите вероятность кроссинговера (может принимать значения от 60% до 95%):", self.window)
        self.mainText2.setStyleSheet("font: oblique 13pt \"Umpush\";")

        self.page3lvl = 1
        self.spinParam = QSpinBox(self.window, value=80, maximum=95, minimum=60, singleStep=5, suffix="%")
        self.window.vbox.insertWidget(2, self.spinParam)

        self.btnNext = QPushButton("далее", self.window)
        self.btnNext.setFixedSize(400, 80)
        self.btnNext.clicked.connect(self.window.page3_mod2)

        self.window.vbox.addWidget(self.mainText1)
        self.window.vbox.addWidget(self.mainText2)
        self.window.vbox.addWidget(self.spinParam)
        self.window.vbox.addWidget(self.btnNext)

    def page3_mod2(self):
        if self.page3lvl == 1:
            self.window.crossoverProbability = self.spinParam.value() / 100
            if self.window.group4algRes == "двоичный":
                self.mainText2.setText("Введите вероятность мутации (может принимать значения от 0,05% до 1%):")

                self.spinParam.setSuffix(" x 10^-2 %")
                self.spinParam.setMinimum(5)
                self.spinParam.setMaximum(100)
                self.spinParam.setValue(5)
                self.page3lvl = 2
            else:
                self.window.mutationProbability = self.spinParam.value() / 10000
                self.mainText2.setText("Введите размер популяции (может принимать значения от 20 до 100):")

                self.spinParam.setSuffix("")
                self.spinParam.setMinimum(20)
                self.spinParam.setMaximum(100)
                self.spinParam.setValue(30)

                self.btnNext.clicked.disconnect()
                self.btnNext.clicked.connect(self.window.run_genetic_algorithm)
        elif self.page3lvl == 2:
            self.window.mutationProbability = self.spinParam.value() / 10000
            self.mainText2.setText("Введите размер популяции (может принимать значения от 20 до 100):")

            self.spinParam.setSuffix("")
            self.spinParam.setMinimum(20)
            self.spinParam.setMaximum(100)
            self.spinParam.setValue(30)

            self.btnNext.clicked.disconnect()
            self.btnNext.clicked.connect(self.window.run_genetic_algorithm)