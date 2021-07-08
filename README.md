# GIT


# Task 0

- Try to use **checkout** to make branches and switch between them.

- Try to use remote repo with commands: **push, pull, merge, merge --squash**

- Find a way how you could use **stash** in your workflow.

- [Read](https://womanonrails.com/replace-parent-branch) and solve problem with a wrong parent branch. 

Use **rebase --onto** to change the parent branch for Task2 to the master.

Actual
```
                / Task2
        / Task1
master 
```
Expected
```
        / Task1
master 
        \ Task2
```
What happen if after **rebase** you push code into existing remote branch?


- Use **cherry-pick** to solve problem with the wrong parent branch.



# Python

Use separate file/folder for each task.

# Task 1

- Find the second by length string in a list or array

- Sort list by string length

- Sort list by count of vowels in string

- Sort list by count of consonants in string (modify previous function)

- Change by places first and last letters in each second string of list

- Revert strings of list

- Read about [LEGB](https://realpython.com/python-scope-legb-rule/)

# Task 2 

- Sort list of tuples by first element of tuple (from low to high) and second element sort alphabetically within a group

[(1, "Python"), (1, "Lua"), (3, "Swift"), (3, "C"), (2, "Elm"), (2, "JS"), (3, "Rust")]

- Sort list of tuples by first element of tuple (from high to low) and second element sort alphabetically within a group

[(1, "Python"), (1, "Lua"), (3, "Swift"), (3, "C"), (2, "Elm"), (2, "JS"), (3, "Rust")]


- Create function to find mean value using closures

``` python
def mean():
    pass

m = mean()
```

``` bash
m(10)
>>> 10
m(20)
>>> 15
```

Hint: it is about using enclosed variables and nested functions

- Create functions to find squares and cubes using partial

``` python
from functools import partial

def power(exp, base):
    pass
```

- Create custom iterator based on class magic methods  ```__iter__ __next__```

# Task 3

- Transpose a matrix 

- Turn a matrix on 90 degrees clockwise

- Multiply matrixes


- Create a simple calculator with at least 4 functions: addition, subtraction, multiplying, division. Use console input/output.

Use library argparse to work with CL arguments

- Check "Code smell" by Robert Martin or [refactoring](https://refactoring.guru/ru/refactoring/smells)

# Task 4

You have two lists. Order is important.

used = [1, 3, 2, 4, 3]
dirty_input = [1, 3, 2, 2, 4, 3, 3, 3]

Remove **used** values from **dirty_input**.

- Create dictionary

keys = ['C', 'Lua', 'Python']
values = [1972, 1993, 1990]

- Merge dictionaries

langs1 = {'C': 1972, 'Lua': 1993, 'Python': 1990}
langs2 = {'Lisp': 1958, 'Scheme': 1975}

- Swap key and values in dictionary using dictionary comprehension.

langs = {'C': 1972, 'Lua': 1993, 'Python': 1990}

- Exceptions

Use [prize.json.zip](https://github.com/semianenka/python/files/6699192/prize.json.zip) 

CSV
Deserialize data from the file to python object and save it to CSV file.
Every action should be done in a separate function.
One person - one row for CSV.
CSV file should have column headers in first line.

YAML
Load CSV file to a python object and save it to YAML file.
Every action should be done in a separate function.
YAML structure should correspond to the original JSON.

Add **exceptions** blocks to handle exceptional cases where it is necessary. 
Store exceptions classes in separate file

- [Big O](https://www.google.com/amp/s/tproger.ru/translations/data-structure-time-complexity-in-python/amp/)

# Task 5

- Implement decorator function to add >>> to every function call.

- Implement decorator function to show executing time.

- Combine decorators to chain.

- Implement decorator as class and store cache as an attribute. Store pairs {arg: result} as a dictionary in an attribute of the class object.

```python
def fibonacci_numbers(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)
```

- Try to use [pdb](https://docs.python.org/3/library/pdb.html) module to debug. Sometimes it faster than PyCharm debugger.
```python
import pdb
pdb.set_trace()
```

# Task 6

You need to implement a file reader which reads files line by line. File list is defined on using command line arguments(in sys.argv). After displaying each line, the program waits for user's input. The user is available to:

- press Enter to read the next line
- press n and Enter to skip the rest of the current file and start reading the next file
- press anything else and Enter to display the next line

Function which displays lines and queries the user for input is already implemented.

```python
class SkipThisFile(Exception):
   r"Tells the generator to jump to the next file in list."
   pass

def display_files(*files):
    source = read_lines(*files)
    for line in source:
        print(line, end='')
        inp = input()
        if inp == 'n':
            print('NEXT')
            source.throw(SkipThisFile) # return value is ignored
```

Implement generator read_lines which is passed a list of files to read during construction.
Generator should yield line after line from the first file, then from the second, and so on.
When the last file is read, it stops.
User of the generator can also throw an exception into the generator (SkipThisFile) which signals the generator to skip the rest of the current file, and just yield a dummy value to be skipped.

Note: Make sure that implemented function is correct. I don't check this legacy code :-).

# Task 7

- SOLID
- Write you own examples. Try to show in code what every rule mean.

# Task 8

Design object oriented model for **Airline**.

Use: classes, inheritance, interfaces, polymorphism, encapsulation.
Each class, method, and variable must have a meaningful name and informative composition.
You need to think carefully about which classes are needed to solve the problem.
Inheritance should only be applied when it makes sense.
Each class should have the fields and methods you deem necessary.

Working with the console should be minimal (only the necessary data for input, output only what is requested in the problem statement).
The program must create objects of various classes in the selected subject area, combine them into a set of objects (use collections).

- Determine the aircraft hierarchy.
- Create an airline.
- Calculate the total capacity and lifting capacity.
- Sort the company's aircraft by range.
- Find an aircraft in the company that matches the specified range of parameters.

# Task 9 

Logger

Implement a simple class with 3 methods: 1st raising exception, 2nd returning None and 3rd returning 'Hello, {name}!' where name is an argument

- Implement a metaclass to log all the method calls
- Logging should have 3 levels: error, info and warning
- Use info level to log the method call itself with arguments
- Use error level to log the exceptions raised during the method
- Use warning level to log a warning if method call returned None

- Implement logging to command line, file and sqllite db

# Task 10

[async/await](https://realpython.com/async-io-python/)

Compare two examples

```python
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```

```python
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```

AmazonHub

Simulate process of items searching.

Use async/await functions.

- Use class AmazonHub

- Implement async func process and private func _searcher

- Show time of execution


``` python

orders = {'Crime and Punishment by Fyodor Dostoevsky': 4, 'Harry Potter (all books)': 1, 'Star Wars IV': 2}

class AmazonHub:
    def __init__(self):
        self.orders = {}
        self._items = []

    @property
    def items(self):
        return self._items

    def add(self, orders):
        self.orders = {**self.orders, **orders}

    def run(self):
        pass

    async def _search(self, order, minutes):
        pass

    async def process(self):
        pass

```

Expected Output

New order: Star Wars IV

New order: Crime and Punishment by Fyodor Dostoevsky

New order: Harry Potter (all books)

Harry Potter (all books) - Done

Star Wars IV - Done

Crime and Punishment by Fyodor Dostoevsky - Done

Items: ['Harry Potter (all books)', 'Star Wars IV', 'Crime and Punishment by Fyodor Dostoevsky']

[task10.py] executed in 4.00 seconds.
