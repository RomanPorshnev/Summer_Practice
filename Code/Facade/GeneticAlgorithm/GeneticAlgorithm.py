from imports import *


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
        self.__parents_selector, self.__pair_matcher, self.__recombinator, \
        self.__mutator, self.__population_selector = input_data.modifications
        self.__population_data_list = []

    '''
    Данный метод предназначен для отбора родителей в популяции в зависимисомти
    от модификации, которую выбрал пользователь.
    Входные данные: популяция (список особей)
    Выходные данные: родители (список особей)
    '''

    def __get_parents(self, population: list) -> list:
        match self.__parents_selector:
            case Modifications.tournament_selection.value:
                parents_selector = TournamentSelector(population,
                                                      [self.__cost_of_individual(individual) for individual in
                                                       population])
            case Modifications.roulette_selection:
                pass
        parents = parents_selector.make_parents()
        return parents

    '''
    Данный метод предназначен для составления пар родителей по принципу, который задал пользователь.
    Входные данные: список родителей
    Выходные данные: список пар родителей
    '''

    def __get_parents_pairs(self, parents: list) -> list:
        match self.__pair_matcher:
            case Modifications.panmixia.value:
                pair_matcher = Panmixia(parents)
            case Modifications.in_and_outbreeding:
                pair_matcher = Inbreeding(parents)
        parents_pairs = pair_matcher.make_parents_pairs()
        return parents_pairs

    '''
    Данный метод предназначен для формирвания семей (потомок 1, потомок 2, родитель 1, родитель 2) 
    в зависимости от того рекомбинатора, который задал пользователь. 
    Входные данные: список пар родителей
    Выходные данные: список семей, где каждая семья - кортеж размерностью 4
    '''

    def __get_families(self, parents_pairs: list) -> list:
        match self.__recombinator:
            case Modifications.homogeneous_recombination.value:
                recombination = HomogeneousRecombinator(parents_pairs, 0.5, self.__probability_of_crossover)
            case Modifications.single_point_recombination.value:
                recombination = SinglePointRecombinator(parents_pairs, 0.5, self.__probability_of_crossover)
        families = recombination.make_children()
        return families

    '''
    Данный метод предназначен для получения списка отправленных на мутацию детей (не гарантирует, что все дети мутируют)
    в зависимости от установленного пользователем мутатора.
    Входные данные: список семей
    Выходные данные: список детей
    '''

    def __get_children(self, families: list) -> list:
        match self.__mutator:
            case Modifications.binary_mutator.value:
                mutator = ChangingMutator(families, self.__probability_of_mutation)
            case Modifications.adaptive_mutator:
                mutator = ChangingMutator(families, self.__probability_of_mutation)
        children = mutator.make_mutation()
        return children

    '''
    Данный метод формирует новую популяцию из списка родителей и списка детей по тому принципу, 
    который задал пользователь.
    Входные данные: список детей и список родителей
    Выходные данные: новая популяция
    '''

    def __get_new_population(self, children: list, parents: list) -> list:
        match self.__population_selector:
            case Modifications.selection_by_displacement:
                population_selector = SelectionByDisplacement(self.__init_info_about_individuals(parents + children),
                                                              self.__backpack_capacity)
                population = population_selector.make_new_population() + self.__generate_population(
                    int(0.9 * self.__number_of_individuals))
            case Modifications.elite_selection:
                population_selector = EliteSelection(self.__init_info_about_individuals(parents + children),
                                                     self.__backpack_capacity)
                population = population_selector.make_new_population() + self.__generate_population(
                    int(self.__number_of_individuals))
        return population

    def make_population_data_list(self):
        population = self.__generate_population(self.__number_of_individuals)
        self.__init_population_info(population)
        i = 0
        while i < 100:
            parents = self.__get_parents(population)
            parents_pairs = self.__get_parents_pairs(parents)
            families = self.__get_families(parents_pairs)
            children = self.__get_children(families)
            population = self.__get_new_population(children, parents)
            self.__init_population_info(population)
            print(self.__population_data_list[-1].average_cost - self.__population_data_list[-2].average_cost)
            print(i)
    '''
    Данные метод инициализирует самые важные данные о каждой популяции, который нужно для отобржения графика в GUI.
    Входные данные: популяция
    '''
    def __init_population_info(self, population: list) -> None:
        sum_cost_of_population = 0
        max_cost_of_individual = 0
        best_individual = population[0]
        bad_population = True
        for individual in population:
            cost_of_individual = self.__cost_of_individual(individual)
            sum_cost_of_population += cost_of_individual
            if cost_of_individual > max_cost_of_individual and self.__weight_of_individual(
                    individual) <= self.__backpack_capacity:
                bad_population = False
                max_cost_of_individual = cost_of_individual
                best_individual = individual
        population_data = PopulationData(best_individual, max_cost_of_individual,
                                         self.__weight_of_individual(best_individual),
                                         sum_cost_of_population / len(population), bad_population)
        self.__population_data_list.append(population_data)

    '''
    Данный метод генерирует начальную популяцию.
    Выходные данные: сгенерированная начальная популяция
    '''

    def __generate_population(self, number_of_individuals) -> list:
        population = []
        i = 0
        while i < number_of_individuals:
            weight_of_individual = 0
            chromosome = ['0'] * self.__number_of_items
            numbers_of_items_not_taken = [
                i for i in range(self.__number_of_items)]
            numbers_of_taken_items = []
            while True:
                if len(numbers_of_items_not_taken) == 0:
                    population.append(chromosome)
                    i += 1
                    break
                index_of_item_not_taken = random.randint(
                    0, len(numbers_of_items_not_taken) - 1)
                number_of_taken_item = numbers_of_items_not_taken.pop(
                    index_of_item_not_taken)
                numbers_of_taken_items.append(number_of_taken_item)
                chromosome[number_of_taken_item] = '1'
                weight_of_individual += self.__weights[number_of_taken_item]
                if weight_of_individual > self.__backpack_capacity:
                    index_of_returned_item = self.__get_index_of_returned_item(
                        numbers_of_taken_items)
                    number_of_returned_item = numbers_of_taken_items.pop(
                        index_of_returned_item)
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
        weights_of_gens = [self.__weights[number_of_taken_item]
                           for number_of_taken_item in numbers_of_taken_items]
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
    Данный метод инициализирует данные о каждой особи популяции в виде кортежа (цена особи, вес, хромосома)
    Входные данные: список особей
    Выходные данные: список кортежей вида (цена особи, вес, хромосома)
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
                dp[i][j] = max(values[i - 1] + dp[i - 1]
                [j - weights[i - 1]], dp[i - 1][j])
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
    for j in range(10):
        input_data = InputData
        input_data.weights = [random.randint(0, 200) for i in range(10)]
        input_data.costs = [random.randint(0, 100) for i in range(10)]
        input_data.probability_of_mutation = 0.01
        input_data.probability_of_crossover = 0.8
        input_data.number_of_individuals = 20
        input_data.backpack_capacity = 100
        input_data.modifications = [1, 2, 3, 4, 5]
        genetic_algorithm = GeneticAlgorithm(input_data)

        max_value, selected_items = knapsack(
            input_data.weights, input_data.costs, input_data.backpack_capacity)
        print(
            f"Максимальная стоимость: {max_value}, ген алгоритм: {genetic_algorithm.make_population_data_list()}\n\n\n")
