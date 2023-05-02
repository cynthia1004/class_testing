import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

df = pd.read_csv(url_to_csv)

# 1) Create a groupby object using "clarity" and "color" as the keys
#    What is the object created?  Can you do anything with it?  Explore.
grouped = df.groupby(['clarity', 'color'])

grouped.groups  # Mapping from DataFrame to GroupBy object
grouped.get_group(('IF', 'D'))  # Note: you must enter a tuple & order must 
# match how you create the group
df_IF_D = grouped.get_group(('IF', 'D'))  # Creates a sub-df for the group

grouped.head(n=1)  # First observation in each group

grouped.mean(numeric_only=True).round(2)  # Numeric value means by group

grouped.size()  # Obs by group
df_group_size = grouped.size()  # Creates a sub-df of obs by group
df_group_size = df_group_size.reset_index(name='count')  # Reset the index  

# For more methods, see:  
# https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html


# 2) Display the describe output for all the groups.  Display the describe() 
#    output JUST for group color=E, clarity=SI2.
grouped.describe().round(2)  # All groups

grouped.get_group(('SI2', 'E')).describe().round(2)  # Just group E, SI2 
grouped.get_group(('SI2', 'E')).describe().round(2).T  # What does .T do?

# All groups .describe returns a df w/ keys as index => can also select by .loc
grouped.describe().loc[('SI2', 'E')].round(2)  


# 3) Display the max value for price in each group.
grouped.max()
grouped.max()['price']


# 4) Show a dataframe where each row is a unique group, with the values sorted
#    by price from highest to lowest.

# What's wrong with doing it this way?  Hint: do the values in the top
# row correspond to an actual diamond in grouped.max()?
grouped.max().sort_values('price', ascending=False)

# We need to sort, then get the first obs (then sort the resulting data).
# The groupby.apply() method iterates over groups, so use it to do so.
grouped.apply(lambda g: g.sort_values('price', ascending=False)
              .head(1)) \
             .sort_values('price', ascending=False)
            