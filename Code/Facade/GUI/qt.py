from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from filelbl import SecondWindow
from Page1RadioButtons import Page1RadioButtons
from Page2InputData import Page2InputData
from Page3ParamsOfAlg import Page3ParamsOfAlg
from Page4Vizualization import Page4Vizualization
from inputdata import DataPacking
from GeneticAlgorithm import *
import sys


class Window(QWidget):
    """
    Объект класса - главное окно.
    Установка параметров главного окна, инициализация переменных, ожидаемых от пользователя,
    и вызов конструктора gui для первой страницы.

    Attributes:
    -----------
    group1res, group2res, group3res : str
        резаультаты выбора пользователя в группах радио кнопок
    weightLimit : int
        ограничение на вместительность рюкзака
    listOfWeights, listOfCosts : List[int]
        список весов и стоимостей предметов соответсвенно
    crossoverProbability : float
        вероятность кроссинговера
    mutationProbability: float
        вероятность мутации
    countOfPopulation : int
        объем популяции
    needOfDataGen : boolean
        необходимость генерации случайных входных данных
    defaultParams : boolean
        необходимость использования дефолтных параметров алгоритма
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задача о рюкзаке")
        self.setGeometry(300, 300, 1200, 1000)
        self.setStyleSheet("background-color: rgb(223, 223, 238);")
        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignCenter)
        self.setLayout(self.vbox)

        self.group1res, self.group2res = '', ''
        self.group1algRes, self.group2algRes, self.group3algRes, self.group4algRes, self.group5algRes = '', '', '', '', ''
        self.weightLimit = 0
        self.listOfWeights, self.listOfCosts = [], []
        self.crossoverProbability = 0.8
        self.mutationProbability = 0.01
        self.countOfPopulation = 30
        self.pathToFile = ''
        self.needOfDataGen = False
        self.defaultParams = False

        self.checker = False

        Page1RadioButtons(self)

    def group1Response(self, btn):
        """
        Для радио кнопок, принадлежащщих группе1 (способ задания входных данных).
        Определяет, какая кнопка была нажата и запоминает напдпись на кнопке.
        :param btn: QAbstractButton
        """
        self.group1res = btn.text()

    def group2Response(self, btn):
        self.group2res = btn.text()

    def choseTypeOfInput(self):
        """
        Проверяет, в каждой ли группе кнопок выбрана опция.
        Если да, то по выбору в первой группе кнопок, определяет, на какую страницу будет совершен переход.
        Если нет, генерируется сообщение об ошибке.
        """
        if self.group1res and self.group2res:
            if self.group1res == "через GUI":
                self.page2 = Page2InputData(self)
            elif self.group1res == "чтение из файла":
                self.page2withFileInput()
            elif self.group1res == "генерация случайных данных":
                self.needOfDataGen = True
                self.choseTypeOfParam()
        else:
            self.errorMes("Не все поля заполнены!")

    def page2_mod(self):
        """
        Вызывает функцию отрисовки ui для модифицированной страницы2 (ввод предметов).
        """
        self.page2.page2_mod()

    def deleteLastItem(self):
        """
        Удаляет информацию о последнем добавленном предмете.
        """
        if self.page2.counterOfItems:
            self.listOfCosts.pop()
            self.listOfWeights.pop()
            self.page2.itemsTable.removeColumn(self.page2.counterOfItems - 1)
            self.page2.counterOfItems -= 1

    def choseTypeOfParam(self):
        """
        Определяет страницу для перехода по выбору в группе2 радио кнопок (задание параметров алгоритма).
        """
        if (self.weightLimit and self.listOfWeights) or self.group1res != "через GUI":
            if self.group2res == "задать самостоятельно":
                self.page3 = Page3ParamsOfAlg(self)
            if self.group2res == "значения по умолчанию":
                self.defaultParams = True
                self.run_genetic_algorithm()
        else:
            self.errorMes("Нажмите enter")

    def errorMes(self, mes: str):
        """
        Генерирует всплывающее окно с сообщением об ошибке.
        :param mes: str
        """
        msg = QMessageBox()
        msg.setStyleSheet("color: rgb(244, 12, 12); font: 75 13pt \"Umpush\";")
        msg.setWindowTitle("неполадки...")
        msg.setText(mes)
        msg.exec_()

    def page2withFileInput(self):
        """
        Открывает дочернее окно для загрузки файла.
        """
        self.file_window = SecondWindow(self)
        self.file_window.submitClicked.connect(self.getFilePath)
        self.file_window.show()

    def getFilePath(self, url: str):
        """
        Считывает данные из файла, полученного из дочернего окна.
        :param url: str
        """
        try:
            file = open(url)
            self.weightLimit = int(file.readline())
            for line in file:
                x, y = [int(i) for i in line.split()]
                self.listOfWeights.append(x)
                self.listOfCosts.append(y)
            file.close()
            self.choseTypeOfParam()
        except ValueError:
            self.errorMes("Неверный формат данных!")
            self.page2withFileInput()

    def page3_mod1(self):
        """
        Обработчик кнопки ДАЛЕЕ на странице3 (после выбора модификаций).
        Отрисовка модификации страницы3мод1 (введение вероятности кроссинговера).
        """
        if self.group1algRes and self.group2algRes and self.group3algRes and self.group4algRes and self.group5algRes:
            self.page3.page3_mod1()
        else:
            self.errorMes("Не все поля заполнены!")

    def page3_mod2(self):
        """
        Обработчик кнопки ДАЛЕЕ на странице3мод1 (после введения вероятности кроссинговера).
        Отрисовка модификации страницы3 (введение объема популяции).
        """
        self.page3.page3_mod2()
        print("\n")

    def group1algResponse(self, btn):
        self.group1algRes = btn.text()

    def group2algResponse(self, btn):
        self.group2algRes = btn.text()

    def group3algResponse(self, btn):
        self.group3algRes = btn.text()

    def group4algResponse(self, btn):
        self.group4algRes = btn.text()

    def group5algResponse(self, btn):
        self.group5algRes = btn.text()

    def run_genetic_algorithm(self):
        """
        Определяет страницу для перехода по выбору в группе3 радио кнопок (визуализация решения)
        """
        if not self.defaultParams:
            self.countOfPopulation = self.page3.spinParam.value()
        self.preparingDataForAlg()
        genetic_algorithm = GeneticAlgorithm(self.dataForALg.input_data)
        population_data_list = genetic_algorithm.run()
        self.page4 = Page4Vizualization(self, population_data_list)
        # if self.group3res == "пошаговая"

    def PrevStepOfAlg(self):
        """
        Отображает предыдущий шаг алгоритма.
        """
        if self.page4.stepCounter > 1:
            self.page4.stepCounter -= 1
            k = self.page4.stepCounter
            self.page4.textStep.setText(f"шаг {k}")
            countingArr = [i for i in range(k + 1)]
            yArr, yArrAvg = [0], [0]
            for i in range(k):
                yArr.append(self.page4.steps[i].price_of_best_chromosome)
                yArrAvg.append(self.page4.steps[i].average_cost)
            self.page4.curve.setData(x=countingArr, y=yArr)
            self.page4.curveAvg.setData(x=countingArr, y=yArrAvg)
            self.page4.changeRowColor(self.page4.steps[k - 1].best_chromosome)
            self.page4.mainText3.setText(f"Вес: {self.page4.steps[k - 1].price_of_best_chromosome}, стоимость: "
                                         f"{self.page4.steps[k - 1].weight_of_best_chromosome}")
            print(f"Вес: {self.page4.steps[k - 1].price_of_best_chromosome}, стоимость: "
                  f"{self.page4.steps[k - 1].weight_of_best_chromosome}, k = {k}")
        else:
            self.errorMes("Нет предыдущих шагов!")

    def NextStepOfAlg(self):
        """
        Отображает следующий шаг алгоритма.
        """
        if self.page4.stepCounter < len(self.page4.steps):
            self.page4.stepCounter += 1
            k = self.page4.stepCounter
            self.page4.textStep.setText(f"шаг {k}")
            countingArr = [i for i in range(k + 1)]
            yArr, yArrAvg = [0], [0]
            for i in range(k):
                yArr.append(self.page4.steps[i].price_of_best_chromosome)
                yArrAvg.append(self.page4.steps[i].average_cost)
            self.page4.curve.setData(x=countingArr, y=yArr)
            self.page4.curveAvg.setData(x=countingArr, y=yArrAvg)
            self.page4.changeRowColor(self.page4.steps[k - 1].best_chromosome)
            self.page4.mainText3.setText(f"Вес: {self.page4.steps[k - 1].price_of_best_chromosome}, стоимость: "
                                         f"{self.page4.steps[k - 1].weight_of_best_chromosome}")
            print(f"Вес: {self.page4.steps[k - 1].price_of_best_chromosome}, стоимость: "
                  f"{self.page4.steps[k - 1].weight_of_best_chromosome}, k = {k}")
        else:
            self.errorMes("Это последний шаг!")

    def ShowLastStepOfAlf(self):
        """
        Отображает последний шаг алгоритма.
        """
        self.page4.stepCounter = len(self.page4.steps)
        k = self.page4.stepCounter
        self.page4.textStep.setText(f"шаг {k}")
        countingArr = [i for i in range(k + 1)]
        yArr, yArrAvg = [0], [0]
        for i in range(k):
            yArr.append(self.page4.steps[i].price_of_best_chromosome)
            yArrAvg.append(self.page4.steps[i].average_cost)
        self.page4.curve.setData(x=countingArr, y=yArr)
        self.page4.curveAvg.setData(x=countingArr, y=yArrAvg)
        self.page4.changeRowColor(self.page4.steps[k - 1].best_chromosome)
        self.page4.mainText3.setText(f"Вес: {self.page4.steps[k - 1].price_of_best_chromosome}, стоимость: "
                                     f"{self.page4.steps[k - 1].weight_of_best_chromosome}")

    def RestartAlgWithNewParams(self):
        """
        Останавливает отображение алгоритма и отрисовывает страницу со вводом параметров алгоритма.
        """
        for i in reversed(range(self.page4.hbox.count())):
            self.page4.hbox.itemAt(i).widget().close()
            self.page4.hbox.takeAt(i)
        self.vbox.takeAt(6)
        self.page3 = Page3ParamsOfAlg(self)

    def preparingDataForAlg(self):
        """
        Запаковывает данные для передачи в алгоритм.
        """
        modifications = [self.group1algRes, self.group2algRes, self.group3algRes, self.group4algRes, self.group5algRes]
        self.dataForALg = DataPacking(self.listOfWeights, self.listOfCosts, self.weightLimit, self.mutationProbability,
                                      self.crossoverProbability, self.countOfPopulation, modifications)
        self.checker = True
        print(self.dataForALg)
