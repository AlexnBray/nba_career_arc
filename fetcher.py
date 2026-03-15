from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players
from nba_api.live.nba.endpoints import scoreboard

from datetime import datetime

import pandas as pd
ply_input = input("Input Player's Full Name: ")
player_info = players.find_players_by_full_name(regex_pattern= ply_input)
print(player_info[0]['id'])
print(player_info[0]['full_name'])

player_career_stats = playercareerstats.PlayerCareerStats(player_info[0]['id'])
print(player_career_stats.get_data_frames()[0])
'''def age(player_id: int) -> int: 
    player_info = commonplayerinfo.CommonPlayerInfo(player_id = player_id)
    return player_info

print(age(1630173).get_data_frames()[1])'''