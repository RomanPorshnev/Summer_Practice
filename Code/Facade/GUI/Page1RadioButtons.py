from PyQt5.QtWidgets import QLabel, QRadioButton, QPushButton, QButtonGroup


class Page1RadioButtons:
    """
    Отрисовка gui первой страницы (выбор опций пользователем).
    """
    def __init__(self, window):
        self.window = window

        self.group1, self.group2 = QButtonGroup(self.window), QButtonGroup(self.window)

        self.mainText1 = QLabel("Способ задания входных данных:", self.window)

        self.rdbtn1 = QRadioButton("через GUI", self.window)
        self.rdbtn2 = QRadioButton("чтение из файла", self.window)
        self.rdbtn3 = QRadioButton("генерация случайных данных", self.window)

        self.mainText2 = QLabel("Параметры алгоритма:", self.window)

        self.rdbtn4 = QRadioButton("задать самостоятельно", self.window)
        self.rdbtn5 = QRadioButton("значения по умолчанию", self.window)

        self.radioButtons = [self.rdbtn1, self.rdbtn2, self.rdbtn3, self.rdbtn4, self.rdbtn5]
        mainTexts = [self.mainText1, self.mainText2]
        for item in self.radioButtons:
            item.setStyleSheet("font: 25 12pt \"Umpush\";")
        for item in mainTexts:
            item.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.btnNext = QPushButton("далее", self.window)
        self.btnNext.setFixedSize(400, 80)
        self.btnNext.clicked.connect(self.window.choseTypeOfInput)

        for i in range(2):
            self.group1.addButton(self.radioButtons[i])
            self.group2.addButton(self.radioButtons[i + 3])
        self.group1.addButton(self.radioButtons[2])

        self.group1.buttonClicked.connect(self.window.group1Response)
        self.group2.buttonClicked.connect(self.window.group2Response)

        window.vbox.addWidget(self.mainText1)
        window.vbox.addWidget(self.rdbtn1)
        window.vbox.addWidget(self.rdbtn2)
        window.vbox.addWidget(self.rdbtn3)
        window.vbox.addWidget(self.mainText2)
        window.vbox.addWidget(self.rdbtn4)
        window.vbox.addWidget(self.rdbtn5)
        window.vbox.addWidget(self.btnNext)