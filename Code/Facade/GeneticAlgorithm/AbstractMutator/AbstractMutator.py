from typing import Protocol  
from random import randint  
import abc  


class AbstractMutator(Protocol):
    '''
    AbstractMutator - протокол (интерфейс) для мутаторов.
    '''

    _children_list: list  # Список потомков
    _selected_population: list  # Список выбранной популяции
    _probabilities_mutation: list  # Список вероятностей мутации

    def __init__(self, children_list: list, changing_probability: float = None):
        '''
        Инициализация экземпляра класса AbstractMutator.

        Args:
            children_list (list): Список потомков.
            changing_probability (int, optional): Вероятность мутации. По умолчанию None.
        '''

        self._children_list = children_list
        self._selected_population = []
        self._probabilities_mutation = []

        if changing_probability is None:
            d = 0.2
            M = 0.9

            # Вычисление вероятности мутации для каждого потомка
            for i in range(len(self._children_list)):
                child, parent1, parent2 = self._children_list[i][0], self._children_list[i][1], self._children_list[i][2]
                dist = 0

                # Вычисление расстояния между родителями
                for j in range(len(parent1)):
                    dist += abs(int(parent1[j]) - int(parent2[j]))**d
                dist /= len(parent1)

                probability = (1 - dist) * M
                self._probabilities_mutation.append(probability)
        else:
            # Задание одинаковой вероятности мутации для всех потомков, если пользователь задал
            self._probabilities_mutation = [changing_probability] * len(self._children_list)

    @abc.abstractmethod
    def make_mutation(self) -> list:
        '''
        Абстрактный метод make_population.
        Должен быть реализован в дочерних классах для создания популяции.

        Returns:
            list: Список популяции.
        '''
        ...
