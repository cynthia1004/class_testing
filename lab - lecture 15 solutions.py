# 1. Using Pandas DataReader, retrieve the average monthly closing stock
#    prices of Tesla (TSLA) from January 1st, 2019 to December 1st, 2021.

#Hint: https://www.alphavantage.co/support/#api-key
import pandas_datareader.data as web
import pandas as pd
import datetime
import matplotlib.pyplot as plt

apikey = '90VRRJWKJV9L5N46'
start = datetime.date(year=2019, month=1,  day=1)
end = datetime.date(year=2021, month=12, day=1)
#end = datetime.date(year=2023, month=5, day=1)  # Uncomment for question 4
series = 'TSLA'
endpoints = 'av-monthly'

df = web.DataReader(series, endpoints, 
                    start=start, end=end,
                    api_key=apikey)


# 2. Create a new column that holds the rolling 3 month average.
df['close_3ma'] = df['close'].rolling(3).mean()


# 3. Create a figure showing the time series for the monthly level and
#    the monthly rolling average together.
fig, ax = plt.subplots(figsize=(12,6))
x = pd.to_datetime(df.index)  # Convert index to a datetime for axis label formatting 
ax.plot(x, df['close'], 'r-', label='Mean closing')
ax.plot(x, df['close_3ma'], 'b--', label='Mean closing, 3-mo MA')

ax.legend()
ax.set_title('Tesla Monthly Average Closing Stock Price')
ax.set_xlabel('')
ax.set_ylabel('Price ($)')

# Remove spines?  Add vlines for significant events?  Change font or font size?
# Change colors?  Move legend outside of the axis lines?  Label max and min?

plt.show()


# 4. Recreate your figure showing the time series through May 1st, 2023.

# Just update the initial "end =" assignment & rerun parts 1 through 3!


# 5. Create a new dataframe from the base data from part 1 that resamples
#    the data to quarterly, using the mean value.
df.index = pd.to_datetime(df.index)
df_q = df.resample('QS').mean()  # 'Q' - quarter end indexes, 'QS' quarter start indexes