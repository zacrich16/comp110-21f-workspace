"""An exercise in remainders and boolean logic."""

__author__ = "730408740"


num: int = int(input("Enter an int: "))

if num % 2 == 0:
    if num % 7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if num % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")