# The brief

For this project we're going to be working with a data set on [Kaggle](https://www.kaggle.com/), which is an awesome site if you're interesting in doing data science with Python. It contains tonnes of real data sets for you to use, absolutely free.

The data we're going to be working with today can be found [here](https://www.kaggle.com/neuromusic/avocado-prices/).

It contains thousands of records of avocado prices across several years in different regions of the US.

For this project I want to know a few different things about this data in this data set:

    I want to know which region had the lowest average price for conventionally grown avocados each year, and I want to know the same information for organic avocados.
    I want to know which region had the highest average price for both types of avocado for each given year.
    I want to know the lowest all time price for both conventionally grown and organic avocados, and I want to know the highest price as well.

pandas has some built in tools for calculating averages, so you may want to look [in the documentation](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.mean.html#pandas.core.groupby.GroupBy.mean) to see how to do that. There are also methods for finding the [minimum](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min) and [maximum](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html) value for a Series.

As a final note, the source data has many fields we don't need. Consider trimming the data down to just the region, the year, the type of avocado, and the price.

Good luck!