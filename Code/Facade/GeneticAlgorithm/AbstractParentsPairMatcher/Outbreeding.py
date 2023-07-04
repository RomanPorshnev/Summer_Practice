from AbstractParentsMatcher import *
import random


class Outbreeding(AbstractParentsMatcher):
    '''
    Данный метод формирует и возвращает пары родителей, сформированные по принципу аутбридинга
    Выходные данные: список кортежей (родитель1, родитель2)
    '''

    def make_parents_pairs(self):
        while len(self._parents) != 1:
            index_of_first_parent = random.randint(0, len(self._parents) - 1)
            first_parent = self._parents[index_of_first_parent]
            min_hamming_distance = 0
            index_of_second_parent = 0
            for i in range(len(self._parents)):
                hamming_distance = self._hamming_distance(first_parent, self._parents[i])
                if hamming_distance >= min_hamming_distance:
                    min_hamming_distance = hamming_distance
                    index_of_second_parent = i
            self._parents_pairs.append((first_parent, self._parents[index_of_second_parent]))
            self._parents.pop(index_of_first_parent)
        return self._parents_pairs


if __name__ == "__main__":
    arr = [['0', '0', '0'], ['0', '1', '1'], ['0', '0', '1'], ['1', '0', '0'], ['1', '0', '0'],
           ['1', '0', '1'], ['1', '1', '0']]
    out_breeding = Outbreeding(arr)
    print(len(out_breeding.make_parents_pairs()))
