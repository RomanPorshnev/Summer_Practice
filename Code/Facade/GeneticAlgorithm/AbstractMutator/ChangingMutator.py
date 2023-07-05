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
            child = self._children_list[i][0]  # Получаем потомка
            # Проходимся по каждой позиции потомка
            for j in range(len(child)):
                # С вероятностью, определенной _probabilities_mutation[i], меняем значение гена на противоположное
                if randint(0, 100) <= self._probabilities_mutation[i] * 100:
                    child[j] = '0' * (child[j] == '1') + '1' * (child[j] == '0')

            # Добавляем потомка в список выбранной популяции
            self._selected_population.append(child)

        return self._selected_population  # Возвращаем список выбранной популяции
