import random

a = {i for i in range(0,100,random.randint(1,10))}
b = {i for i in range(0,100,random.randint(1,10))}

print(a)
print(b)
print(a & b)