def square(x: int | float) -> int | float:
    """
    Return the square of a number

    Args:
        x (int | float):
            Number to square

    Returns:
        int | float:
            Squared value of x
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Return a number raised to itself

    Args:
        x (int | float):
            Number used as both base and exponent

    Returns:
        int | float:
            Result of x raised to the power x
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Return a function that repeatedly applies a function
    to a stored value

    Args:
        x (int | float):
            Initial value

        function:
            Function applied to x

    Returns:
        object:
            Inner function maintaining state
    """
    count = 0

    def inner() -> float:
        """
        Apply the stored function to x and return result

        Returns:
            float:
                Updated value after function application
        """
        nonlocal x, count
        x = function(x)
        count += 1
        return x
    return inner
