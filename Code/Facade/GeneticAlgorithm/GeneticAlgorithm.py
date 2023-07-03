class GeneticAlgorithm:

    # В конструкторе происходит распаковка данных,
    # которые задал пользователь (не хватает функционала для управления модификациями).
    def __init__(self, input_data):
        self.__weight_and_cost_list = input_data.weight_and_cost_list
        self.__probability_of_mutation = input_data.probability_of_mutation
        self.__probability_of_crossover = input_data.probability_of_crossover
        self.__number_of_individuals = input_data.number_of_individuals
        self.__backpack_capacity = input_data.backpack_capacity
        self.__population_data_list = []

    '''
    Данный метод запускает и останавливает ГА. P.S. (Управление ГА будет в другом методе)
    '''

    def run(self):

        while True:
            pass

    def get_population_data_list(self):
        return self.__population_data_list
