# Name: Evan Williams
# Section Leader: Jacquie Kuru
# Date: 04/20/23
# ISTA 131 Final Project 3rd Image Script
#
# Description: This file contains the code needed
#              to create and display data needed 
#              for image 3 of my final project.
# 
# 

import pandas as pd
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

    df = pd.read_csv('datasets/games_by_teams.csv', usecols=[4,8,54])

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
                  shots taken and number of wins data

    :params: df - a dataframe consisnting of the data
             team_names - an array of strings of team names

    :return: a dictionary of the game data on shots taken
             and win averages
    """

    ret_data = {'0-700': 0,
                '700-1400': 0,
                '1400-2100': 0,
                '2100-2800': 0,
                '2800-3500': 0}
    

    num_wins_700 = 0
    num_wins_1400 = 0
    num_wins_2100 = 0
    num_wins_2800 = 0
    num_wins_3500 = 0

    amount_of_wins_700 = 0
    amount_of_wins_1400 = 0
    amount_of_wins_2100 = 0
    amount_of_wins_2800 = 0
    amount_of_wins_3500 = 0

    for name in team_names:
        num_wins = 0
        winner_col = df.loc[df['team_name'] == name, 'winner']
        shots = df.loc[df['team_name'] == name, 'core_shots'].sum()

        for n in winner_col.index:
            if winner_col[n]:
                num_wins += 1

        if shots <= 700:
            num_wins_700 += num_wins
            amount_of_wins_700 += 1

        elif 700 < shots <= 1400:
            num_wins_1400 += num_wins
            amount_of_wins_1400 += 1

        elif 1400 < shots <= 2100:
            num_wins_2100 += num_wins
            amount_of_wins_2100 += 1

        elif 2100 < shots <= 2800:
            num_wins_2800 += num_wins
            amount_of_wins_2800 += 1

        elif 2800 < shots:
            num_wins_3500 += num_wins
            amount_of_wins_3500 += 1
    
    ret_data['0-700'] = num_wins_700 / amount_of_wins_700
    ret_data['700-1400'] = num_wins_1400 / amount_of_wins_1400
    ret_data['1400-2100'] = num_wins_2100 / amount_of_wins_2100
    ret_data['2100-2800'] = num_wins_2800 / amount_of_wins_2800
    ret_data['2800-3500'] = num_wins_3500 / amount_of_wins_3500

    return ret_data

def make_fig(data):
    """
    Name: make_fig
    Type: void
    Description: This function uses the dictinary data
                 array from the previous fucntions and 
                 creates a plot

    :params: data - a dictionary with number of avg number
                    of wins based on shots taken ranges


    :return: none
    """

    # Create initial scatter plot with data from dataframe
    x = 'Ranges of Shots Taken (Number of Shots)'
    y = 'Average Number of Wins (Avg. Number of Wins)'
    fig = plt.figure(figsize= (13,9))
    plt.bar(list(data.keys()),list(data.values()), color='DarkBlue', width=0.4, align='center')

    #### Misc changes to plot ####
    ax = plt.gca()
    
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
    plt.title('Avergae Number of Wins Grouped by Ranges of Shots Taken by Team', fontsize=18, color='blue')


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
    make_fig(data)


    # Show plot
    plt.show()