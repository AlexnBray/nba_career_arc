from nba_api.stats.endpoints import playercareerstats

career = playercareerstats.PlayerCareerStats(player_id='203999')

df = career.season_totals_regular_season.get_data_frame()
print(df)
