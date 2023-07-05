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
            list: Список потомков + родители.
        '''

        # Получаем количество пар родителей
        len_pairs = len(self._parents_pairs)
        # Получаем длину хромосомы
        len_chromosome = len(self._parents_pairs[0][0])

        # Проходимся по парам родителей
        for i in range(len_pairs):
            self._selected_children.append(
                (self._parents_pairs[i][0].copy(), self._parents_pairs[i][1].copy()))
            if randint(0, 100) <= (self._changing_probability * 100):
                # Проходимся по каждой позиции хромосомы
                for j in range(len_chromosome):
                    # С вероятностью, определенной _crossing_probability, меняем значения генов местами
                    if randint(0, 100) <= (self._crossing_probability * 100):
                        try:
                            self._selected_children[i][0][j], self._selected_children[i][1][
                                j] = self._parents_pairs[i][1][j], self._parents_pairs[i][0][j]
                        except:
                            print(j,len(self._parents_pairs[i][1]))

            # Добавляем ребенка и его родителей в список потомков
            self._selected_children[i] = (
                self._selected_children[i][0], self._selected_children[i][1], self._parents_pairs[i][0], self._parents_pairs[i][0])

        return self._selected_children  # Возвращаем список выбранных потомков


if __name__ == "__main__":
    for i in range(100):
        arr = []
        for i in range(100):
            arr.append(
                (list(bin(randint(16, 31))[2:]), list(bin(randint(16, 32))[2:])))
            x = HomogeneousRecombinator(arr, 0.6, 0.8)
            x.make_children()
