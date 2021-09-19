""" Numeric Operators, Zachary Richardson."""


left: str = input("What is the Left-hand side? ")
right: str = input("What is the Right-hand side? ")
print("Left-hand side: ", left)
print("Right-hand side: ", right)
print(left, "**", right, "is", int(left) ** int(right))
print(left, "/", right, "is", int(left) / int(right))
print(left, "//", right, "is", int(left) // int(right))
print(left, "%", right, "is", int(left) % int(right))