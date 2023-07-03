from AbstractRecombinator import *


class HomogeneousRecombinator(AbstractRecombinator):
    '''
    HomogeneousRecombinator - класс, наследующийся от AbstractRecombinator.
    Он реализует метод make_children() для создания потомков с помощью однородной рекомбинации.
    '''

    def make_children(self) -> list:
        '''
        Метод make_children() создает потомков с использованием однородной рекомбинации.

        Returns:
            list: Список потомков.
        '''

        # Получаем количество пар родителей
        len_pairs = len(self._parents_pairs)
        # Получаем длину хромосомы
        len_chromosome = len(self._parents_pairs[0][0])

        # Проходимся по парам родителей
        for i in range(len_pairs):
            # Преобразуем родителей в список символов
            self._parents_pairs[i] = list(
                self._parents_pairs[i][0]), list(self._parents_pairs[i][1])

            # Проходимся по каждой позиции хромосомы
            for j in range(len_chromosome):
                # С вероятностью, определенной _probability, меняем значения генов местами
                if randint(0, 100) < (self._probability * 100):
                    self._parents_pairs[i][0][j], self._parents_pairs[i][1][
                        j] = self._parents_pairs[i][1][j], self._parents_pairs[i][0][j]

            # Преобразуем детей обратно в строку и добавляем их в список потомков
            self._selected_children.append(''.join(self._parents_pairs[i][0]))
            self._selected_children.append(''.join(self._parents_pairs[i][1]))

        return self._selected_children  # Возвращаем список выбранных потомков
