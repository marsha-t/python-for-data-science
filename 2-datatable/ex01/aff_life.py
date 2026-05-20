from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def aff_life(country_life: pd.DataFrame) -> None:
    """
    Display life expectancy projections for a country

    Args:
        country_life (pd.DataFrame):
            DataFrame containing single country's life expectancy data
    """
    if country_life.empty:
        print("No country data found")
        return

    years = country_life.columns[1:].astype(int)
    values = country_life.iloc[0, 1:]
    country = country_life.iloc[0, 0]

    plt.plot(years, values, label=country)

    plt.title(f"{country} Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.legend()

    plt.show()


def main():
    """
    Load dataset and display life expectancy graph for UAE
    """
    data = load("life_expectancy_years.csv")
    if data is not None:
        uae = data[data["country"] == "United Arab Emirates"]
        aff_life(uae)


if __name__ == "__main__":
    main()
