# Simple Scatter Plot in Pandas

## Summary 
>This is a simple introduction to data visualization in Python, using Pandas and Matplotlib to create scatter plots. The results displays the heights and weights of players for the sports: NHL, MLB, NFL and NBA. The data is shown in 2 ways: 

>#1 - Shows all the sports overlapping on 1 plot
 ![alt text](https://github.com/MilyChen/major-league-player-heights-and-weights/blob/master/src/figure_0.png "Figure w/ combined data")
 
>#2 - Shows each sport's data individually in subplots
 ![alt text](https://github.com/MilyChen/major-league-player-heights-and-weights/blob/master/src/figure_1.png "Figure w/ subplots")

## Constructing the Scatter Plots

>#1 Import the necessary libraries.
```python
import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
>#2 Import  
```python
#======set up data to plot==============================================================================
data_nhla = pd.read_csv('C:\...\MySportsFeed\NHL Data\MYSPORTSFEEDS-ACTIVE_PLAYERS-NHL-20162017REGULAR.csv')
data_mlb = pd.read_csv('C:\...\MySportsFeed\MLB Data\MYSPORTSFEEDS-CUMULATIVE_PLAYER_STATS-MLB-2016REGULAR.csv')
data_nba = pd.read_csv('C:\...\MySportsFeed\NBA Data\MYSPORTSFEEDS-ACTIVE_PLAYERS-NBA-20162017REGULAR.csv')
data_nfl = pd.read_csv('C:\...MySportsFeed\NFL Data\MYSPORTSFEEDS-ACTIVE_PLAYERS-NFL-20162017REGULAR.csv')

data = [data_mlb, data_nfl, data_nba, data_nhla]
colors = ['pink', 'orange', 'yellow', 'blue']
sports = ['mlb', 'nfl', 'nba', 'nhl']
shapes = ["*", "x", "^", "D"]
plot_x_ax = {}
plot_y_ax = {}
df_fit_fn = {}
```


## Source Data 
>https://www.mysportsfeeds.com/
