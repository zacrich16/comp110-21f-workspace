"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730408740"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# assign variables
fortune: int = randint(1, 4)

# create if/else conditionals
print("Your fortune cookie says...")
if fortune == 1:
    print("A breeze will blow only on the hottest of days.")
else:
    if fortune == 2:
        print("You are as bright as the ocean is deep.")
    else:
        if fortune == 3:
            print("Big things are coming your way sooner than you realize.")
        else:
            print("Live life to the fullest!")
print("Now, go spread positive vibes!")