# What year you turn 100. ----- DONE

name = input("What's your name? ")
age = int(input("How old are you? "))
how_many = int(input("How many times would you like to print the message? "))
year_one_hundred = (100-age)+2017
print("Hey {}. You'll turn 100 in the year {}. \n".format(name, year_one_hundred) * how_many)

