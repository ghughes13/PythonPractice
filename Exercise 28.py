# Determines the max number out of 3 you give without using max()

print("Give me 3 different numbers and I will tell you the largest: ")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

if num1 > num2 and num1 > num3:
    print("Number 1, {} is the largest of the three.".format(num1))
elif num2 > num1 and num2 > num3:
    print("Number 2, {} is the largest of the three.".format(num2))
else:
    print("Number 3, {} is the largest of the three.".format(num3))
