from AbstractPopulationSelector import *
from random import randint


class SelectionByDisplacement(AbstractPopulationSelector):
    '''
    SelectionByDisplacement - класс, наследующийся от AbstractPopulationSelector.
    Он реализует метод make_new_population() для создания новой популяции с помощью смещения.
    '''

    def make_new_population(self):
        '''
        Метод make_new_population() создает новую популяцию с использованием смещения.

        Returns:
            list: Список новой популяции.
        '''

        self._info_about_individuals = sorted(
            self._info_about_individuals, key=lambda x: (-x[0], x[1]))

        i = 0

        # Добавляем индивидов в список отобранных, пока не достигнем трети от общего размера, или пока не пройдем все индивиды
        while len(self._info_about_fined_individuals) < len(self._info_about_individuals) // 3 and i < len(self._info_about_individuals):
            if self._info_about_individuals[i][1] < self._backpack_capacity:
                # Проверяем, что у отобранных индивидов нет смежных индивидов
                if all([(self.hamming_distance(elem, self._info_about_individuals[i][2]) > 0) for elem in self._info_about_fined_individuals]):
                    self._info_about_fined_individuals.append(
                        self._info_about_individuals[i][2])
            i += 1

        i = 0

        # Добавляем оставшихся индивидов в список отобранных, пока не достигнем трети от общего размера, или пока не пройдем все индивиды
        while len(self._info_about_fined_individuals) < len(self._info_about_individuals) // 3 and i < len(self._info_about_individuals):
            if self._info_about_individuals[i] not in self._info_about_fined_individuals:
                self._info_about_fined_individuals.append(
                    self._info_about_individuals[i][2])
            i += 1

        # Возвращаем список отобранных индивидов
        return self._info_about_fined_individuals

    @staticmethod
    def hamming_distance(individual1, individual2):
        '''
        Статический метод hamming_distance() вычисляет расстояние Хэмминга между двумя индивидами.

        Args:
            individual1 (str): Первый индивид.
            individual2 (str): Второй индивид.

        Returns:
            int: Расстояние Хэмминга.
        '''

        counter = 0
        for i in range(len(individual1)):
            if individual1[i] != individual2[i]:
                counter += 1
        return counter
