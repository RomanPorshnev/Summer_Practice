from typing import Protocol
import abc


class AbstractParentsMatcher(Protocol):
    _parents: list
    _parents_pairs: list
    # В конструктор передаётся список хромосом популяции

    def __init__(self, parents: list):
        self._parents = parents
        self._parents_pairs = []

    '''
    Запуск работы метода выбора родителей
    '''

    @abc.abstractmethod
    def make_parents_pairs(self) -> list:
        ...

