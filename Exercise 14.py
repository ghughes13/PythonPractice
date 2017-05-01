NOT DONE

#Write two different functions to do this - one using a loop and constructing a list, and another using sets.

numbers = [1,1,2,2,3,3,4,5,6]


def fair(thing):
    copy = []
    for i in thing:
        if i not in copy:
            copy.append(i)
    print(copy)

fair(numbers)