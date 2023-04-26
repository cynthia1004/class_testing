import pandas as pd

# Combine these three dataframes so that the result is a single
# dataframe with the columns "date", "place", "value1", "value2",
# with the date columns being datetime objects that run from
# 1/2020 to 10/2021, without modifying any starter code.
# Note: df1 contains value1 values & df2 contains value2 values.

data1 = {'date':['2020-1-1', '2020-4-1', '2020-7-1', '2020-10-1'],
         'place1':[39, 17, 20, 88],
         'place2':[55, 88, 19, 42]}

data2 = {'date':['2020-01-01', '2020-04-01', '2020-07-01', '2020-10-01',
                 '2021-01-01', '2021-04-01', '2021-07-01', '2021-10-01'],
         'place1':[1, 4, 7, 2, 5, 8, 11, 13],
         'place2':[2, 5, 8, 6, 6, 9, 13, 15]}

data3 = {'date':['2021-1-1', '2021-4-1', '2021-7-1', '2021-10-1']*2,
         'place':['place1']*4 + ['place2']*4,
         'value1':[33, 43, 53, 34, 35, 46, 47, 48]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

## Examine the DataFrames to see what needs to be done
print(df1)  # Wide 2020, place 1-2, value1 data
print(df2)  # Wide 2020-21, place 1-2, value2 data
print(df3)  # Long 2021, place 1-2, value1 data

df1.dtypes
df2.dtypes
df3.dtypes
# All dates are strings, not datetimes (but we knew that from the data dictionaries)
 
## Reshape df1 wide to long
df1_long = df1.melt(id_vars='date', value_name='value1', var_name='place')
# Long 2020, place 1-2, value1 data 

## Combine df1 (2020) & df3 (2021) value 1 data vertically
df_1and3 = pd.concat([df1_long, df3])
# Long 2020-21, place 1-2, value1 data  

## Reshape df2 wide to long
df2_long = df2.melt(id_vars='date', value_name='value2', var_name='place')
# Long 2020-21, place 1-2, value2 data  

## Convert date variables to datetimes
df_1and3["date"] = pd.to_datetime(df_1and3["date"])
df2_long["date"] = pd.to_datetime(df2_long["date"])

## Merge the long 2020-21, place 1-2 datasets
df = df_1and3.merge(df2_long, on=['date', 'place'], how='outer', indicator=True)
assert(all(df['_merge'] == 'both')), 'Nope!'
df = df.drop('_merge', axis=1)
df