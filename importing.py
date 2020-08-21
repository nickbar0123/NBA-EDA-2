def get_data(path):
    import pandas as pd 
    df = pd.read_csv(path)
    def graphs(df):
        first_season = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'])]['PTS'].mean()
        second_season = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 1)]['PTS'].mean()
        third_season = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 2)]['PTS'].mean()
        fourth_season = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 3)]['PTS'].mean()
        return [first_season, second_season, third_season, fourth_season]
