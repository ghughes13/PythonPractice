num = int(input("Give me a number: "))

if num % 4 == 0:
    print("THIS IS THE NUMBER I'VE BEEN WAITING FOR!! \n")
elif num % 2 == 0:
    print("This number is even. \n")
else:
    print("This number is odd. \n")

check = int(input("Give me a second number: "))

if num % check == 0:
    print("The first number you gave me is evenly divisible by the second. ")
else:
    print("The first number is not evenly divisible by the second. ")