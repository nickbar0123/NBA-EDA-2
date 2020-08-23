import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib as mpl 
from PIL import Image
import plotly.graph_objects as go

@st.cache
def load_data(path):
    data = pd.read_csv(path)
    return data 

xtitle = 'Season'
df = load_data('Fixed Merged.csv')

first_season = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'])]['PTS'].mean()
second_season = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 1)]['PTS'].mean()
third_season = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 2)]['PTS'].mean()
fourth_season = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 3)]['PTS'].mean()

first_season_blk = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'])]['BLK%'].mean()
second_season_blk = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 1)]['BLK%'].mean()
third_season_blk = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 2)]['BLK%'].mean()
fourth_season_blk = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 3)]['BLK%'].mean()

first_season_ast = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'])]['AST%'].mean()
second_season_ast = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 1)]['AST%'].mean()
third_season_ast = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 2)]['AST%'].mean()
fourth_season_ast = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 3)]['AST%'].mean()

first_season_stl = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'])]['STL%'].mean()
second_season_stl = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 1)]['STL%'].mean()
third_season_stl = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 2)]['STL%'].mean()
fourth_season_stl = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 3)]['STL%'].mean()

first_season_rb = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'])]['TRB%'].mean()
second_season_rb = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 1)]['TRB%'].mean()
third_season_rb = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 2)]['TRB%'].mean()
fourth_season_rb = df[(df['fame'] == 1) & (df['YEAR'] == df['year_start'] + 3)]['TRB%'].mean()

#Setting style 
st.markdown(
    '''
    <head>
    <link href="https://fonts.googleapis.com/css2?family=Alata&display=swap" rel="stylesheet">
    <style>
    h1 {
        color: #C9082A;
        font-family: "Alata", sans-serif;
        font-size: 300%;
        text-align: center;
        border: 1px solid #C9082A;
        font-weight: bold}
    h2 {
        color: #C9082A;
        font-family: "Alata", sans-serif;
        font-size: 200%;
        text-align: left;
        border-bottom: 1px solid #C9082A;
        font-weight: bold;
    }
    p {
        color: #C9082A;
        font-family: "Alata", sans-serif;
        font-size: 150%;
    }
    </style>
    </head>
    ''', unsafe_allow_html = True) 



st.markdown(
    '<h1> NBA College Analysis </h1>', unsafe_allow_html= True)

image = Image.open('C:\Project_4\Kobe.jpeg')
st.image(image,use_column_width=True, caption = 'RIP Kobe')

st.markdown(
    '''<p> For many aspiring NBA players, the college experience is integral to their future pursuits. 
    This report will analyze how different collegiate divisions impact players on the NBA landscape.</p>''', unsafe_allow_html = True
)

'---'
st.markdown(
    '<h2>Analyzing Hall of Fame Players</h2>', unsafe_allow_html = True
)



seasons = ['First', 'Second', 'Third', 'Fourth']
options = st.selectbox(
    'Choose your stat',
    ('Average Points Scored', 'Average Block Rate', 'Average Assist Rate',
    'Average Steal Rate', 'Average Rebound Rate')
)

fig, ax = plt.subplots()

if options == 'Average Points Scored':
    points = [first_season, second_season, third_season, fourth_season]
    ax.bar(seasons, points, color = '#17408B', width = 0.5)
    ax.set(xlabel = xtitle, ylabel = 'Average Points Scored')
    st.pyplot()

if options == 'Average Block Rate':
    blocks = [first_season_blk, second_season_blk, third_season_blk, fourth_season_blk]
    ax.bar(seasons, blocks, color = '#17408B', width = 0.5)
    ax.set(xlabel = xtitle, ylabel = 'Average Block Rate')
    st.pyplot()

if options == 'Average Assist Rate':
    ast = [first_season_ast, second_season_ast, third_season_ast, fourth_season_ast]
    ax.bar(seasons, ast, color = '#17408B', width = 0.5)
    ax.set(xlabel = xtitle, ylabel = 'Average Assist Rate')
    st.pyplot()

if options == 'Average Steal Rate':
    stl = [first_season_stl, second_season_stl, third_season_stl, fourth_season_stl]
    ax.bar(seasons, stl, color = '#17408B', width = 0.5)
    ax.set(xlabel = xtitle, ylabel = 'Average Assist Rate')
    st.pyplot()

if options == 'Average Rebound Rate':
    rb = [first_season_rb, second_season_rb, third_season_rb, fourth_season_rb]
    ax.bar(seasons, rb, color = '#17408B', width = 0.5)
    ax.set(xlabel = xtitle, ylabel = 'Average Assist Rate')
    st.pyplot()
'---'
st.markdown(
    '<h2>Distribution of Hall of Fame Players</h2>', unsafe_allow_html= True)

distribution = df[df['fame'] == 1]['division'].value_counts()
label = ['Division 1','Non-division 1']
fig, ax = plt.subplots(figsize = (5,5))
ax.pie(distribution, labels = label, autopct = '%1.2f%%', radius = 0.8, colors = ('#17408B', '#C9082A'))
ax.set_title('Overview of Hall of Fame Players', size = 12)
ax.legend(loc = 'upper right')
st.pyplot(use_container_width=True)

