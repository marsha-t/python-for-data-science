from load_csv import load


def main():
    print("\n--- VALID CSV ---")
    print(load("life_expectancy_years.csv"))

    print("\n--- UPPERCASE EXTENSION ---")
    print(load("life_expectancy_years.CSV"))

    print("\n--- WRONG EXTENSION ---")
    print(load("life_expectancy_years.txt"))

    print("\n--- MISSING FILE ---")
    print(load("does_not_exist.csv"))

    print("\n--- WRONG TYPE (int) ---")
    print(load(42))

    print("\n--- WRONG TYPE (list) ---")
    print(load(["file.csv"]))

    print("\n--- EMPTY STRING ---")
    print(load(""))

    print("\n--- DIRECTORY PATH ---")
    print(load("."))


if __name__ == "__main__":
    main()
