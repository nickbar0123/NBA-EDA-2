import pandas as pd 

player = pd.read_csv('Cleaned Player.csv')
season = pd.read_csv('Cleaned Season.csv')

df_left = player[['name', 'year_start','college','division','fame']]
df_right = season[['name','YEAR','G','POS','TRB%','STL%','BLK%','PTS', 'AST%']]

df = pd.merge(df_left, df_right, on = 'name', how = 'inner')

df = pd.DataFrame(df)

df.to_csv('Merged.csv', index = False)

