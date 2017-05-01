name = input("What's your name? ")
age = int(input("How old are you? "))
how_many = int(input("How many times would you like to print the message? "))
year_onehundred = (100-age)+2017
message = print("Hey {}. You'll turn 100 in the year {}. \n".format(name,year_onehundred) * how_many)

