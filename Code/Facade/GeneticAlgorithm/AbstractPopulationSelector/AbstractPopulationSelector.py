from typing import Protocol
from random import randint
import abc


class AbstractPopulationSelector(Protocol):
    '''
    AbstractPopulationSelector - протокол (интерфейс) для рекомбинаторов.
    '''

    _info_about_individuals: list
    _info_about_fined_individuals: list
    _backpack_capacity: int
    _new_population: list

    def __init__(self, info_about_individuals: list, backpack_capacity: int):
        '''
        Инициализация экземпляра класса AbstractRecombinator.

        Args:
            parents_pairs (list): Список пар родителей.
            probability (list): Вероятность рекомбинации.
        '''
        self._info_about_individuals = info_about_individuals
        self._backpack_capacity = backpack_capacity
        self._info_about_fined_individuals = []
        self._new_population = []

    @abc.abstractmethod
    def make_new_population(self) -> list:
        '''
        Абстрактный метод make_new_population.
        Должен быть реализован в дочерних классах для создания новой популяции.

        Returns:
            list: Список потомков новой популяции.
        '''
        ...
