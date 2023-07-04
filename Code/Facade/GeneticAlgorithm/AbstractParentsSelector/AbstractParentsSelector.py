from typing import Protocol
from random import randint
import abc


class AbstractParentsSelector(Protocol):
    _population: list
    _selected_parents: list
    _costs: list
    # В конструктор передаётся список хромосом популяции

    def __init__(self, population: list, costs: list):
        self._population = population
        self._costs = costs
        self._selected_parents = []

    '''
    Запуск работы метода выбора родителей
    '''

    @abc.abstractmethod
    def make_parents(self) -> list:
        ...

