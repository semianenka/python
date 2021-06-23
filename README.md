# GIT


# Task 0

- Try to use **checkout** to make branches and switch between them.

- Try to use remote repo with commands: **push, pull, merge, merge --squash**

- Find a way how you could use **stash** in your workflow.

- Read https://womanonrails.com/replace-parent-branch and solve problem with a wrong parent branch. 

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

- Check "Code smell" by Robert Martin or https://refactoring.guru/ru/refactoring/smells 

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
