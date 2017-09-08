# Simple Scatter Plot in Pandas

## Summary 
>This is a simple introduction to data visualization in Python, using Pandas and Matplotlib to create scatter plots. The results displays the heights and weights of players for the sports: NHL, MLB, NFL and NBA. The data is shown in 2 ways: 

>#1 - Shows all the sport's data overlapping on one plot
 ![alt text](https://github.com/MilyChen/major-league-player-heights-and-weights/blob/master/src/figure_0.png "Figure w/ combined data")
 
>#2 - Shows each sport's data individually in subplots
 ![alt text](https://github.com/MilyChen/major-league-player-heights-and-weights/blob/master/src/figure_1.png "Figure w/ subplots")

## Constructing the Scatter Plots Steps

### 1 - Import the necessary libraries
```python
import library		#for my own custom functions
import pandas as pd		#for holding and manipulating data
import numpy as np		#for data analysis
import matplotlib.pyplot as plt		#for plotting
```
These packages need to be installed before they're able to be used in Python. 
 
### 2 - Import data  
```python
data_nhla = pd.read_csv('C:\...\NHL Data\MYSPORTSFEEDS-ACTIVE_PLAYERS-NHL.csv')
data_mlb = pd.read_csv('C:\...\MLB Data\MYSPORTSFEEDS-CUMULATIVE_PLAYER_STATS-MLB.csv')
data_nba = pd.read_csv('C:\...\NBA Data\MYSPORTSFEEDS-ACTIVE_PLAYERS-NBA.csv')
data_nfl = pd.read_csv('C:\...\NFL Data\MYSPORTSFEEDS-ACTIVE_PLAYERS-NFL.csv')
```
Pandas has many built in functions to read from various data structures such as csv, excel, json etc.. This makes it quick and simple to bring data into Python.

### 3 - Clean and prepare data for plotting
Unless the data your importing is completely formatted, clean, and filled in (ahh the dream), chances are you'll need to prep your data before plotting. Here are a few ways to get your data plot ready with Pandas. 
```python
df = pd.DataFrame(df[['#Weight', 'height_as_decimals']]).dropna()
```
There are a few different things happening with this one line. First, I'm dropping all the unnecessary columns from the dataframe by creating and reassigning the dataframe to a new dataframe with only the columns I'm interested in - weight and height. Second, I'm dropping all rows with one or more NaN values. Pandas also offers the versatility to drop specific rows if a specific column is empty or if 2+ or 3+ columns are empty. If dropping the row is not what you desire, there is also a built-in fill NaN function (.fillna()).

```python
df['height_as_decimals'] = df['#Height'].apply(lambda x:np.NaN if pd.isnull(x) else 
        library.height_ftiins_to_cm(x))
```
Ensure the data your trying to graph is in a format that can be sorted and graphed. Here I'm converting the values in the Height column, if not null, from the format 6'1" to cms by applying a custom function (see below).

```python
def height_ftiins_to_cm(x):
    x = x.replace('"', "")
    heights = x.split("'")
    ft_to_cm = float(heights[0]) * 30
    incs_to_cm = float(heights[1]) * 2.5
    return ft_to_cm + incs_to_cm
```
```python
df.height_as_decimals = pd.to_numeric(df.height_as_decimals)
```
Here I am casting the column height_as_decimals to numeric.

### 4 - Plot away!

```python
plt.figure(0)
colors = ['pink', 'orange', 'yellow', 'blue']
sports = ['mlb', 'nfl', 'nba', 'nhl']
shapes = ["*", "x", "^", "D"]
plot_x_ax = {}
plot_y_ax = {}
df_fit_fn = {}
#plot each player's height and weight
plt.plot(plot_x_ax[i], plot_y_ax[i], shapes[i], color=colors[i], alpha=0.2, label=sports[i])
#plot line of best fit
plt.plot(plot_x_ax[i], df_fit_fn[i](plot_x_ax[i]), '-k', color=colors[i], alpha=0.7)

plt.ylabel("Height (cm)")
plt.xlabel("Weight (lbs)")
plt.minorticks_on()
plt.legend(loc='upper left')
plt.title("Player Height per Major League Sport")

plt.show()
```


## Source Data 
>https://www.mysportsfeeds.com/
