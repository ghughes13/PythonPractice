# Cows and Bulls Number Guessing Game. The game works like this:
# Computer randomly generates a 4-digit number. You guess a number. For every digit that you guessed correctly in
# the correct place, you have a “cow”. For every digit you guessed correctly in the wrong place you get a “bull.”
# Once you guess the correct number, the game is over.

import random


def cows_and_bulls():
    cows = 0
    bulls = 0
    guess_count = 1
    print("Guess a 4 digit number!")
    random_num = str(random.randint(1000, 9999))
    print(random_num)
    while True:
        user_guess = input("Guess {}: ".format(guess_count))
        guess_count += 1
        for i in user_guess:
            if i in random_num:
                bulls += 1
        if random_num[0] == user_guess[0]:
            cows += 1
            bulls -= 1
        if random_num[1] == user_guess[1]:
            cows +=1
            bulls -=1
        if random_num[2] == user_guess[2]:
            cows += 1
            bulls -=1
        if random_num[3] == user_guess[3]:
            cows += 1
            bulls -=1
        print("You have {} cows.".format(cows))
        print("You have {} bulls.".format(bulls))
        if cows == 4:
            break
        else:
            bulls = 0
            cows = 0
    print("You got 4 cows! You win!!")
    print(random_num)

cows_and_bulls()
