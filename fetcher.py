from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard
from datetime import datetime
import pandas as pd

career = playercareerstats.PlayerCareerStats(player_id='203999')
get_player_career = career.get_data_frames()[0]

career.season_totals_regular_season.get_data_frame()

career.get_dict()

