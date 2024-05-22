# Name: Evan Williams
# Section Leader: Jacquie Kuru
# Date: 04/20/23
# ISTA 131 Final Project 2nd Image Script
#
# Description: This file contains the code needed
#              to create and display data needed 
#              for image 2 of my final project.
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

    df = pd.read_csv('datasets/games_by_teams.csv', usecols=[4,12,54])

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
                  above and win average data

    :params: df - a dataframe consisnting of the data
             team_names - an array of strings of team names

    :return: a dictionary with number of teams
             with below and average win data
    """

    wins_per_team = {}

    total_wins = 0

    for name in team_names:
        num_wins = 0
        winner_col = df.loc[df['team_name'] == name, 'winner']
        
        for n in winner_col.index:
            if winner_col[n]:
                num_wins += 1

        wins_per_team[name] = num_wins
        total_wins += num_wins

    total_win_avg = total_wins / len(team_names)

    score_above_avg = 0
    score_below_avg = 0

    num_teams_above = 0
    num_teams_below = 0

    ret_data = {}

    for name in team_names:
        score = df.loc[df['team_name'] == name, 'core_score'].sum()

        if wins_per_team[name] > total_win_avg:
            score_above_avg += score
            num_teams_above += 1
        else:
            score_below_avg += score
            num_teams_below += 1

    ret_data['Above Win Average(' + str(round(num_teams_above)) + ')'] = score_above_avg / num_teams_above
    ret_data['Below Win Average(' + str(round(num_teams_below)) + ')'] = score_below_avg / num_teams_below
    
    return ret_data, total_win_avg

def make_fig(data, win_avg):
    """
    Name: make_fig
    Type: void
    Description: This function uses the dictinary data
                 array from the previous fucntions and 
                 creates a plot

    :params: data - a dictionary with ball possession time and 
                    goals scored per team

    :return: none
    """

    # Create initial scatter plot with data from dataframe
    x = 'Teams Above/Below Win Average (Number of Teams)'
    y = 'Average Combined Score (Avg. Score)'
    fig = plt.figure(figsize= (13,8))
    plt.bar(list(data.keys()),list(data.values()), color='DarkBlue', width=0.2, align='center')

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
    plt.title('Average Combined Score of Teams With Above/Below Average Number of Wins - Win Average(' + str(round(win_avg)) + ')', fontsize=18, color='blue')


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
    data,win_avg = get_values(df, team_names)


    # Create figure with data
    make_fig(data, win_avg)


    # Show plot
    plt.show()