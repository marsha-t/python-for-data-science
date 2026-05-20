from give_bmi import give_bmi, apply_limit


def test_bmi_case(description, height, weight):
    print(f"\n--- {description} ---")

    try:
        result = give_bmi(height, weight)
        print(result)
        print(type(result))

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def test_limit_case(description, bmi, limit):
    print(f"\n--- {description} ---")

    try:
        result = apply_limit(bmi, limit)
        print(result)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def main():
    print("\n===== VALID BMI TESTS =====")

    test_bmi_case(
        "Empty lists",
        [],
        []
    )
    bmi = give_bmi([], [])

    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    test_bmi_case(
        "Valid BMI calculation",
        height,
        weight
    )

    bmi = give_bmi(height, weight)

    print("\n===== VALID LIMIT TESTS =====")

    test_limit_case(
        "Valid limit test",
        bmi,
        26
    )

    test_limit_case(
        "Limit with no matches",
        bmi,
        100
    )

    test_limit_case(
        "Limit with all matches",
        bmi,
        1
    )

    print("\n===== INVALID BMI INPUT TESTS =====")

    test_bmi_case(
        "Height is not a list",
        "hello",
        weight
    )

    test_bmi_case(
        "Weight is not a list",
        height,
        "hello"
    )

    test_bmi_case(
        "Different list lengths",
        [1.80],
        [70, 80]
    )

    test_bmi_case(
        "Height contains string",
        [1.80, "bad"],
        [70, 80]
    )

    test_bmi_case(
        "Weight contains string",
        [1.80, 1.90],
        [70, "bad"]
    )

    test_bmi_case(
        "Height contains bool",
        [1.80, True],
        [70, 80]
    )

    test_bmi_case(
        "Weight contains bool",
        [1.80, 1.90],
        [70, False]
    )

    test_bmi_case(
        "Height contains zero",
        [0, 1.90],
        [70, 80]
    )

    test_bmi_case(
        "Negative height",
        [-1.80, 1.90],
        [70, 80]
    )

    test_bmi_case(
        "Weight contains zero",
        [1.80, 1.90],
        [0, 80]
    )

    test_bmi_case(
        "Negative weight",
        [1.80, 1.90],
        [-70, 80]
    )

    print("\n===== INVALID LIMIT TESTS =====")

    test_limit_case(
        "BMI input not list",
        "hello",
        26
    )

    test_limit_case(
        "BMI contains string",
        [22.5, "bad"],
        26
    )

    test_limit_case(
        "BMI contains bool",
        [22.5, True],
        26
    )

    test_limit_case(
        "Limit is float",
        [22.5, 30.1],
        26.5
    )

    test_limit_case(
        "Limit is bool",
        [22.5, 30.1],
        True
    )


if __name__ == "__main__":
    main()
