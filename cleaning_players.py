import pandas as pd
import numpy as np 

player = pd.read_csv('players.csv')

player['college'] = player['college'].fillna('Unknown')

import requests
from bs4 import BeautifulSoup 

r = requests.get('https://www.ncsasports.org/mens-basketball/division-1-colleges')
soup = BeautifulSoup(r.text, 'html.parser')

data = []
for college in soup.find_all('div', {'class': 'column fifth college-list-college'}):
    d = {'College':''}
    d['College'] = college.a.text.strip()
    data.append(d)

division = []
for college in data:
    division.append(college['College'])

def div(x):
    if x in division:
        return 1
    else:
        return 0 

player['division'] = player['college'].apply(div)

re = requests.get('https://www.landofbasketball.com/hall_of_fame/hall_of_famers_by_year.htm')
fame = BeautifulSoup(re.text, 'html.parser')

data_2 = []
for name in fame.find_all('tr', {'class': 'a-top'}):
    d = {}
    d['Name'] = name.td.text.strip()
    data_2.append(d)

name = []
for x in data_2:
    name.append(x['Name'])

def fame(x):
    if x in name:
        return 1
    else:
        return 0 

player['fame'] = player['name'].apply(fame)

player.to_csv('Cleaned Player.csv', index = False)