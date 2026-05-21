from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def projection_life(data: pd.DataFrame, year: int) -> None:
    """
    Display scatter plot of income & expectancy for given year

    Args:
        data (pd.DataFrame):
            DataFrame containing income &
            life expectancy projection data by country
        year (int):
            Year to plot
    """
    if data.empty:
        print("No data found")
        return

    plt.scatter(data[f"{year}_income"], data[f"{year}_life"], s=15)

    plt.title(f"{year}")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()


def main():
    """
    Load income & expectancy datasets,
    and display scatter plot of both in 1900 by country
    """
    expectancy = load("life_expectancy_years.csv")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    if expectancy is None or income is None:
        return
    merged = pd.merge(
        expectancy,
        income,
        on="country",
        suffixes=("_life", "_income")
    )
    projection_life(merged, 1900)


if __name__ == "__main__":
    main()
