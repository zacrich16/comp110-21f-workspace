"""Drawing forests in a loop."""

__author__ = "730408740"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
i = 1
counter = 1

# print nothing if input is less than or equal to zero
if depth <= 0:
    i = depth + 1
else:
    while i <= depth:
        print(TREE * i)
        i = i + 1