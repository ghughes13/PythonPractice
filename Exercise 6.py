#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

a = "Hello"
b = "Goodbye"
c = "Racecar"

def palindrome(word):
    forward = word
    backward = word[::-1]
    if forward.lower() == backward.lower(): print("This word is a palindrome.")
    else: print("This word is not a palindrome")

palindrome(a)
palindrome(b)
palindrome(c)