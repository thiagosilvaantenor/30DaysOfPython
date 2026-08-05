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


# filter dt to only the year inform, and drops the column
def find_with_year(dt: DataFrame, year):
    return dt.query("year == @year")
    # if function == "low":
    #     lowest = same_year["AveragePrice"].min()
    #     return same_year.query("AveragePrice == @lowest")
    # else:
    #     highest = same_year["AveragePrice"].max()
    #     return same_year.query("AveragePrice == @highest")


def get_avg_price_each_year(dt, years):

    averages = {}
    for year in years:
        result = find_with_year(dt, year).groupby("region").mean(numeric_only=True)
        averages.update({year: result})
    return averages


def show_avg_price_all_time(dt, function, years):
    if function not in ("low", "high"):
        print('Oops, wrong argument for "function", use "low" or "high"')
        return None
    # Find the avg price of each year and saves in the dataframe
    dt_result = pd.DataFrame({"AveragePrice": [0.0]}, index=[0])
    for year in years:
        result = find_with_year(dt, year).drop_duplicates()
        result = result[["year", "region", "type", "AveragePrice"]]
        dt_result = pd.concat([dt_result, result["AveragePrice"]])

    # Inside the dt of years find the most of all time
    if function in "low":
        lowest = dt_result.loc[dt_result.AveragePrice > 0].min()
        return dt.loc[dt.AveragePrice == lowest["AveragePrice"]]
    else:
        highest = dt_result.loc[dt_result.AveragePrice > 0].max()
        return dt.loc[dt.AveragePrice == highest["AveragePrice"]]


def show_min_max(dt, type):
    # which region had the lowest avg price,
    #  organic avocados each year
    print(f"#### Lowest AVG Price Region for {type} grown avocados ####\n")
    years = dt["year"].drop_duplicates()
    avgs = get_avg_price_each_year(dt, years)
    for year in avgs:
        lowest = avgs[year].min()["AveragePrice"]
        result = avgs[year].query("AveragePrice == @lowest")
        print(f"{result.head()}")

    # # highest avg price for both types each year
    # conventionally

    print(f"#### Highest AVG Price Region for {type} grown avocados ####\n")
    for year in avgs:
        highest = avgs[year].max()["AveragePrice"]
        result = avgs[year].query(
            "AveragePrice == @highest",
        )
        print(f"{result.head()}")

    print("###############\n")


# which region had the lowest avg price,
#  conventionally grown each year
dt = get_data()
# filter type
dt_conv = dt.query("type == 'conventional'").copy()
show_min_max(dt_conv, "Conventionally")

# which region had the lowest avg price,
#  organic avocados each year
dt_organic = dt.query("type == 'organic'").copy()
show_min_max(dt_conv, "Organic")
print("###############\n")

# # lowest all time price
# for both coventionally and organic
print(
    "#### Lowest AVG Price of all time for Organic and Convetionally grown avocados ####\n"
)
dt_both = dt.copy()
years = dt_both["year"].drop_duplicates()
print(show_avg_price_all_time(dt_both, "low", years))
print("###############\n")
# highest all time price
# for both coventionally and organic
print(
    "#### Highest AVG Price of all time for Organic and Convetionally grown avocados ####\n"
)

print(show_avg_price_all_time(dt_both, "high", years))

## Simplified version
highest_c = dt_both["AveragePrice"].max()
print(f"Highest of both conventional and organic price simplified: {highest_c:.2f}")
