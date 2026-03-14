from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.live.nba.endpoints import scoreboard

from datetime import datetime

import pandas as pd

def age(player_id: int) -> int: 
    player_info = commonplayerinfo.CommonPlayerInfo(player_id = player_id)
    return player_info

print(age(1630173).get_data_frames())