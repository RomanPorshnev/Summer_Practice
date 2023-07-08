from typing import Protocol 
from random import randint  
import abc  


class AbstractRecombinator(Protocol):
    '''
    AbstractRecombinator - протокол (интерфейс) для рекомбинаторов.
    '''

    _parents_pairs: list  # Список пар родителей
    _selected_children: list  # Список выбранных потомков
    _crossing_probability: float  # Вероятность рекомбинации
    _changing_probability: float  # Вероятность изменения гена

    def __init__(self, parents_pairs: list, crossing_probability: float, changing_probability: float):
        '''
        Инициализация экземпляра класса AbstractRecombinator.

        Args:
            parents_pairs (list): Список пар родителей.
            probability (list): Вероятность рекомбинации.
        '''
        self._parents_pairs = parents_pairs
        self._crossing_probability = crossing_probability
        self._changing_probability = changing_probability
        self._selected_children = []

    @abc.abstractmethod
    def make_children(self) -> list:
        '''
        Абстрактный метод make_children.
        Должен быть реализован в дочерних классах для создания потомков.

        Returns:
            list: Список потомков.
        '''
        ...

    def get_selected_children(self):
        '''
        Возвращает выбранных потомков.

        Returns:
            list: Список выбранных потомков.
        '''
        return self._selected_children
