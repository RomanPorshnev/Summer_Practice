from AbstractMutator import *


class ChangingMutator(AbstractMutator):
    '''
    ChangingMutator - класс, наследующийся от AbstractMutator.
    Он реализует метод make_population() для создания популяции с помощью изменяющейся мутации.
    '''

    def make_mutation(self) -> list:
        '''
        Метод make_population() создает популяцию с использованием изменяющейся мутации.

        Returns:
            list: Список популяции.
        '''

        # Проходимся по каждому потомку
        for i in range(len(self._children_list)):
            child1 = self._children_list[i][0]
            child2 = self._children_list[i][1]  # Получаем потомков
            # Проходимся по каждой позиции потомка
            for j in range(len(child1)):
                # С вероятностью, определенной _probabilities_mutation[i], меняем значение гена на противоположное
                if randint(0, 100) <= self._probabilities_mutation[i] * 100:
                    child1[j] = '0' * (child1[j] == '1') + \
                        '1' * (child1[j] == '0')
            for j in range(len(child2)):
                # С вероятностью, определенной _probabilities_mutation[i], меняем значение гена на противоположное
                if randint(0, 100) <= self._probabilities_mutation[i] * 100:
                    child2[j] = '0' * (child2[j] == '1') + \
                        '1' * (child2[j] == '0')
            # Добавляем потомка в список выбранной популяции
            self._selected_population.append(child1)
            self._selected_population.append(child2)

        return self._selected_population  # Возвращаем список выбранной популяции


if __name__ == "__main__":
    for i in range(100):
        arr = []
        for i in range(100):
            arr.append(
                (list(bin(randint(16, 31))[2:]), list(bin(randint(16, 32))[2:]), list(bin(randint(16, 31))[2:]), list(bin(randint(16, 31))[2:])))
            x = ChangingMutator(arr, 0.6)
            x.make_mutation()
