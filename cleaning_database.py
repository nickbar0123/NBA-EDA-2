import pandas as pd 

season = pd.read_csv('seasons.csv')

season.drop(season.columns[season.columns.str.contains('Unnamed: 0')], axis = 1, inplace = True)
season.dropna(how = 'all', axis = 1, inplace = True)
season.dropna(how = 'any', axis = 0, inplace = True)

season.rename(columns = {'Pos': 'POS', 'Player':'name', 'Year':'YEAR'}, inplace = True) 
season['name'] = season['name'].str.replace('*','',regex = True)

season.to_csv('Cleaned Season.csv', index = False)