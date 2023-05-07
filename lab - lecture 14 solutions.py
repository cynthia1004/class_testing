import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

fig, ax = plt.subplots()
grouped = df.groupby('species')
colors = {'setosa':'red', 'versicolor':'blue', 'virginica':'green'}

for key, group in grouped:
    group.plot(x='sepal_length', y='petal_length',
               ax=ax,
               kind='scatter',
               color=colors[key],
               label=key.capitalize())

leg = ax.legend()
leg.set_title('species')
plt.show()

# Recreate this plot in Seaborn!
#sns.set()  # Results in Seaborn style (e.g.) grey background w/ white lines

# Easiest but has wrong capitalization in legend
ax = sns.scatterplot(x='sepal_length', y='petal_length',
                     data=df, hue='species')
plt.show()  # This clears the previous plot
# See what happens if you don't include this & run the next ax =


# To get the capitalization in the legend right
df['species'] = df['species'].str.capitalize()  # Cap. method 1
ax = sns.scatterplot(x='sepal_length', y='petal_length',
                     data=df.assign(species=df['species'].str.capitalize()),  # Cap. method 2 
                     hue='species')
# Capitaliztion methods 1 & 2 do the same thing & you only need one.
# The second one lets you capitalize without an extra line for the df[] =. 
# But the first changes the df, so you don't have to repeat the long data=df in
# subsequent plots. 
plt.show()


# To get the colors to match (but Seaborn's look better!)
colors_cap = {key.capitalize():val for key, val in colors.items()}
ax = sns.scatterplot(x='sepal_length', y='petal_length',
                     data=df, hue='species',
                     palette=colors_cap) 
plt.show()
                    

# Seaborn only returns the Axes, not the Figure 
# How to get the Figure, method 1
fig, ax = plt.subplots()  # Method 1 initializes w/ matplotlib ex-ante
ax = sns.scatterplot(x='sepal_length', y='petal_length',
                data=df, hue='species', ax=ax)
fig.savefig('myplot.png')
plt.show()  


# How to get the Figure, method 2
ax = sns.scatterplot(x='sepal_length', y='petal_length',
                data=df, hue='species', ax=ax)
fig = ax.get_figure()      # Method 2 recovers Figure ex-post
fig.savefig('myplot.png')
plt.show()  
