import random

a = range(1,random.randint(1,99))
b = range(1,random.randint(1,99))

for i in a:
    if i in b:
        print(i)