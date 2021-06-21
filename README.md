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

Note: Use separate file for each task.


# Python


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


