from typing import Protocol
from random import randint
import abc


class AbstractPopulationsSelector(Protocol):
    _population: list
    _selected_population: list
    _costs: list
    # В конструктор передаётся список хромосом популяции

    def __init__(self, population: list, costs: list):
        self._population = population
        self._costs = costs
        self._selected_population = []

    '''
    Запуск работы метода выбора родителей
    '''

    @abc.abstractmethod
    def make_population(self) -> None:
        ...

    '''
    Геттер для получения списка отобранных родителей
    '''

    def get_selected_parents(self):
        return self._selected_population
