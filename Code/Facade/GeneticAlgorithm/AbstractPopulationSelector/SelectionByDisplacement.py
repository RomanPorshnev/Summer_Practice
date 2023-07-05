from AbstractPopulationSelector import *


class SelectionByDisplacement(AbstractPopulationSelector):
    '''
    Данный метод формирует новую популяцию на основе родителей и их детей
    с опорой на характеристические данные о каждом индивиде по приниципу отбора вытеснением.
    В случае недобора берутся оштрафованные ососби (вес особи > вес рюказака)
    '''

    def make_new_population(self):
        self._info_about_individuals.sort(reverse=True)
        i = 0
        while i != len(self._info_about_individuals):
            if self._info_about_individuals[i][1] > self._backpack_capacity:
                self._info_about_fined_individuals.append(self._info_about_individuals[i])
                self._info_about_individuals.pop(i)
                continue
            i += 1
        next_population = []
        for i in range((len(self._info_about_individuals) + 1) // 2):
            next_population += self._info_about_individuals[i][2]
        if len(next_population) < (len(self._info_about_individuals) + 1) // 2:
            next_population += self.__add_fined_individuals(
                (len(self._info_about_individuals) + 1) // 2 - len(next_population))

    '''
    Данный метод добавляет недостающее количество особей (они оштрафованы)
    '''
    def __add_fined_individuals(self, size_of_shortage):
        fined_individuals = []
        self._info_about_fined_individuals.sort(key=lambda x: x[1])
        for i in range(size_of_shortage):
            fined_individuals += self._info_about_individuals[i][2]
        return fined_individuals
