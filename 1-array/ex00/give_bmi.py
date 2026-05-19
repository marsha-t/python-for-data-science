import numpy as np

def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate BMI values from height and weight lists

    Args:
        height (list[int | float]):
            list of heights in meters
        weight (list[int | float]):
            list of weights in kilograms

    Returns:
        (list[int | float]):
            list containing BMI values

    Raises:
        TypeError:
            - inputs are not lists
            - either list is not made of numbers
        ValueError:
            - lists are of different lengths
            - heights or weights are 0 or negative
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Inputs must be lists")
    if len(height) != len(weight):
        raise ValueError("Heights and weights are of different lengths")
    if not all(
        isinstance(h, (int, float)) and not isinstance(h, bool) for h in height
    ):
        raise TypeError("Not all height values are numbers")
    if not all(
        isinstance(w, (int, float)) and not isinstance(w, bool) for w in weight
    ):
        raise TypeError("Not all weight values are numbers")
    if any(h <= 0 for h in height):
        raise ValueError("Heights must be positive")
    if any(w <= 0 for w in weight):
        raise ValueError("Weights must be positive")

    np_height = np.array(height)
    np_weight = np.array(weight)
    bmi = np_weight / (np_height ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Identify BMI values that are above a given limit

    Args:
        bmi (list[int | float]):
            list of BMI values
        limit (int):
            limit used for comparison

    Returns:
        (list[bool]):
            list identifying BMI values that are above the limit

    Raises:
        TypeError:
            - BMI input is not a list
            - Limit is not an int
            - BMI values are not all numbers
    """

    if not isinstance(bmi, list):
        raise TypeError("BMI input must be a list")
    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("Limit must be an int")
    if not all(
        isinstance(b, (int, float)) and not isinstance(b, bool) for b in bmi
    ):
        raise TypeError("Not all BMI values are numbers")

    np_bmi = np.array(bmi)
    return (np_bmi > limit).tolist()