'---'
st.markdown(
    '<h2>Analyzing Divisions</h2>', unsafe_allow_html = True
)

options = st.selectbox(
    'Choose your non-division 1 stat',
    ('Average Points Scored', 'Average Block Rate', 'Average Assist Rate',
    'Average Steal Rate', 'Average Rebound Rate')
)
fig, ax = plt.subplots()
if options == 'Average Points Scored':
    threshold = [first_season, second_season, third_season, fourth_season]
    first = df[(df['division'] == 0) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['PTS'].mean()
    second = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['PTS'].mean()
    third = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['PTS'].mean()
    fourth = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['PTS'].mean()
    points = [first,second,third,fourth]
    ax.bar(seasons, points, color = '#17408B', width = 0.5)
    ax.plot(threshold, color = '#C9082A')
    ax.set(xlabel = xtitle, ylabel = 'Average Points Scored')
    st.pyplot()

if options == 'Average Block Rate':
    threshold = [first_season_blk, second_season_blk, third_season_blk, fourth_season_blk]
    first = df[(df['division'] == 0) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['BLK%'].mean()
    second = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['BLK%'].mean()
    third = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['BLK%'].mean()
    fourth = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['BLK%'].mean()
    points = [first,second,third,fourth]
    ax.bar(seasons, points, color = '#17408B', width = 0.5)
    ax.plot(threshold, color = '#C9082A')
    ax.set(xlabel = xtitle, ylabel = 'Average Block Rate')
    st.pyplot()

if options == 'Average Assist Rate':
    threshold = [first_season_ast, second_season_ast, third_season_ast, fourth_season_ast]
    first = df[(df['division'] == 0) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['AST%'].mean()
    second = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['AST%'].mean()
    third = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['AST%'].mean()
    fourth = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['AST%'].mean()
    assist = [first, second, third, fourth]
    ax.bar(seasons, assist, color = '#17408B', width = 0.5)
    ax.plot(threshold, color = '#C9082A')
    ax.set(xlabel = xtitle, ylabel = 'Average Assist Rate')
    st.pyplot()

if options == 'Average Steal Rate':
    threshold = [first_season_stl, second_season_stl, third_season_stl, fourth_season_stl]
    first = df[(df['division'] == 0) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['STL%'].mean()
    second = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['STL%'].mean()
    third = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['STL%'].mean()
    fourth = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['STL%'].mean()
    stl = [first, second, third, fourth]
    ax.bar(seasons, stl, color = '#17408B', width = 0.5)
    ax.plot(threshold, color = '#C9082A')
    ax.set(xlabel = xtitle, ylabel = 'Average Steal Rate')
    st.pyplot()

if options == 'Average Rebound Rate':
    threshold = [first_season_rb, second_season_rb, third_season_rb, fourth_season_rb]
    first = df[(df['division'] == 0) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['TRB%'].mean()
    second = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['TRB%'].mean()
    third = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['TRB%'].mean()
    fourth = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['TRB%'].mean()
    trb = [first, second, third, fourth]
    ax.bar(seasons, trb, color = '#17408B', width = 0.5)
    ax.plot(threshold, color = '#C9082A')
    ax.set(xlabel = xtitle, ylabel = 'Average Rebound Rate')
    st.pyplot()


options = st.selectbox('Choose your division 1 stat',
            ('Average Points Scored', 'Average Block Rate',
            'Average Assist Rate', 'Average Steal Rate',
            'Average Rebound Rate'))

fig, ax = plt.subplots()
if options == 'Average Points Scored':
    threshold = [first_season, second_season, third_season, fourth_season]
    first = df[(df['division'] == 1) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['PTS'].mean()
    second = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['PTS'].mean()
    third = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['PTS'].mean()
    fourth = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['PTS'].mean()
    points = [first,second,third,fourth]
    ax.bar(seasons, points, color = '#17408B', width = 0.5)
    ax.plot(threshold, color = '#C9082A')
    ax.set(xlabel = xtitle, ylabel = 'Average Points Scored')
    st.pyplot()

if options == 'Average Block Rate':
    threshold = [first_season_blk, second_season_blk, third_season_blk, fourth_season_blk]
    first = df[(df['division'] == 1) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['BLK%'].mean()
    second = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['BLK%'].mean()
    third = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['BLK%'].mean()
    fourth = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['BLK%'].mean()
    points = [first,second,third,fourth]
    ax.bar(seasons, points, color = '#17408B', width = 0.5)
    ax.plot(threshold, color = '#C9082A')
    ax.set(xlabel = xtitle, ylabel = 'Average Block Rate')
    st.pyplot()

if options == 'Average Assist Rate':
    threshold = [first_season_ast, second_season_ast, third_season_ast, fourth_season_ast]
    first = df[(df['division'] == 1) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['AST%'].mean()
    second = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['AST%'].mean()
    third = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['AST%'].mean()
    fourth = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['AST%'].mean()
    assist = [first, second, third, fourth]
    ax.bar(seasons, assist, color = '#17408B', width = 0.5)
    ax.plot(threshold, color = '#C9082A')
    ax.set(xlabel = xtitle, ylabel = 'Average Assist Rate')
    st.pyplot()

if options == 'Average Steal Rate':
    threshold = [first_season_stl, second_season_stl, third_season_stl, fourth_season_stl]
    first = df[(df['division'] == 1) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['STL%'].mean()
    second = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['STL%'].mean()
    third = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['STL%'].mean()
    fourth = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['STL%'].mean()
    stl = [first, second, third, fourth]
    ax.bar(seasons, stl, color = '#17408B', width = 0.5)
    ax.plot(threshold, color = '#C9082A')
    ax.set(xlabel = xtitle, ylabel = 'Average Steal Rate')
    st.pyplot()

if options == 'Average Rebound Rate':
    threshold = [first_season_rb, second_season_rb, third_season_rb, fourth_season_rb]
    first = df[(df['division'] == 1) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['TRB%'].mean()
    second = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['TRB%'].mean()
    third = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['TRB%'].mean()
    fourth = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['TRB%'].mean()
    trb = [first, second, third, fourth]
    ax.bar(seasons, trb, color = '#17408B',  width = 0.5)
    ax.plot(threshold, color = '#C9082A')
    ax.set(xlabel = xtitle, ylabel = 'Average Rebound Rate')
    st.pyplot()

'---'
st.markdown(
    '<h2>Which division 1 college should you attend?</h2>', unsafe_allow_html = True
)


colleges = df[df['division'] == 1].groupby('college')['name'].count().sort_values(ascending = False).head(5).index.tolist()

options = st.selectbox('Choose College', options = (['Top 5'] + colleges))
graph = pd.crosstab(df[(df['YEAR'] > 2000)]['YEAR'], df[df['college'].isin(colleges)]['college'])

fig, ax = plt.subplots()
if options == 'Top 5':
    ax.plot(graph, marker = '.')
    ax.legend(colleges, fontsize = 6)
    ax.set(xlabel = 'Year', ylabel = 'Number of Players')
    st.pyplot()
else:
    for college in colleges:
        if college == options and college != 'All':
            ax.plot(graph[college], marker = '.')
            ax.set(xlabel = 'Year', ylabel = 'Number of Players')
            fig.legend([college], loc = 1)
            st.pyplot()

st.markdown(
    '<h2>Distribution of Hall of Fame Players</h2>', unsafe_allow_html = True
)

colleges = df[(df['division'] == 1) | (df['college'].str.contains('Unknown'))].groupby('college')['name'].count().sort_values(ascending = False).head(5).index.tolist()
fame = df[(df['college'].isin(colleges)) & (df['fame'] == 1)].groupby('college')['name'].count().sort_values(ascending = False).head(5).tolist()
total = df[(df['division'] == 1) | (df['college'].str.contains('Unknown'))].groupby('college')['name'].count().sort_values(ascending = False).head(5).tolist()

fig, ax = plt.subplots()

ax.bar(colleges, total, color = '#17408B', width = 0.5)
ax.bar(colleges, fame, color = '#C9082A', width = 0.5)
ax.set(xlabel = 'College', ylabel = 'Number of Players')
fig.legend(['Division 1', 'Hall of Fame Players'], loc=1)
fig.autofmt_xdate(rotation='vertical')
st.pyplot()

# uni = df.groupby('college').count().sort_values(by = 'name', ascending = False).reset_index().head(31)
# def get_division(name):

#     division = df[df['college'].isin([name])]['division'].unique()[0]



# def get_fame_player(college):
#     n_fames = df[(df['college'] == college) & df['fame'] == 1].groupby('college').count()['name'].max()
#     return n_fames

# fig, ax = plt.subplots( figsize=(10, 8))

# colors = ['orange'  if  get_division(x) == 0 else 'blue' for x in uni['college']]
# fames = [get_fame_player(x) for x in uni['college']]

# ax.bar(uni['college'], uni['name'], color=colors)
# ax.bar(uni['college'], fames, color ='red')

# fig.legend(['Non-division 1', 'Hall of Fame Players', 'Division 1'], loc=1)

# fig.autofmt_xdate(rotation='vertical')
# st.pyplot()


# colleges = df[df['division'] == 0].groupby('college')['name'].count().sort_values(ascending = False).head(5).index.tolist()
# options = st.selectbox('Choose College', options = (['Top 5'] + colleges))
# graph = pd.crosstab(df[(df['YEAR'] > 2000)]['YEAR'], df[df['college'].isin(colleges)]['college'])
# fig = go.Figure()

# figure, ax = plt.subplots()
# if options == 'Top 5':
#     ax.plot(graph, marker = '.')
#     ax.legend(colleges, loc = 'upper left', fontsize = 6)
#     ax.set(xlabel = 'Year', ylabel = 'Number of Players')
#     st.pyplot()
# else:
#     for college in colleges:
#         if college == options and college != 'All':
#             ax.plot(graph[college], marker = '.')
#             ax.set(xlabel = 'Year', ylabel = 'Number of Players')
#             st.pyplot()

  





