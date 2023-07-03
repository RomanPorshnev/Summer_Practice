import random

from dataclasses import dataclass


@dataclass
class InputData:
    weights: list
    costs: list
    probability_of_mutation: float
    probability_of_crossover: float
    number_of_individuals: int
    backpack_capacity: int


class GeneticAlgorithm:

    # В конструкторе происходит распаковка данных,
    # которые задал пользователь (не хватает функционала для управления модификациями).
    def __init__(self, input_data):
        self.__number_of_items = len(input_data.weights)
        self.__weights = input_data.weights
        self.__costs = input_data.costs
        self.__probability_of_mutation = input_data.probability_of_mutation
        self.__probability_of_crossover = input_data.probability_of_crossover
        self.__number_of_individuals = input_data.number_of_individuals
        self.__backpack_capacity = input_data.backpack_capacity
        self.__population_data_list = []
        self.__population = []

    '''
    Данный метод запускает, останавливает и управляет ГА.
    '''

    def make_population_data_list(self):
        self.__generate_population()
        for individual in self.__population:
            print(
                f"chromosome = {individual} weight = {self.__compute_weight_of_individual(individual)} cost = "
                f"{self.__compute_cost_of_individual(individual)}")

    '''
    Данный метод генерирует начальную популяцию.
    Выходные данные: сгенерированная начальная популяция
    '''

    def __generate_population(self) -> list:
        i = 0
        while i < self.__number_of_individuals:
            weight_of_individual = 0
            chromosome = ['0'] * self.__number_of_items
            numbers_of_items_not_taken = [i for i in range(self.__number_of_items)]
            numbers_of_taken_items = []
            while True:
                if len(numbers_of_items_not_taken) == 0:
                    self.__population.append(chromosome)
                    i += 1
                    break
                index_of_item_not_taken = random.randint(0, len(numbers_of_items_not_taken) - 1)
                number_of_taken_item = numbers_of_items_not_taken.pop(index_of_item_not_taken)
                numbers_of_taken_items.append(number_of_taken_item)
                chromosome[number_of_taken_item] = '1'
                weight_of_individual += self.__weights[number_of_taken_item]
                if weight_of_individual > self.__backpack_capacity:
                    index_of_returned_item = self.__get_index_of_returned_item(numbers_of_taken_items)
                    number_of_returned_item = numbers_of_taken_items.pop(index_of_returned_item)
                    chromosome[number_of_returned_item] = '0'
                    self.__population.append(chromosome)
                    i += 1
                    break
        return self.__population

    '''
    Данный метод находит индекс предмета, 
    который лучше всего выкинуть из хромосомы,
    чтобы её можно было положить в рюкзак (выкидываем самый жирный по весу предмет).
    Входные данные: номера уже взятых предметов в набор.
    Выходные данные: индекс предмета, который лучше всего выкинуть.
    '''

    def __get_index_of_returned_item(self, numbers_of_taken_items: list) -> int:
        weights_of_gens = [self.__weights[number_of_taken_item] for number_of_taken_item in numbers_of_taken_items]
        max_weight = max(weights_of_gens)
        return weights_of_gens.index(max_weight)

    '''
    Данный метод считает вес особи
    Входные данные: особь(хромосома)
    Выходные данные: вес особи
    '''
    def __compute_weight_of_individual(self, individual):
        weight = 0
        for i in range(len(individual)):
            weight += int(individual[i]) * self.__weights[i]
        return weight

    '''
        Данный метод считает цену особи
        Входные данные: особь(хромосома)
        Выходные данные: цена особи
        '''
    def __compute_cost_of_individual(self, individual):
        cost = 0
        for i in range(len(individual)):
            cost += int(individual[i]) * self.__costs[i]
        return cost


if __name__ == "__main__":
    input_data = InputData
    input_data.weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    input_data.costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    input_data.probability_of_mutation = 0.5
    input_data.probability_of_crossover = 0.5
    input_data.number_of_individuals = 100
    input_data.backpack_capacity = 100
    genetic_algorithm = GeneticAlgorithm(input_data)
    genetic_algorithm.make_population_data_list()
