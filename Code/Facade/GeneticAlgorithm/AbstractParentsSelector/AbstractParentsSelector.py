from typing import Protocol
from random import randint
import abc


class AbstractParentsSelector(Protocol):
    _population: list
    _selected_parents: list
    _costs: list
    _weights: list
    _backpack_capacity: int
    # В конструктор передаётся список хромосом популяции

    def __init__(self, population: list, costs: list, weights: list, backpack_capacity: int):
        self._population = population
        self._costs = costs
        self._weights = weights
        self._backpack_capacity = backpack_capacity
        self._selected_parents = []

    '''
    Запуск работы метода выбора родителей
    '''

    @abc.abstractmethod
    def make_parents(self) -> list:
        ...

