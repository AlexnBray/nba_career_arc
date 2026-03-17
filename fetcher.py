from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players
from nba_api.live.nba.endpoints import scoreboard
import sys

from datetime import datetime

import pandas as pd


def player_finder(rgx: str):

    player_info = players.find_players_by_full_name(regex_pattern= rgx)
    
    ########If multiple players########
    if len(player_info) > 1:
        print("Multiple")
        for i,x in enumerate(player_info):
            print (str(i+1) + "." + " ",(commonplayerinfo.CommonPlayerInfo(player_id= x['id']).get_data_frames()[0][["DRAFT_YEAR","DRAFT_NUMBER"]]))
        ply_choose = (input("Enter the number corresponding to the player you would like to see: "))

    print(player_info[0]['id'])
    print(player_info[0]['full_name'])
    player_career_stats = playercareerstats.PlayerCareerStats(player_info[0]['id'])

    return player_career_stats
    
ply_input = input("Input Player's Full Name: ")
##### To ensure a valid player is inputted
try:
    df = player_finder(ply_input).get_data_frames()[0]
except IndexError:
    print("Player has not played in the NBA")
    sys.exit()

df_rename = df.rename(columns={"PTS":"PPG"})
# print(df.columns)

#vvvvvvvvvvv Test line vvvvvvvvvvv
#print(commonplayerinfo.CommonPlayerInfo(player_id= 1629029).get_data_frames()[0])
print(df[["PLAYER_AGE", "PTS", "GP", "AST", "DREB"]]) # Columns shows the headers, to list sorts it nicer instead of index(headers) it just prints headers
#print(df_rename.columns)

