# Prints all divisible numbers in the number you give it

num = int(input("Enter a number: "))

for i in range(1, num):
    if num % i == 0:
        print(i)
