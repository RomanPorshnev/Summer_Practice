from dataclasses import dataclass


@dataclass
class InputData:
    weights: list
    costs: list
    probability_of_mutation: float
    probability_of_crossover: float
    number_of_individuals: int
    backpack_capacity: int
    modifications: list
