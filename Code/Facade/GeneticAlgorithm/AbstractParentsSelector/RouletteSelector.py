from AbstractParentsSelector import *
import random


class RouletteSelector(AbstractParentsSelector):
    def make_parents(self):
        # Вычисляем суммарное значение приспособленности
        total_fitness = sum(self._costs)

        # Вычисляем вероятности выбора каждого индивида
        probabilities = [fitness / total_fitness for fitness in self._costs]
        # Создаем список границ для рулетки
        wheel = [0]
        cumulative_probability = 0
        for probability in probabilities:
            cumulative_probability += probability
            wheel.append(cumulative_probability)
        wheel.pop()
        for _ in range(len(self._population)):
            # Случайным образом выбираем число из диапазона от 0 до 1
            spin = random.random()
            to_add = None
            # Находим выбранный индивид в рулетке
            for i, probability in enumerate(wheel):
                if spin >= probability:
                    to_add = self._population[i]
            self._selected_parents.append(to_add)

        # Если ничего не выбрано (например, из-за ошибки округления), возвращаем последний индивид
        return self._selected_parents


if __name__ == '__main__':
    arr = ['10011', '11001', '11100', '00110', '00100']
    costs = [10, 100, 32, 51, 16]
    x = RouletteSelector(arr, costs)
    print(x.make_parents())
