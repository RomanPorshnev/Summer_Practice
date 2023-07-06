from AbstractRecombinator import *

class SinglePointRecombinator(AbstractRecombinator):


    def make_children(self):
        for i in range(len(self._parents_pairs)):
            individual1 = self._parents_pairs[i][0].copy()
            individual2 = self._parents_pairs[i][1].copy()
            if randint(0,100) <= self._crossing_probability * 100:
                point = randint(1, len(individual1) - 1)
                individual1[point:], individual2[point:] = individual2[point:], individual1[point:]
                self._selected_children.append((individual1, individual2, self._parents_pairs[i][0], self._parents_pairs[i][1]))
        return self._selected_children
    


if __name__ == "__main__":
    for i in range(1):
        arr = []
        for i in range(5):
            arr.append(
                (list(bin(randint(16, 31))[2:]), list(bin(randint(16, 32))[2:])))
        x = SinglePointRecombinator(arr, 0.6, 0.8)
        print(x.make_children())
