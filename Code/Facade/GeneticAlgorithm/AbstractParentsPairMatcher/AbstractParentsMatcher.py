from typing import Protocol
from random import randint
import abc


class AbstractParentsMatcher(Protocol):
    _parents: list
    _parents_pairs: list

    # В конструктор передаётся список хромосом популяции

    def __init__(self, parents: list):
        self._parents = parents
        self._parents_pairs = []

    @staticmethod
    def _hamming_distance(first_parent, second_parent):
        distance = 0
        for i in range(len(first_parent)):
            if first_parent[i] != second_parent[i]:
                distance += 1
        return distance
    '''
    Запуск работы метода выбора родителей
    '''
    @abc.abstractmethod
    def make_parents_pairs(self) -> list:
        ...
