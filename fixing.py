from bs4 import BeautifulSoup
import requests
import pandas as pd 

df = pd.read_csv('Merged.csv')
df.drop(columns=['division'], inplace=True)

r = requests.get('https://en.wikipedia.org/wiki/List_of_NCAA_Division_I_institutions')
soup = BeautifulSoup(r.text, 'html.parser')

# get all the rows in table
rows = soup.find('table', {'class': 'sortable'}).find_all('tr')[1:]

# get all uni name
unis = set([u.a.text.strip().lower() for u in rows])
unis.remove('university of illinois at urbana–champaign')
unis.add('university of illinois at urbana-champaign')

# division 1 college:
div1 = set()
for x in df['college'].unique():
    for u in unis:
        if x.lower() in u:
            div1.add(x)
# change division
df['division'] = df['college'].apply(lambda x: 1 if x in div1 else 0)

df.to_csv('Fixed Merged.csv')