from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QMessageBox
from filelbl import SecondWindow
from Page1RadioButtons import Page1RadioButtons
from Page2InputData import Page2InputData
from Page3ParamsOfAlg import Page3ParamsOfAlg
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
    crossoverProbability : int
        вероятность кроссинговера
    countOfPopulation : int
        объем популяции
    pathToFile : str
        путь к файлу с входными данными
    needOfDataGen : boolean
        необходимость генерации случайных входных данных
    defaultParams : boolean
        необходимость использования дефолтных параметров алгоритма
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задача о рюкзаке")
        self.setGeometry(300, 300, 1200, 900)
        self.vbox = QVBoxLayout(self)
        self.setLayout(self.vbox)

        self.group1res, self.group2res, self.group3res = '', '', ''
        self.weightLimit = 0
        self.listOfWeights, self.listOfCosts = [], []
        self.crossoverProbability = 0
        self.countOfPopulation = 0
        self.pathToFile = ''
        self.needOfDataGen = False
        self.defaultParams = False

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

    def group3Response(self, btn):
        self.group3res = btn.text()

    def choseTypeOfInput(self):
        """
        Проверяет, в каждой ли группе кнопок выбрана опция.
        Если да, то по выбору в первой группе кнопок, определяет, на какую страницу будет совершен переход.
        Если нет, генерируется сообщение об ошибке.
        """
        if self.group1res and self.group2res and self.group3res:
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
        self.listOfCosts.pop()
        self.listOfWeights.pop()

    def choseTypeOfParam(self):
        """
        Определяет страницу для перехода по выбору в группе2 радио кнопок (задание параметров алгоритма).
        """
        if self.group2res == "задать самостоятельно":
            self.page3 = Page3ParamsOfAlg(self)
        if self.group2res == "значения по умолчанию":
            self.choseTypeOfVisual()

    def errorMes(self, mes):
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

    def getFilePath(self, url):
        """
        Записывает путь к файлу, полученный из дочернего окна.
        :param url: str
        """
        self.pathToFile = url
        self.choseTypeOfParam()

    def page3_mod(self):
        """
        Обработчик кнопки ДАЛЕЕ на странице3 (после введения вероятности кроссинговера).
        Отрисовка модификации модифицированной страницы3 (введение объема популяции).
        """
        self.page3.page3_mod()

    def choseTypeOfVisual(self):
        """
        Определяет страницу для перехода по выбору в группе3 радио кнопок (визуализация решения)
        """
        self.countOfPopulation = self.page3.spinParam.value()
        #if self.group3res == "пошаговая"

    def preparingDataForAlg(self):
        """
        Запаковывает данные для передачи в алгоритм.
        """
        pass


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
