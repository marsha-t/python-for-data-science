import sys
from ft_filter import ft_filter


def check_arguments():
    """
    Validate command-line arguments

    Returns:
        tuple[str, int]:
            Validated input string and integer threshold

    Raises:
        AssertionError:
            - number of arguments incorrect
            - second argument can't be converted to int
            - characters in first argument is not alphanumeric nor space
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    try:
        number = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    if not all(c.isalnum() or c.isspace() for c in sys.argv[1]):
        raise AssertionError("the arguments are bad")
    return (sys.argv[1], number)


def main():
    """
    Filter and display words longer than given length

    Raises:
        AssertionError:
            - if program arguments are invalid

    """
    # TODO add docstring
    try:
        text, number = check_arguments()
        words = text.split()
        long_words = ft_filter(lambda word: len(word) > number, words)
        print(long_words)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return


if __name__ == "__main__":
    main()
