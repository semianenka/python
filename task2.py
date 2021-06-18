from copy import deepcopy
from functools import partial

list_of_tuples = [(1, "Python"), (1, "Lua"), (3, "Swift"), (3, "C"), (2, "Elm"), (2, "JS"), (3, "Rust")]


def sort_by_first_low_second_alpha(list_):
    new_list = deepcopy(list_)
    new_list.sort(key=lambda tuple_: (tuple_[0], tuple_[1]))
    return new_list


def mean():
    enclosed_list = []

    def get_mean(number=0):
        nonlocal enclosed_list
        enclosed_list.append(number)
        mean_ = sum(enclosed_list) / len(enclosed_list)
        return mean_
    return get_mean


m = mean()


def power(exp, base):
    return base ** exp


square = partial(power, 2)
cube = partial(power, 3)


class CustomIterator:
    def __init__(self, collection):
        self.collection = collection
        self.cursor = 0

    def __next__(self):
        if self.cursor + 1 >= len(self.collection):
            raise StopIteration
        self.cursor += 1
        return self.collection[self.cursor]

    def __iter__(self):
        return self


print('Sort list of tuples by first element of tuple (from low to high) and second element sort alphabetically within '
      'a group\n', sort_by_first_low_second_alpha(list_of_tuples))
print('Create function to find mean value using closures\n', m(10), m(20))
print('Create functions to find squares and cubes using partial\n', square(10), cube(10))
print('Create custom iterator based on class magic methods __iter__ __next__')
for i in CustomIterator([1, 3, 6, 9, 12, 15]):
    print('', i)
