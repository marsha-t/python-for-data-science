from typing import Any


def callLimit(limit: int):
    """
    Return a decorator that limits number of function calls

    Args:
        limit (int):
            Maximum number of allowed function calls

    Returns:
        callable:
            Decorator function
    """
    count = 0

    def callLimiter(function):
        """
        Decorate a function with a call limit

        Args:
            function:
                Function to decorate

        Returns:
            callable:
                Wrapped function with call limitation
        """

        def limit_function(*args: Any, **kwds: Any):
            """
            Execute function while under the
            allowed call limit

            Args:
                *args:
                    Positional arguments passed to
                    the original function

                **kwds:
                    Keyword arguments passed to
                    the original function

            Returns:
                Any | None:
                    Result of wrapped function or None
                    if call limit is exceeded.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
