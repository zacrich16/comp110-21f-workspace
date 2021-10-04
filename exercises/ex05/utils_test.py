"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730408740"


def test_only_evens_empty() -> None:
    """Test only_evens with empty list."""
    a: list[int] = []
    assert only_evens(a) == []


def test_only_evens_one_item() -> None:
    """Test only_evens with one even and odd item."""
    a: list[int] = [1, 2]
    assert only_evens(a) == [2]


def test_only_evens_multiple_items() -> None:
    """Test only_evens with multiple even and odd items."""
    a: list[int] = [1, 2, 3, 4]
    assert only_evens(a) == [2, 4]


def test_sub_empty() -> None:
    """Test sub with empty list."""
    a: list[int] = []
    i: int = 1
    j: int = 3
    assert sub(a, i, j) == []


def test_sub_i_less_0() -> None:
    """Test sub if i < 0."""
    a: list[int] = [1, 2, 3, 4]
    i: int = -1
    j: int = 3
    assert sub(a, i, j) == [1, 2, 3]


def test_sub_j_greater_len() -> None:
    """Test sub if j > length of the list."""
    a: list[int] = [1, 2, 3, 4]
    i: int = 1
    j: int = 5
    assert sub(a, i, j) == [2, 3, 4]


def test_sub_normal_list() -> None:
    """Test sub if j !> length of the list, i !< 0, and the list is not empty."""
    a: list[int] = [1, 2, 3, 4]
    i: int = 1
    j: int = 3
    assert sub(a, i, j) == [2, 3]


def test_concat_empty_lists() -> None:
    """Test concat if both lists are empty."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []


def test_concat_one_empty() -> None:
    """Test concat if one list is empty."""
    a: list[int] = [1, 2, 3]
    b: list[int] = []
    assert concat(a, b) == [1, 2, 3]


def test_concat_two_lists() -> None:
    """Test concat if both lists have multiple values."""
    a: list[int] = [1, 2, 3]
    b: list[int] = [4, 5, 6]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6]