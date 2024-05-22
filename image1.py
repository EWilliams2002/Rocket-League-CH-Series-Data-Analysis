# Name: Evan Williams
# Section Leader: Jacquie Kuru
# Date: 04/20/23
# ISTA 131 Final Project 1st Image Script
#
# Description: This file contains the code needed
#              to create and display data needed 
#              for image 1 of my final project.
# 
# 

import pandas as pd, numpy as np
import matplotlib.pyplot as plt

def read_in_file():
    """
    Name: read_in_file
    Type: Dataframe and array
    Description: This function reads in the csv file
                 for the game data by teams and returns
                 a dataframe with that data and an array
                 of team names.

    :return: a dataframe and array
    """

    team_names = []

    df = pd.read_csv('datasets/games_by_teams.csv', usecols=[4,6,9])

    for name in df['team_name']:
        if name not in team_names:
            team_names.append(name)
        else:
            pass
    
    return df, team_names

def get_values(df, team_names):
    """
    Name: get_values
    Type: dictionary
    Description: This function uses the dataframe and team_names
                  array to create and return a dictionary with 
                  ball possession time and scored goals data
                  per team

    :params: df - a dataframe consisnting of the data
             team_names - an array of strings of team names

    :return: a dictionary of the game data by team
    """

    data = {}

    for i in range(len(df['ball_possession_time'])):
        df.iloc[i, 1] = (df.iloc[i, 1] / 60)
    
    for name in team_names:
        ball_poss = df.loc[df['team_name'] == name, 'ball_possession_time'].sum()
        shots_scored = df.loc[df['team_name'] == name, 'core_goals'].sum()

        data[name] = [ball_poss, shots_scored]
    
    return data

def make_fig(data, team_names):
    """
    Name: make_fig
    Type: void
    Description: This function uses the dictinary data and teamn_names 
                 array from the previous fucntions and creates a plot

    :params: data - a dictionary with ball possession time and 
                    goals scored per team
             team_names - an array of strings of team names

    :return: none
    """

    # Create Empty Dataframe
    frame = pd.DataFrame(index=team_names, columns=['Total Ball Possession (Minutes)', 'Total Goals (Number of Goals made)'])

    # Set values from data dictionary
    for name in team_names:
        frame.loc[name,'Total Ball Possession (Minutes)'] = data[name][0]
        frame.loc[name,'Total Goals (Number of Goals made)'] = data[name][1]

    # Create initial scatter plot with data from dataframe
    x = 'Total Ball Possession (Minutes)'
    y = 'Total Goals (Number of Goals made)'
    frame.plot.scatter(x=x, y=y, c='DarkBlue')

    #### Misc changes to plot ####
    ax = plt.gca()
    fig = plt.gcf()

    # Line of Regression
    m, b = np.polyfit(list(frame[x]), list(frame[y]), 1)
    ax.plot(list(frame[x]), m*frame[x]+b)

    # Colors and Font Sizes
    ax.spines['bottom'].set_color('blue')
    ax.spines['top'].set_color('blue')
    ax.spines['right'].set_color('blue')
    ax.spines['left'].set_color('blue')
    ax.set_facecolor("navajowhite")
    fig.patch.set_facecolor("sandybrown")
    plt.xticks(fontsize=14, rotation='horizontal', color='blue')
    plt.yticks(fontsize=14, color='blue')
    plt.ylabel(y, fontsize=18, color='blue')
    plt.xlabel(x, fontsize=18, color='blue')
    plt.title('Total Shots on Goal Based on Total Possession of Ball Time', fontsize=18, color='blue')


def main():
    """
    Name: main
    Type: Void
    Description: This function ties 
                 all of the above functions
                 together, showing the plot
                 graph

    :return: Nothing
    """

    # Read in the csv file and gatehr additional data
    df,team_names = read_in_file()

    # ball_poss and shots_scored are dictionries with the total data entry per team
    data = get_values(df, team_names)

    # Create figure with data
    make_fig(data, team_names)

    # Show plot
    plt.show()