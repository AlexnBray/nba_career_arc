from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard

from datetime import datetime

import pandas as pd



'''career = playercareerstats.PlayerCareerStats(player_id='203999')
get_player_career = career.get_data_frames()[0]

career.season_totals_regular_season.get_data_frame()

print(career.season_totals_regular_season.get_data_frame())

'''
id_input = ""

def career_stats(player_id: int) -> pd.DataFrame: # a pd.DataFrame is a 2D data structure that can hold data of different types (like a spreadsheet or SQL table)
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career.season_totals_regular_season.get_data_frame()

print(career_stats(id_input))
