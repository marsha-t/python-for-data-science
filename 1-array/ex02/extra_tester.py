from load_image import ft_load


def test_case(description, path):
    print(f"\n--- {description} ---")

    result = ft_load(path)

    print(result)
    print(type(result))


def main():

    print("\n===== VALID TEST =====")

    test_case(
        "Valid JPG image",
        "landscape.jpg"
    )

    test_case(
        "Uppercase extension",
        "LANDSCAPE.JPG"
    )

    print("\n===== INVALID INPUT TESTS =====")

    test_case(
        "File does not exist",
        "missing.jpg"
    )

    test_case(
        "Wrong extension",
        "image.png"
    )

    test_case(
        "Path is not string",
        42
    )

    test_case(
        "Empty string path",
        ""
    )

    test_case(
        "Fake JPG file",
        "fake.jpg"
    )


if __name__ == "__main__":
    main()