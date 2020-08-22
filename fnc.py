def graph(x):
    first_season = x[(x['fame'] == 1) & (x['YEAR'] == x['year_start'])]['PTS'].mean()
    second_season = x[(x['fame'] == 1) & (x['YEAR'] == x['year_start'] + 1)]['PTS'].mean()
    third_season = x[(x['fame'] == 1) & (x['YEAR'] == x['year_start'] + 2)]['PTS'].mean()
    fourth_season = x[(x['fame'] == 1) & (x['YEAR'] == x['year_start'] + 3)]['PTS'].mean()
    points = [first_season, second_season, third_season, fourth_season]

    return points