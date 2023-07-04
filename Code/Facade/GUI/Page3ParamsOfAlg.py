from PyQt5.QtWidgets import QLabel, QPushButton, QSpinBox


class Page3ParamsOfAlg:
    """
    Отрисовка gui третьей страницы (ввод параметров алгоритма пользователем).
    """
    def __init__(self, window):
        self.window = window
        for i in reversed(range(self.window.vbox.count())):
            self.window.vbox.itemAt(i).widget().close()
            self.window.vbox.takeAt(i)

        self.mainText1 = QLabel("Параметры алгоритма: вероятность кроссинговера, вероятность мутации, размер популяции.",
                                window)
        self.mainText1.setStyleSheet("font: oblique 14pt \"Umpush\";")

        self.mainText2 = QLabel("Введите вероятность кроссинговера (может принимать значения от 60% до 95%):", window)
        self.mainText2.setStyleSheet("font: oblique 13pt \"Umpush\";")

        self.spinParam = QSpinBox(window, value=80, maximum=95, minimum=60, singleStep=5, suffix="%")
        self.window.vbox.insertWidget(2, self.spinParam)

        self.btnNext = QPushButton("далее", window)
        self.btnNext.setFixedSize(400, 80)
        self.btnNext.clicked.connect(self.window.page3_mod)

        self.window.vbox.addWidget(self.mainText1)
        self.window.vbox.addWidget(self.mainText2)
        self.window.vbox.addWidget(self.spinParam)
        self.window.vbox.addWidget(self.btnNext)

    def page3_mod(self):
        self.window.crossoverProbability = self.spinParam.value()
        self.mainText2.setText("Введите размер популяции (может принимать значения от 20 до 100):")

        self.spinParam.setSuffix("")
        self.spinParam.setMinimum(20)
        self.spinParam.setMaximum(100)
        self.spinParam.setValue(30)

        self.btnNext.clicked.disconnect()
        self.btnNext.clicked.connect(self.window.choseTypeOfVisual)