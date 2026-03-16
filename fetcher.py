from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players
from nba_api.live.nba.endpoints import scoreboard

from datetime import datetime

import pandas as pd


def player_finder(rgx: str):

    player_info = players.find_players_by_full_name(regex_pattern= rgx)
        
    print(player_info[0]['id'])
    print(player_info[0]['full_name'])
    player_career_stats = playercareerstats.PlayerCareerStats(player_info[0]['id'])

    return player_career_stats

ply_input = input("Input Player's Full Name: ")
df = player_finder(ply_input).get_data_frames()[0]
test = player_finder(ply_input).get_data_frames()[0]

df_rename = df.rename(columns={"PTS":"PPG"})
#vvvvvvvvvvv Test line vvvvvvvvvvv
#print (df.columns)
#print(df[["PLAYER_AGE", "PTS", "GP", "AST", "DREB"]]) # Columns shows the headers, to list sorts it nicer instead of index(headers) it just prints headers
#print(df_rename.columns)


print(bool([1, 2, 3] or 1/0))
