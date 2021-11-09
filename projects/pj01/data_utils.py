"""Utility functions."""

__author__ = "730408740"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result

    
def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Visualize the first N rows of data in a table."""
    result: dict[str, list[str]] = {}
    for column in table:
        items: list[str] = []
        for row in range(N):
            items.append(table[column][row])
        result[column] = items
    return result


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Create a new table with only desired columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = table[column]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column-based tables into one."""
    result: dict[str, list[str]] = {}
    for column in a:
        result[column] = a[column]
    for column in b:
        if column in result:
            result[column] = a[column] + b[column]
        else:
            result[column] = b[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Create a dictionary with a value and its frequency in a table."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result