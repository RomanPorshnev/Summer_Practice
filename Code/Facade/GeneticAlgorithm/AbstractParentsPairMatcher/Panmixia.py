from AbstractParentsMatcher import *


class Panmixia(AbstractParentsMatcher):
    '''
    Panmixia - класс, наследующийся от AbstractParentsMatcher.
    Он реализует метод make_parents_pairs() для создания пар родителей с помощью панмиксии.
    '''

    def make_parents_pairs(self) -> list:
        '''
        Метод make_parents_pairs() создает пары родителей с использованием панмиксии.

        Returns:
            list: Список пар родителей.
        '''

        len_parents = len(self._parents)  # Получаем количество родителей

        # Проходимся по каждому родителю
        for i in range(len_parents):
            pair = randint(0, len_parents - 1)  # Выбираем случайного партнера для родителя
            self._parents_pairs.append((self._parents[i], self._parents[pair]))  # Добавляем пару родителей в список

        return self._parents_pairs  # Возвращаем список пар родителей
