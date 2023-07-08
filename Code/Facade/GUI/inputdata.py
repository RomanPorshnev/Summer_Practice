from typing import List
import random
from dataclasses import dataclass
import enum


class Modifications(enum.Enum):
    # варианты выбор родителей
    tournament_selection = 0
    roulette_selection = 1
    # варианты составления пар
    panmixia = 2
    in_and_outbreeding = 3
    # варианты кроссоверов
    homogeneous_recombination = 4
    single_point_recombination = 5
    # варианты мутаторов
    binary_mutator = 6
    adaptive_mutator = 7
    # варианты селекторов популяции
    elite_selection = 8
    selection_by_displacement = 9


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
    modifications: List[int]


class DataPacking:
    """
    Заполняет структуру данных в зависимости от опций выбранных пользователем.
    """
    def __init__(self, weights: List[int], costs: List[int], backpack_capacity: int, probability_of_mutation: float,
                 probability_of_crossover: float, number_of_individuals: int, modifications: List[str]):
        self.input_data = InputData
        self.input_data.probability_of_crossover = probability_of_crossover
        self.input_data.probability_of_mutation = probability_of_mutation
        self.input_data.number_of_individuals = number_of_individuals
        self.input_data.weights = weights
        self.input_data.costs = costs

        self.input_data.modifications = []
        self.input_data.modifications.append(Modifications.tournament_selection.value)
        self.input_data.modifications.append(Modifications.in_and_outbreeding.value)
        self.input_data.modifications.append(Modifications.homogeneous_recombination.value)
        self.input_data.modifications.append(Modifications.adaptive_mutator.value)
        self.input_data.modifications.append(Modifications.selection_by_displacement.value)

        if "рулеточный" in modifications:
            self.input_data.modifications[0] = Modifications.roulette_selection.value
        if "панмиксия" in modifications:
            self.input_data.modifications[1] = Modifications.panmixia.value
        if "одноточечный" in modifications:
            self.input_data.modifications[2] = Modifications.single_point_recombination.value
        if "двоичный" in modifications:
            self.input_data.modifications[3] = Modifications.binary_mutator.value
        if "элитарный" in modifications:
            self.input_data.modifications[4] = Modifications.elite_selection.value

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
               f"{self.input_data.probability_of_crossover}\nобъем популяции: {self.input_data.number_of_individuals}\n" \
               f"модификации: {self.input_data.modifications}"

    def data_generator(self):
        """
        Случайно генерирует вместительность рюкзака и предметы.
        """
        number_of_items = random.randint(10, 50)
        self.input_data.backpack_capacity = random.randint(100, 500)
        for i in range(number_of_items):
            self.input_data.weights.append(random.randint(1, 100))
            self.input_data.costs.append(random.randint(1, 100))