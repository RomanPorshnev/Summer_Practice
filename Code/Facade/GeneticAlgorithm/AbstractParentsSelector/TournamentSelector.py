from AbstractParentsSelector import *


class TournamentSelector(AbstractParentsSelector):
    '''
    TournamentSelector - класс, наследующийся от AbstractParentsSelector.
    Он реализует метод make_parents() для выбора родителей из популяции с помощью стратегии турнирного отбора.
    '''

    def make_parents(self):
        # Получаем длину популяции
        population_len = len(self._population)

        # Проходимся по популяции
        for i in range(population_len):
            # Выбираем три случайных индивида из популяции
            individuals = [randint(0, population_len - 1), randint(
                0, population_len - 1), randint(0, population_len - 1)]

                # Создаем список кортежей с индивидами и их соответствующими индексами
            individuals = [(self._costs[j] - self._weights[j] * (self._weights[j] > self._backpack_capacity), self._population[j], j)
                           for j in individuals]

            # Сортируем индивидов по их приспособленности (предполагая, что они могут быть отсортированы)
            individuals.sort(reverse=True)
            # Добавляем индивида с наивысшей приспособленностью (индекс 0) в список выбранных родителей
            self._selected_parents.append(
                self._population[individuals[0][2]])
        return self._selected_parents


if __name__ == '__main__':
    arr = ['10011', '11001', '11100', '00110', '00100'] 
    costs = [10, 100, 32, 51, 16]
    x = TournamentSelector(arr, costs)
    print(x.make_parents())
