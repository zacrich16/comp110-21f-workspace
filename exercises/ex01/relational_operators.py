"""COMP 110 Relational Operators Assignment."""
__author__ = "730408740"

left: str = input("What is the Left-hand side? ")
right: str = input("What is the Right-hand side? ")
print(left, "<", right, "is", int(left) < int(right))
print(left, ">=", right, "is", int(left) >= int(right))
print(left, "==", right, "is", int(left) == int(right))
print(left, "!=", right, "is", int(left) != int(right))