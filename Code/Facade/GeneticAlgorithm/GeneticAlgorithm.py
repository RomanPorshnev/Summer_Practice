import sys
from TournamentSelector import *
from Panmixia import *
from HomogeneousRecombinator import *
from ChangingMutator import *
from SelectionByDisplacement import *
import random
from dataclasses import dataclass

sys.path.append("./AbstractParentsSelector")
sys.path.append("./AbstractParentsPairMatcher")
sys.path.append("./AbstractMutator")
sys.path.append("./AbstractRecombinator")
sys.path.append("./AbstractPopulationSelector")


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

    '''
    Данный метод запускает, останавливает и управляет ГА.
    '''

    def make_population_data_list(self):
        population = self.__generate_population()
        i = 0
        while i < 10000:
            # print(population)
            tournament = TournamentSelector(population,
                                            [self.__cost_of_individual(individual) for individual in population])
            parents = tournament.make_parents()
            panmixia = Panmixia(parents)
            parents_pairs = panmixia.make_parents_pairs()
            homogeneous_recombination = HomogeneousRecombinator(parents_pairs, self.__probability_of_crossover, 0.5)
            families = homogeneous_recombination.make_children()
            changing_mutator = ChangingMutator(families)
            children = changing_mutator.make_mutation()
            population_selector = SelectionByDisplacement(self.__init_info_about_individuals(parents + children),
                                                          self.__backpack_capacity)
            population = population_selector.make_new_population()
            i += 1
        max = 0
        chromosome = population[0]
        '''
                for individual in population:
            if self.__cost_of_individual(individual) >= max:
                max = self.__cost_of_individual(individual)
                chromosome = individual
        print(chromosome, max, self.__weight_of_individual(chromosome))
        '''
        for individual in population:
            print(individual, self.__cost_of_individual(individual), self.__weight_of_individual(individual))

    '''
    Данный метод генерирует начальную популяцию.
    Выходные данные: сгенерированная начальная популяция
    '''

    def __generate_population(self) -> list:
        population = []
        i = 0
        while i < self.__number_of_individuals:
            weight_of_individual = 0
            chromosome = ['0'] * self.__number_of_items
            numbers_of_items_not_taken = [i for i in range(self.__number_of_items)]
            numbers_of_taken_items = []
            while True:
                if len(numbers_of_items_not_taken) == 0:
                    population.append(chromosome)
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
                    population.append(chromosome)
                    i += 1
                    break
        return population

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

    def __weight_of_individual(self, individual: list) -> int:
        weight = 0
        for i in range(len(individual)):
            weight += int(individual[i]) * self.__weights[i]
        return weight

    '''
    Данный метод считает цену особи
    Входные данные: особь(хромосома)
    Выходные данные: цена особи
    '''

    def __cost_of_individual(self, individual: list) -> int:
        cost = 0
        for i in range(len(individual)):
            cost += int(individual[i]) * self.__costs[i]
        return cost

    '''
    Данный метод считает вес особи
    Входные данные: особь(хромосома)
    Выходные данные: вес особи
    '''

    def __init_info_about_individuals(self, population: list) -> list:
        info_about_individuals = []
        for individual in population:
            info_about_individual = (
                self.__cost_of_individual(individual), self.__weight_of_individual(individual), individual)
            info_about_individuals.append(info_about_individual)
        return info_about_individuals


def knapsack(weights, values, capacity):
    n = len(weights)
    # Создаем матрицу размером (n+1) x (capacity+1) и заполняем ее нулями
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # Если текущий предмет помещается в рюкзак
            if weights[i - 1] <= j:
                # Выбираем максимальную стоимость между включением или исключением предмета
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                # Текущий предмет не помещается в рюкзак, поэтому стоимость остается такой же, как и для предыдущих предметов
                dp[i][j] = dp[i - 1][j]

    # Восстановление решения
    selected_items = []
    i = n
    j = capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            # Предмет был выбран
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    # Возвращаем максимальную стоимость и выбранные предметы
    return dp[n][capacity], selected_items[::-1]


if __name__ == "__main__":
    for j in range(1):
        input_data = InputData
        input_data.weights = [random.randint(0, 100) for i in range(10)]
        input_data.costs = [random.randint(0, 100) for i in range(10)]
        print(input_data.weights)
        print(input_data.costs)
        input_data.probability_of_mutation = 0.01
        input_data.probability_of_crossover = 0.8
        input_data.number_of_individuals = 10
        input_data.backpack_capacity = 100
        genetic_algorithm = GeneticAlgorithm(input_data)
        genetic_algorithm.make_population_data_list()

        max_value, selected_items = knapsack(input_data.weights, input_data.costs, input_data.backpack_capacity)
        print("Максимальная стоимость:", max_value)
        print("Выбранные предметы (индексы):", selected_items)
