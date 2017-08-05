# Ask the user for a number and determine whether the number is prime or not.

prime = int(input("Enter a number. I'll determine if it's prime: "))

l = []

for i in range(1,prime):
    if prime % i == 0:
        l.append(i)

if len(l) < 2:
    print("The number is prime!")