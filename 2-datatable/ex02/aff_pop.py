from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def convert_population(value: str) -> float:
    """
    Convert population strings to numeric values

    Args:
        value (str):
            Population e.g., 42K, 42M, 42B

    Returns:
        float:
            Population in millions
    """
    if value.endswith("k"):
        return float(value[:-1]) / 1000
    if value.endswith("M"):
        return float(value[:-1])
    if value.endswith("B"):
        return float(value[:-1]) * 1000
    return float(value) / 1000000


def aff_pop(data: pd.DataFrame, country_1: str, country_2: str) -> None:
    """
    Display population projections for 2 countries

    Args:
        data (pd.DataFrame):
            DataFrame containing population projection data by country
        country_1 (str):
            First country to plot
        country_2 (str):
            Second country to plot
    """
    if data.empty:
        print("No population data found")
        return

    country_1_data = data[data['country'] == country_1]
    country_2_data = data[data['country'] == country_2]

    if country_1_data.empty or country_2_data.empty:
        print("Country not found")
        return

    years = data.columns[1:].astype(int)
    mask = (years >= 1800) & (years <= 2050)

    years = years[mask]
    country_1_values = country_1_data.iloc[0, 1:][mask]
    country_1_values = country_1_values.apply(convert_population)
    country_2_values = country_2_data.iloc[0, 1:][mask]
    country_2_values = country_2_values.apply(convert_population)

    plt.plot(years, country_1_values, label=country_1)
    plt.plot(years, country_2_values, label=country_2)

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population (in Millions)")
    plt.legend()

    plt.show()


def main():
    """
    Load dataset and display life expectancy graph for UAE
    """
    data = load("population_total.csv")

    if data is None:
        return

    aff_pop(data, "United Arab Emirates", "France")


if __name__ == "__main__":
    main()
