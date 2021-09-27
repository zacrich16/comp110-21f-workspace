"""List utility functions."""

__author__ = "730408740"


def all(a: list[int], b: int) -> bool:
    if len(a) == 0:
        return False
    else:
        i = 0
        counter = 0
        while i < len(a):
            if a[i] == b:
                counter += 1
            i += 1
    if counter == len(a):
        return True
    else:
        return False


def is_equal(a: list[int], b: list[int]) -> bool:
    if len(a) != len(b):
        return False
    i = 0
    counter = 0
    while i < len(a) and len(b):
        if a[i] == b[i]:
            counter += 1
        i += 1
    if counter == len(a) and len(b):
        return True
    else:
        return False


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    i = 0
    value = 0
    while i < len(input):
        if input[i] > value:
            value = input[i]
        i += 1
    return value