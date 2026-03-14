from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

# 1. Find a player's ID using the static lookup (no API call)
player_dict = players.find_players_by_full_name("LeBron James")[0]
player_id = player_dict["id"]  # 2544

# 2. Fetch career stats
career = playercareerstats.PlayerCareerStats(player_id=player_id)

# 3. Get a DataFrame
df = career.get_data_frames()[0]
print(df.head(["GP"]))