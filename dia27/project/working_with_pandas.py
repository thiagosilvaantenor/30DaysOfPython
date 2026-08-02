import pandas as pd
from pandas import DataFrame
from pandas import Series
from pandas import Float64Dtype


def get_data(file="./data/avocado.csv") -> DataFrame:
    from pathlib import Path

    script_dir = Path(__file__).parent.resolve()
    file_dir = script_dir / f"./{file}"
    dt = pd.read_csv(file_dir)
    # Selecting only the columns that will be use
    dt = dt[["region", "year", "type", "AveragePrice"]]

    return dt


# Generalist function to deal with highest or lowest avg price in year
def find_with_year(dt: DataFrame, year, function: str):
    same_year = dt.query("year == @year")
    if function == "low":
        lowest = same_year["AveragePrice"].min()
        return same_year.query("AveragePrice == @lowest")
    else:
        highest = same_year["AveragePrice"].max()
        return same_year.query("AveragePrice == @highest")


def show_avg_price_each_year(dt, function, years):
    if function not in ("low", "high"):
        print('Oops, wrong argument for "function", use "low" or "high"')
        return None

    for year in years:
        result = find_with_year(dt, year, function).drop_duplicates()
        result = result[["year", "region", "type", "AveragePrice"]]
        print(result.head())


def show_avg_price_all_time(dt, function, years):
    if function not in ("low", "high"):
        print('Oops, wrong argument for "function", use "low" or "high"')
        return None
    # Find the avg price of each year and saves in the dataframe
    dt_result = pd.DataFrame({"AveragePrice": [0.0]}, index=[0])
    for year in years:
        result = find_with_year(dt, year, function).drop_duplicates()
        result = result[["year", "region", "type", "AveragePrice"]]
        dt_result = pd.concat([dt_result, result["AveragePrice"]])

    # Inside the dt of years find the most of all time
    if function in "low":
        lowest = dt_result.loc[dt_result.AveragePrice > 0].min()
        return dt.loc[dt.AveragePrice == lowest["AveragePrice"]]
    else:
        highest = dt_result.loc[dt_result.AveragePrice > 0].max()
        return dt.loc[dt.AveragePrice == highest["AveragePrice"]]


# which region had the lowest avg price,
#  conventionally grown each year
dt = get_data()

# filter type
dt_conv = dt.query("type == 'conventional'")
years = dt_conv["year"].drop_duplicates()
print("#### Lowest AVG Price Region for Convetionally grown avocados ####\n")
show_avg_price_each_year(dt_conv, "low", years)
print("###############\n")


# which region had the lowest avg price,
#  organic avocados each year
print("#### Lowest AVG Price Region for Organic grown avocados ####\n")
dt_organic = dt.query("type == 'organic'")
years = dt_organic["year"].drop_duplicates()
show_avg_price_each_year(dt_organic, "low", years)
print("###############\n")

# highest avg price for both types each year
print(
    "#### Highest AVG Price Region for Organic and Convetionally grown avocados ####\n"
)
dt_both = get_data()
years = dt_both["year"].drop_duplicates()
show_avg_price_each_year(dt_both, "high", years)
print("###############\n")
# lowest all time price
# for both coventionally and organic
print(
    "#### Lowest AVG Price of all time for Organic and Convetionally grown avocados ####\n"
)
dt_low_all = get_data()
years = dt_low_all["year"].drop_duplicates()
print(show_avg_price_all_time(dt_low_all, "low", years))
print("###############\n")
# highest all time price
# for both coventionally and organic
print(
    "#### Highest AVG Price of all time for Organic and Convetionally grown avocados ####\n"
)
dt_high_all = get_data()
print(show_avg_price_all_time(dt_high_all, "high", years))
