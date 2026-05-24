from typing import Any


def get_mean(numbers: list[float]) -> float:
    """
    Return mean of numbers

    Args:
        numbers (list[float]):
            list of numbers

    Returns:
        float:
            mean
    """
    return sum(numbers) / len(numbers)


def get_median(numbers: list[float]) -> float:
    """
    Return median of numbers

    Args:
        numbers (list[float]):
            list of numbers

    Returns:
        float:
            median
    """
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 != 0:
        return sorted_numbers[n // 2]
    else:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2


def get_quartile(numbers: list[float]) -> list[float]:
    """
    Return 1st and 3rd quartiles of numbers

    Args:
        numbers (list[float]):
            list of numbers

    Returns:
        list[float]:
            1st and 3rd quartile respectively
    """
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    q1 = sorted_numbers[int(n * 0.25)]
    q3 = sorted_numbers[int(n * 0.75)]
    return [float(q1), float(q3)]


def get_variance(numbers: list[float]) -> float:
    """
    Return variance of numbers

    Args:
        numbers (list[float]):
            list of numbers

    Returns:
        float:
            variance
    """
    mean = get_mean(numbers)
    total = 0
    for number in numbers:
        total += (number - mean) ** 2
    return total / len(numbers)


def get_std(numbers: list[float]) -> float:
    """
    Return standard deviation of numbers

    Args:
        numbers (list[float]):
            list of numbers

    Returns:
        float:
            standard deviation
    """
    return get_variance(numbers) ** 0.5


def print_error(count: int) -> None:
    """
    Print ERROR count times

    Args:
        count (int):
            number of times to print ERROR
    """
    for _ in range(count):
        print("ERROR")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Print requested statistics from args

    Args:
        *args:
            Variable number of numeric values
        **kwargs:
            Requested statistics

    Notes:
        Prints error if
            - no args are given
            - not all numbers are given in args
    """
    numbers = list(args)

    if not numbers:
        print_error(len(kwargs))
        return
    if not all(
        isinstance(x, (int, float))
        and not isinstance(x, bool)
        for x in numbers
    ):
        print_error(len(kwargs))
        return

    operations = {
        "mean": get_mean,
        "median": get_median,
        "quartile": get_quartile,
        "std": get_std,
        "var": get_variance
    }
    for request in kwargs.values():
        if request in operations:
            result = operations[request](numbers)
            print(f"{request} : {result}")
