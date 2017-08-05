# Password Generator

import random

strong = input("Would you like a [W]eak password or a [s]trong password? ").lower()


def pass_gen(strength):
    if strength == "w":
        words = ["blue", "school","apple","raindrop", "droptop", "rap","pants","sweet","drumph","fire","house","book"]
        print(words[random.randint(0,len(words))] + words[random.randint(0,len(words))])
    else:
        password = []
        while True:
            letters = "abcdefghijkslmnopqrstuvwxyz!@#$%^&*()1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if len(password) <= 10:
                password.append(letters[random.randint(0,73)])
            else:
                break
        print("".join(password))


pass_gen(strong)
