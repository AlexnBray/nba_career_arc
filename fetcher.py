from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players
from nba_api.live.nba.endpoints import scoreboard
import sys

from datetime import datetime

import pandas as pd
'''
Print player_info before you index into it — if there are two 
matching players it'll show you a list with two dictionaries instead of one.
Then think about how you'd handle that case — what would you want the 
program to do if it finds two matches? Probably print both options and ask 
the user to be more specific. Have a think about how you'd write that logic.
'''

def player_finder(rgx: str):

    player_info = players.find_players_by_full_name(regex_pattern= rgx)
    if len(player_info) > 1:
        print("Multiple")
        for i,x in enumerate(player_info):
            print (str(i+1) + "." + " " + str(x["id"]))

    print(player_info[0]['id'])
    print(player_info[0]['full_name'])
    player_career_stats = playercareerstats.PlayerCareerStats(player_info[0]['id'])

    return player_career_stats
    
ply_input = input("Input Player's Full Name: ")
try:
    df = player_finder(ply_input).get_data_frames()[0]
except IndexError:
    print("Player has not played in the NBA")
    sys.exit()

df_rename = df.rename(columns={"PTS":"PPG"})
# print(df.columns)

#vvvvvvvvvvv Test line vvvvvvvvvvv

print(df[["PLAYER_AGE", "PTS", "GP", "AST", "DREB"]]) # Columns shows the headers, to list sorts it nicer instead of index(headers) it just prints headers
#print(df_rename.columns)

