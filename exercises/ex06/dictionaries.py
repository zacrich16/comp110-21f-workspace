"""Practice with dictionaries."""

__author__ = "730408740"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Switch a dictionary's keys and values."""
    result: dict[str, str] = {}
    for key, value in xs.items():
        if value in result:
            raise KeyError("Cannot duplicate keys in a dictionary.")
        result[value] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Calculate the most frequently stated value in a dictionary."""
    numeric_dict: dict[str, int] = {}
    favorite: str = ""
    if colors == {}:
        return favorite
    for key, value in colors.items():
        if value in numeric_dict:
            numeric_dict[value] += 1
        else:
            numeric_dict[value] = 1
    favorite = max(numeric_dict, key=lambda key: numeric_dict[key])
    return favorite


def count(items: list[str]) -> dict[str, int]:
    """Count the number of times a value appears in a list and assign it to a key-pair value."""
    result: dict[str, int] = {}
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result