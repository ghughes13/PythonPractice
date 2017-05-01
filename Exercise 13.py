def fibbonacci():
    amt = int(input("How many fibbonacci numbers do you want to generate? "))
    lst = [1]
    fibbonacci = 1
    previous = 1
    while True:
        lst.append(fibbonacci)
        new_previous = fibbonacci + previous
        previous = fibbonacci
        fibbonacci = new_previous
        if len(lst) == amt:
            print(lst)
            break

fibbonacci()

