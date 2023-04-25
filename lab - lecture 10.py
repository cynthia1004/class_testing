import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

df = pd.read_csv(url_to_csv)

# 1. Explore the data.  How many categories of flowers are there? What
#    are the mean and median values?  How would you find the mean values
#    per type of flower (you don't actually have to implement this - we
#    will cover it next week)

# Explore the data
df.index
df.columns
df.head()
df.tail()
df.dtypes  # Note: species is an object (string)
df
# How many categories of flowers are there?
# A few solutions:
df['species'].unique()
df['species'].value_counts()
df['species'].describe()

# What are the mean and median values? 
# A few solutions: 
#df.mean() # ERROR!  B/se of the species string
num_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df[num_cols].mean()
df[num_cols].median()

df.set_index('species').mean()  # axis=0 or axis="index" is the kwarg default; takes mean over rows
df.set_index('species').mean(axis=1)  # axis=1 or axis="columns" takes mean over columns

df.describe()
df.describe().transpose()

# 2. Using one line of code, multiply every value by 100
# A few solutions:
df.set_index('species') * 100

df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].applymap(lambda v: v*100)

# This could be one line but reads better as two:
num_cols = [c for c in df.columns if c != 'species'] 
df[num_cols] = df[num_cols].applymap(lambda v: v*100)


# 3. Subset the data so only virginica flowers remain
df[df['species'] =='virginica']  # A view
df[df['species'] == 'virginica'].copy()  # A copy
df.loc[df['species'] == 'virginica']  # A copy


# 4. Create a new column named "petal_area" which is equal to the length
#    times the width
df['petal_area'] = df['petal_length'] * df['petal_width']
