from AbstractRecombinator import *

class SinglePointRecombinator(AbstractRecombinator):
    '''
    SinglePointRecombinator - класс, наследующийся от AbstractRecombinator.
    Он реализует метод make_children() для создания потомков с помощью одноточечной рекомбинации.
    '''

    def make_children(self):
        '''
        Метод make_children() создает потомков с использованием одноточечной рекомбинации.

        Returns:
            list: Список потомков.
        '''

        for i in range(len(self._parents_pairs)):
            individual1 = self._parents_pairs[i][0].copy()  # Создаем копию первого индивида из пары родителей
            individual2 = self._parents_pairs[i][1].copy()  # Создаем копию второго индивида из пары родителей

            # Проверяем, выполняется ли рекомбинация с заданной вероятностью
            if randint(0, 100) <= self._crossing_probability * 100:
                point = randint(1, len(individual1) - 1)  # Выбираем случайную точку разделения
                # Меняем части индивидов после точки разделения местами
                individual1[point:], individual2[point:] = individual2[point:], individual1[point:]
                # Добавляем созданные потомки и их родителей в список выбранных потомков
                self._selected_children.append((individual1, individual2, self._parents_pairs[i][0], self._parents_pairs[i][1]))

        return self._selected_children  # Возвращаем список выбранных потомков

if __name__ == "__main__":
    for i in range(1):
        arr = []
        for i in range(5):
            # Генерируем случайные пары родителей, представленных в виде бинарных строк
            arr.append(
                (list(bin(randint(16, 31))[2:]), list(bin(randint(16, 32))[2:])))
        x = SinglePointRecombinator(arr, 0.6, 0.8)  # Создаем объект класса SinglePointRecombinator
        print(x.make_children())  # Выводим список созданных потомков
