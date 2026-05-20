import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice 2D array and print shapes

    Args:
        family (list[list[int | float]]):
            2D array of numeric values
        start (int):
            start of slice
        end (int):
            end (not inclusive) of slice

    Returns:
        list[list[int | float]]:
            sliced 2D array as nested Python lists

    Raises:
        TypeError:
            - family is not a list or is not 2D
            - family contains non-numeric values
            - start or end are not int
        ValueError:
            - family is empty
            - family rows are of different length
    """
    if not isinstance(family, list):
        raise TypeError("family is not a list")
    if not family:  # len(family) == 0
        raise ValueError("family is empty")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family is not a 2D array")
    if not all(len(row) == len(family[0]) for row in family):
        raise ValueError("Rows are not the same length")
    if not all(
        isinstance(value, (int, float)) 
        and not isinstance(value, bool) 
        for row in family 
        for value in row
    ):
        raise TypeError("Array contains non-numeric values")
    if not isinstance(start, int) or isinstance(start, bool):
        raise TypeError("start is not an int")
    if not isinstance(end, int) or isinstance(end, bool):
        raise TypeError("end is not an int")

    np_family = np.array(family)
    print(f"My shape is : {np_family.shape}")
    new_array = np_family[start:end]
    print(f"My new shape is : {new_array.shape}")
    return new_array.tolist()
