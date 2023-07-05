from AbstractPopulationSelector import *
from random import randint


class SelectionByDisplacement(AbstractPopulationSelector):
    '''
    Данный метод формирует новую популяцию на основе родителей и их детей
    с опорой на характеристические данные о каждом индивиде по приниципу отбора вытеснением.
    В случае недобора берутся оштрафованные ососби (вес особи > вес рюказака)
    '''

    def make_new_population(self):
        self._info_about_individuals.sort(reverse=True)
        size_of_new_population = (len(self._info_about_individuals) + 1) // 3
        i = 0
        while i != len(self._info_about_individuals):
            if self._info_about_individuals[i][1] > self._backpack_capacity:
                self._info_about_fined_individuals.append(self._info_about_individuals[i])
                self._info_about_individuals.pop(i)
                continue
            i += 1
        new_population = []
        if size_of_new_population > len(self._info_about_individuals):
            for i in range(len(self._info_about_individuals)):
                new_population += [self._info_about_individuals[i][2]]
            fined_individuals = self.__add_fined_individuals(size_of_new_population - len(self._info_about_individuals))
            new_population += fined_individuals
        else:
            for i in range(size_of_new_population):
                new_population += [self._info_about_individuals[i][2]]

        return new_population

    '''
    Данный метод добавляет недостающее количество особей (они оштрафованы)
    '''

    def __add_fined_individuals(self, size_of_shortage):
        fined_individuals = []
        self._info_about_fined_individuals.sort(key=lambda x: x[1])
        for i in range(size_of_shortage):
            fined_individuals += [self._info_about_fined_individuals[i][2]]
        return fined_individuals


if __name__ == "__main__":
    '''
               
    '''
    for j in range(100000):
        costs = [randint(0, 100) for i in range(10)]
        weights = [randint(0, 200) for i in range(10)]
        chromo = [list(bin(randint(16, 31))[2:]) for i in range(10)]
        arr = list(zip(costs, weights, chromo))
        selection_by_displacement = SelectionByDisplacement(arr, 100)
        l = selection_by_displacement.make_new_population()
        if len(l) != 5:
            print("FUCK")
            break
