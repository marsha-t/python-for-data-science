import sys


def is_even(number):
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def parse_argument():
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 1:
        return None
    try:
        return int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")


def main():
    try:
        number = parse_argument()
        if number is not None:
            is_even(number)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
