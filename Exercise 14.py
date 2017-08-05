#Write two different functions to do this - one using a loop and constructing a list, and another using sets.

numbers = [1,1,2,2,3,3,4,5,6]


def loop_function(thing):
    copy = []
    for i in thing:
        if i not in copy:
            copy.append(i)
    print(copy)


def set_function(thing):
    new = set()
    new.update(numbers)
    print(new)

loop_function(numbers)
set_function(numbers)