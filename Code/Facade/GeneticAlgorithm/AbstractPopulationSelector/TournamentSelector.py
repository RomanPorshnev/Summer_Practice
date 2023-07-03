from AbstractPopulationsSelector import *


class TournamentSelector(AbstractPopulationsSelector):
    def make_population(self):
        population_len = len(self._population)
        for i in range(population_len):
            individuals = [randint(0, population_len-1), randint(
                0, population_len-1), randint(0, population_len-1)]
            individuals = [(self._population[j], j)for j in individuals]
            individuals.sort()
            self._selected_parents.append(
                self._population[individuals[0][1]])
        print(self._selected_population)


x = TournamentSelector(
    ['1010101', '1110001',  '1110000', '1110101', '1110101'], [100, 2, 1, 3])
x.make_population()
