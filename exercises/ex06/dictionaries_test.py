"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730408740"


def test_invert_empty() -> None:
    """Test invert with an empty dictionary."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_single() -> None:
    """Test invert with a single key-value pair."""
    xs: dict[str, str] = {"a": "b"}
    assert invert(xs) == {"b": "a"}


def test_invert_multiple() -> None:
    """Test invert with multiple key-value pairs."""
    xs: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(xs) == {"b": "a", "d": "c"}


def test_favorite_color_empty() -> None:
    """Test favorite_color with empty list."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_favorite_color_multiple() -> None:
    """Test favorite_color with multiple color entries."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_equal() -> None:
    """Test favorite color if two colors are equally favorited."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue"}
    assert favorite_color(colors) == "yellow"


def test_count_empty() -> None:
    """Test count with an empty list."""
    items: list = []
    assert count(items) == {}


def test_count_single_value() -> None:
    """Test count with one value in the list."""
    items: list = ["one"]
    assert count(items) == {"one": 1}


def test_count_multiple_values() -> None:
    """Test count with multiple values in the list."""
    items: list = ["one", "two", "two"]
    assert count(items) == {"one": 1, "two": 2}