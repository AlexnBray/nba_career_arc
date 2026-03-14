import pandas as pd

data = {
    "players": ["Lebron", "Steph", "KD", "Etc"], 
    "Positions": ["SF" , "PG", "SF", "Etc"]
    }

dataframe = pd.DataFrame(data)

print(dataframe)