from dataclasses import dataclass

'''
Структура для хранения информации 
о лучшей хромосоме и среднего значения 
цены по всей текущей популяции на каждой итерации ГА.
'''


@dataclass
class PopulationData:
    best_chromosome: str
    price_of_best_chromosome: int
    weight_of_best_chromosome: int
    average_cost: float
    bad_population: bool
