'''
Created on Aug 26, 2017

@author: Mily
'''
import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#======set up data to plot==============================================================================
data_nhla = pd.read_csv('C:\...\MySportsFeed\NHL Data\MYSPORTSFEEDS-ACTIVE_PLAYERS-NHL-20162017REGULAR.csv')
data_mlb = pd.read_csv('C:\...\MySportsFeed\MLB Data\MYSPORTSFEEDS-CUMULATIVE_PLAYER_STATS-MLB-2016REGULAR.csv')
data_nba = pd.read_csv('C:\...\MySportsFeed\NBA Data\MYSPORTSFEEDS-ACTIVE_PLAYERS-NBA-20162017REGULAR.csv')
data_nfl = pd.read_csv('C:\...\MySportsFeed\NFL Data\MYSPORTSFEEDS-ACTIVE_PLAYERS-NFL-20162017REGULAR.csv')

data = [data_mlb, data_nfl, data_nba, data_nhla]
colors = ['pink', 'orange', 'yellow', 'blue']
sports = ['mlb', 'nfl', 'nba', 'nhl']
shapes = ["*", "x", "^", "D"]
plot_x_ax = {}
plot_y_ax = {}
df_fit_fn = {}

#===first plot of combined data===========================================================================
plt.figure(0)  #

for i, df in enumerate(data):
    #convert height column from ft'in'' into cm
    df['height_as_decimals'] = pd.to_numeric(df['#Height'].apply(lambda x:np.NaN if pd.isnull(x) else library.height_ftiins_to_cm(x)))
    #drop all rows with 1+ NaN column values
    df = pd.DataFrame(df[['#Weight', 'height_as_decimals']]).dropna()
    df.height_as_decimals = pd.to_numeric(df.height_as_decimals)
    plot_x_ax[i] = np.array(df['#Weight'])
    plot_y_ax[i] = np.array(df.height_as_decimals)
    df_fit = np.polyfit(plot_x_ax[i], plot_y_ax[i], 1)
    df_fit_fn[i] = np.poly1d(df_fit)
    #plot each player's height and weight
    plt.plot(plot_x_ax[i], plot_y_ax[i], shapes[i], color=colors[i], alpha=0.2, label=sports[i])
    #plot line of best fit
    plt.plot(plot_x_ax[i], df_fit_fn[i](plot_x_ax[i]), '-k', color=colors[i], alpha=0.7)
   

plt.ylabel("Height (cm)")
plt.xlabel("Weight (lbs)")
plt.minorticks_on()
plt.legend(loc='upper left')
plt.title("Player Height per Major League Sport")

#second plot separated data in subplots====================================================================
fig_split = plt.figure(1)


for i, df in enumerate(data):
    #create a subplot
    ax = fig_split.add_subplot(2, 2, (i + 1))
    ax.set_xlim(150, 350)
    ax.set_ylim(160, 220)
    plt.plot(plot_x_ax[i], plot_y_ax[i], shapes[i], color=colors[i], alpha=0.2, label=sports[i])
    plt.plot(plot_x_ax[i] , df_fit_fn[i](plot_x_ax[i]), '-k', color='black', alpha=0.2)
    plt.title(sports[i].upper())
     
plt.suptitle('Major League Player Heights')
plt.subplots_adjust(hspace=0.36)

# display all figures
plt.show()  




