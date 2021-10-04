"""List utility functions part 2."""

__author__ = "730408740"

# Define your functions below


def only_evens(a: list[int]) -> list[int]:
    """Create new list of only even values from input list."""
    i = 0
    evens: list[int] = []
    while i < len(a):
        if a[i] % 2 == 0:
            evens.append(a[i])
        i += 1
    return evens


def sub(a: list[int], i: int, j: int) -> list[int]:
    """Create subset list of defined indices."""
    sub_list: list[int] = []
    if i < 0:
        i = 0
    if j > len(a):
        j = len(a)
    if len(a) == 0 or i > len(a) or j <= 0:
        return sub_list
    while i < j:
        sub_list.append(a[i])
        i += 1
    return sub_list


def concat(a: list[int], b: list[int]) -> list[int]:
    """Concatenate two lists together."""
    a_plus_b: list[int] = []
    i = 0
    while i < len(a):
        a_plus_b.append(a[i])
        i += 1
    i = 0
    while i < len(b):
        a_plus_b.append(b[i])
        i += 1
    return a_plus_b