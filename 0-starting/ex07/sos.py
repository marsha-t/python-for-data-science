import sys


def convert_to_morse(c):
    """
    Convert character into Morse representation

    Args:
        c (str):
            character to convert (alphanumeric or space)

    Returns:
        str:
            Morse representation
    """
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    return NESTED_MORSE[c]


def check_arguments():
    """
    Validate command-line arguments

    Raises:
        AssertionError:
            - number of arguments incorrect
            - character in first argument is not alphanumeric nor space
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    if not all(c.isalnum() or c == " " for c in sys.argv[1]):
        raise AssertionError("the arguments are bad")


def main():
    """
    Validate input arguments and convert string into Morse code

    Raises:
        AssertionError:
            - if program arguments are invalid
    """
    try:
        check_arguments()
        print(" ".join(convert_to_morse(c.upper()) for c in sys.argv[1]))
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
