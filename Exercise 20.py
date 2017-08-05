# Binary Search Algorythm


looking_for = int(input("What number do we need to check? "))
l = [i for i in range(0, 5000)]


def binary_search():
    copy = l[:]
    while len(copy) != 1:
        if copy == [looking_for]:
            print(copy)
        elif copy[int(round(len(copy)/2))] <= looking_for:
            copy = copy[int(round(len(copy)/2)):]
            print(copy)
        elif copy[int(round(len(copy) / 2))] >= looking_for:
            copy = copy[:int(round(len(copy) / 2))]
            print(copy)
        else:
            pass
    if copy == [looking_for]:
        print("The number is in the list!")
    else:
        print("The number is not in the list!")


binary_search()
