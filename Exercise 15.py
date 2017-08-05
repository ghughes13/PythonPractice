words = "My name is Michele"


def reverse(string):
    string = string.split(" ")
    string = string[::-1]
    print(" ".join(string))

reverse(words)
