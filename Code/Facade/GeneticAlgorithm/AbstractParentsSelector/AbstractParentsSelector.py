from typing import Protocol
import abc


class AbstractParentsSelector(Protocol):
    # В конструктор передаётся список хромосом популяции
    def __init__(self, population: list):
        self._population = population
        self._selected_parents = []

    '''
    Запуск работы метода выбора родителей
    '''

    @abc.abstractmethod
    def execute(self) -> None:
        ...

    '''
    Геттер для получения списка отобранных родителей
    '''

    def get_selected_parents(self):
        return self._selected_parents
