# Generates a list of numbers from 0 to the number you give it ----- DONE

num = int(input("Enter the number: "))
new = []

for i in range(0, num):
    if i < num:
        new.append(i)

print(new)
