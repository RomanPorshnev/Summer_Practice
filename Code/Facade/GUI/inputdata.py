from typing import List
import random
from dataclasses import dataclass


@dataclass
class InputData:
    """
    Структура данных для передачи введеных пользователем данных в алгоритм.
    """
    weights: List[int]
    costs: List[int]
    backpack_capacity: int
    probability_of_mutation: float
    probability_of_crossover: float
    number_of_individuals: int


class DataPacking:
    """
    Заполняет структуру данных в зависимости от опций выбранных пользователем.
    """
    def __init__(self, weights: List[int], costs: List[int], backpack_capacity: int, probability_of_mutation: float,
                 probability_of_crossover: float, number_of_individuals: int):
        self.input_data = InputData
        self.input_data.probability_of_crossover = probability_of_crossover
        self.input_data.probability_of_mutation = probability_of_mutation
        self.input_data.number_of_individuals = number_of_individuals
        self.input_data.weights = weights
        self.input_data.costs = costs

        if not weights:
            self.data_generator()
        else:
            self.input_data.weights = weights
            self.input_data.costs = costs
            self.input_data.backpack_capacity = backpack_capacity

    def __str__(self):
        return f"веса предметов: {self.input_data.weights}\nстоимости предметов: {self.input_data.costs}\n" \
               f"вместительность рюкзака: {self.input_data.backpack_capacity}\n" \
               f"вер-ть мутации: {self.input_data.probability_of_mutation}\nвер-ть кроссинговера: " \
               f"{self.input_data.probability_of_crossover}\nобъем популяции: {self.input_data.number_of_individuals}"

    def data_generator(self):
        """
        Случайно генерирует вместительность рюкзака и предметы.
        """
        number_of_items = random.randint(10, 50)
        self.input_data.backpack_capacity = random.randint(100, 500)
        for i in range(number_of_items):
            self.input_data.weights.append(random.randint(1, 100))
            self.input_data.costs.append(random.randint(1, 100))