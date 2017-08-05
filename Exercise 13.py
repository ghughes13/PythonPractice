def fibonacci():
    amt = int(input("How many fibonacci numbers do you want to generate? "))
    lst = [1]
    fibonacci = 1
    previous = 1
    while True:
        lst.append(fibonacci)
        new_previous = fibonacci + previous
        previous = fibonacci
        fibonacci = new_previous
        if len(lst) == amt:
            print(lst)
            break

fibonacci()

