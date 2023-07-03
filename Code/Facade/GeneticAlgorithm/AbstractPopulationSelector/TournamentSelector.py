from AbstractPopulationsSelector import *


class TournamentSelector(AbstractPopulationsSelector):
    def make_population(self):
        population_len = len(self._population)
        for i in range(population_len):
            individuals = [randint(0, population_len-1), randint(
                0, population_len-1), randint(0, population_len-1)]
            individuals = [(self._population[j], j)for j in individuals]
            individuals.sort()
            self._selected_population.append(
                self._population[individuals[0][1]])

