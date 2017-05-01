# Number guessing game

import random

count = 0


def gen_number():
    global number
    number = random.randint(0,9)
    print(number)
    get_guess()


def get_guess():
    global num
    num = input("Guess a number: ")
    global count
    count += 1
    if num == 'exit':
        pass
    else:
        num = int(num)
        number_game()


def number_game():
        if num == number:
            print("That's it! You win!")
            print("It took you {} guesses.".format(count))
            print("Starting new game...")
            gen_number()
            get_guess()
        elif num < number:
            print("That's to low. Try again. ")
            get_guess()
        elif num > number:
            print("That's to high! Try again. ")
            get_guess()

gen_number()