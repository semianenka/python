from functools import partial
from operator import itemgetter

list_of_tuples = [(1, "Python"), (1, "Lua"), (3, "Swift"), (3, "C"), (2, "Elm"), (2, "JS"), (3, "Rust")]


def sort_by_id_value(list_, rev_id=False, rev_value=False):
    return sorted(sorted(list_, key=itemgetter(1), reverse=rev_value), key=itemgetter(0), reverse=rev_id)


def mean():
    sum_, k = 0, 0

    def get_mean(number=0):
        nonlocal sum_, k
        sum_ += number
        k += 1
        mean_ = sum_/k
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


print(f'Sort list of tuples by first element of tuple (from low to high) and second element sort alphabetically within '
      f'a group:\n{sort_by_id_value(list_of_tuples)}')
print(f'Sort list of tuples by first element of tuple (from high to low) and second element sort alphabetically within '
      f'a group:\n{sort_by_id_value(list_of_tuples, rev_id=True)}')
print(f'Create function to find mean value using closures:\n{m(10)}, {m(20)}, {m(30)}')
print(f'Create functions to find squares and cubes using partial:\n', square(10), cube(10))
print(f'Create custom iterator based on class magic methods __iter__ __next__:')
for i in CustomIterator([1, 3, 6, 9, 12, 15]):
    print('', i)
