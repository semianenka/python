import time


def output(func):
    def wrapper(*args, **kwargs):
        print('>>> ', end='')
        return func(*args, **kwargs)
    return wrapper


def timed(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        print(f'Function {func.__name__} was finished in {time.time() - t1}s')
        return func(*args, **kwargs)
    return wrapper


class StoreResults:
    def __init__(self, func):
        self.func = func
        self.results = {}

    def __call__(self, *args, **kwargs):
        if args[0] in self.results:
            return self.results[args[0]]
        result = self.func(*args, **kwargs)
        self.results[args[0]] = result
        return result

    def cache(self):
        return self.results


@timed
@output
def some_func(a=2, b=2):
    return a + b


@StoreResults
def fibonacci_numbers(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)


print(some_func())
print(fibonacci_numbers(16))
print(fibonacci_numbers(32))
print(fibonacci_numbers(4))
print(fibonacci_numbers(31))
print(fibonacci_numbers(32))
print(fibonacci_numbers.cache())
