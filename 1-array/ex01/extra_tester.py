from array2D import slice_me


def test_case(description, data, start, end):
    print(f"\n--- {description} ---")

    try:
        result = slice_me(data, start, end)
        print(result)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


# VALID TESTS

family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]
]

test_case(
    "Valid slice 0 -> 2",
    family,
    0,
    2
)

test_case(
    "Valid negative slice",
    family,
    1,
    -2
)

test_case(
    "Slice beyond bounds",
    family,
    0,
    100
)

test_case(
    "Empty slice",
    family,
    2,
    2
)

# INVALID STRUCTURE TESTS

test_case(
    "Not a list",
    "hello",
    0,
    1
)

test_case(
    "Empty family",
    [],
    0,
    1
)

test_case(
    "Not 2D",
    [1.80, 78.4],
    0,
    1
)

test_case(
    "Rows different sizes",
    [
        [1, 2],
        [3]
    ],
    0,
    1
)

# INVALID VALUE TESTS

test_case(
    "Contains string",
    [
        [1, 2],
        [3, "hello"]
    ],
    0,
    1
)

test_case(
    "Contains bool",
    [
        [1, True],
        [3, 4]
    ],
    0,
    1
)

# INVALID START / END TESTS

test_case(
    "start is float",
    family,
    1.5,
    2
)

test_case(
    "end is string",
    family,
    0,
    "2"
)

test_case(
    "start is bool",
    family,
    True,
    2
)