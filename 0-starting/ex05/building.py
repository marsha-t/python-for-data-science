import sys
import string


def count_char(text):
    """
    Counts different character types present in string

    Args:
        text (str): string to analyse

    Returns:
        dict[str, int]:
            dictionary containing counts for
                - uppercase letters
                - lowercase letters
                - punctuation characters
                - whitespace characters
                - digits
    """
    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "space": 0,
        "digit": 0
    }

    for c in text:
        if c.isupper():
            counts["upper"] += 1
        elif c.islower():
            counts["lower"] += 1
        elif c in string.punctuation:
            # string.punctuation = string of punctuation chars
            counts["punctuation"] += 1
        elif c.isspace():
            # Returns true for any whitespace character
            counts["space"] += 1
        elif c.isdigit():
            counts["digit"] += 1
    return counts


def get_input_text():
    """
    Validates command-line arguments and retrieves input text
    If no argument provided, prompts user for input through stdin

    Returns:
        str: text provided either through command-line arguments
            or standard input

    Raises:
        AssertionError:
            - more than one argument is provided
    """

    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    else:
        text = sys.argv[1]
    return text


def main():
    """
    Validates input arguments, counts character categories
    in provided text, and displays results

    Raises:
        AssertionError:
            - more than one argument is provided
    """

    try:
        text = get_input_text()
        counts = count_char(text)
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['space']} spaces")
        print(f"{counts['digit']} digits")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
