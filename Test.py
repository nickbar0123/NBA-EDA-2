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

global df
df = load_data('Merged.csv')

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

st.markdown(
    '''
    <body>
    <head>
    <style>
    h1 {
        color: #FF8C00;
        font-family: "Comic Sans MS", cursive, sans-serif;
        font-size: 300%;
        text-align: center;
        border: 1px solid red;
        font-weight: bold}
    h2 {
        color: #FF8C00;
        font-family: "Comic Sans MS", cursive, sans-serif;
        font-size: 200%;
        text-align: left;
        border-bottom: 1px solid red
        font-weight: bold;
    }
    p {
        color: #FF8C00;
        font-family: "Comic Sans MS", cursive, sans-serif;
        font-size: 100%;
    }
    </style>
    </head>
    </body>''', unsafe_allow_html = True
)




st.markdown(
    '<h1> NBA College Analysis </h1>', unsafe_allow_html= True)

image = Image.open('C:\Project_4\Kobe.jpeg')
st.image(image,use_column_width=True, caption = 'RIP Kobe')


st.dataframe(data = df)

'---'
st.markdown(
    '<h2>Analyzing Hall of Fame Players</h2>', unsafe_allow_html = True
)

seasons = ['First', 'Second', 'Third', 'Fourth']
options = st.selectbox(
    'Choose your stats',
    ('Average Points Scored', 'Average Block Rate', 'Average Assist Rate',
    'Average Steal Rate', 'Average Rebound Rate')
)

fig = go.Figure()

if options == 'Average Points Scored':
    points = [first_season, second_season, third_season, fourth_season]
    fig.add_trace(go.Bar(x = seasons, y = points))
    st.plotly_chart(fig)

if options == 'Average Block Rate':
    blocks = [first_season_blk, second_season_blk, third_season_blk, fourth_season_blk]
    fig.add_trace(go.Bar(x = seasons, y = blocks))
    st.plotly_chart(fig)

if options == 'Average Assist Rate':
    ast = [first_season_ast, second_season_ast, third_season_ast, fourth_season_ast]
    fig.add_trace(go.Bar(x = seasons, y = ast))
    st.plotly_chart(fig)

if options == 'Average Steal Rate':
    stl = [first_season_stl, second_season_stl, third_season_stl, fourth_season_stl]
    fig.add_trace(go.Bar(x = seasons, y = stl))
    st.plotly_chart(fig)

if options == 'Average Rebound Rate':
    rb = [first_season_rb, second_season_rb, third_season_rb, fourth_season_rb]
    fig.add_trace(go.Bar(x = seasons, y = rb))
    st.plotly_chart(fig)
'---'
st.markdown(
    '<h2>Distribution of Hall of Fame Players</h2>', unsafe_allow_html= True)

distribution = df[df['fame'] == 1]['division'].value_counts()
label = ['Division 1','Non-division 1']
fig, ax = plt.subplots(figsize = (5,5))
ax.pie(distribution, labels = label, autopct = '%1.2f%%', radius = 0.8)
ax.set_title('Overview of Hall of Fame Players', size = 12)
ax.legend(loc = 'upper right')
st.pyplot(use_container_width=True)

st.markdown(
    '<h2>Distribution within Divisions', unsafe_allow_html = True
)

division = df['division'].value_counts().tolist()
fig, ax = plt.subplots(figsize = (5,5))
ax.pie(division, labels = label, autopct = '%1.2f%%', radius = 0.8)
ax.set_title('Overview of NBA players')
ax.legend(loc = 'upper right')
st.pyplot(use_container_width = True)

'---'
st.markdown(
    '<h2>Analyzing Divisions</h2>', unsafe_allow_html = True
)
options = st.selectbox(
    'Choose your non-division 1 stats',
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
    ax.bar(seasons, points)
    ax.plot(threshold)
    st.pyplot()

if options == 'Average Block Rate':
    threshold = [first_season_blk, second_season_blk, third_season_blk, fourth_season_blk]
    first = df[(df['division'] == 0) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['BLK%'].mean()
    second = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['BLK%'].mean()
    third = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['BLK%'].mean()
    fourth = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['BLK%'].mean()
    points = [first,second,third,fourth]
    ax.bar(seasons, points)
    ax.plot(threshold)
    st.pyplot()

if options == 'Average Assist Rate':
    threshold = [first_season_ast, second_season_ast, third_season_ast, fourth_season_ast]
    first = df[(df['division'] == 0) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['AST%'].mean()
    second = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['AST%'].mean()
    third = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['AST%'].mean()
    fourth = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['AST%'].mean()
    assist = [first, second, third, fourth]
    ax.bar(seasons, assist)
    ax.plot(threshold)
    st.pyplot()

if options == 'Average Steal Rate':
    threshold = [first_season_stl, second_season_stl, third_season_stl, fourth_season_stl]
    first = df[(df['division'] == 0) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['STL%'].mean()
    second = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['STL%'].mean()
    third = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['STL%'].mean()
    fourth = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['STL%'].mean()
    stl = [first, second, third, fourth]
    ax.bar(seasons, stl)
    ax.plot(threshold)
    st.pyplot()

if options == 'Average Rebound Rate':
    threshold = [first_season_rb, second_season_rb, third_season_rb, fourth_season_rb]
    first = df[(df['division'] == 0) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['TRB%'].mean()
    second = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['TRB%'].mean()
    third = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['TRB%'].mean()
    fourth = df[(df['division'] == 0) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['TRB%'].mean()
    trb = [first, second, third, fourth]
    ax.bar(seasons, trb)
    ax.plot(threshold)
    st.pyplot()


options = st.selectbox('Choose your division 1 stats',
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
    ax.bar(seasons, points)
    ax.plot(threshold)
    st.pyplot()

if options == 'Average Block Rate':
    threshold = [first_season_blk, second_season_blk, third_season_blk, fourth_season_blk]
    first = df[(df['division'] == 1) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['BLK%'].mean()
    second = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['BLK%'].mean()
    third = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['BLK%'].mean()
    fourth = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['BLK%'].mean()
    points = [first,second,third,fourth]
    ax.bar(seasons, points)
    ax.plot(threshold)
    st.pyplot()

if options == 'Average Assist Rate':
    threshold = [first_season_ast, second_season_ast, third_season_ast, fourth_season_ast]
    first = df[(df['division'] == 1) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['AST%'].mean()
    second = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['AST%'].mean()
    third = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['AST%'].mean()
    fourth = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['AST%'].mean()
    assist = [first, second, third, fourth]
    ax.bar(seasons, assist)
    ax.plot(threshold)
    st.pyplot()

if options == 'Average Steal Rate':
    threshold = [first_season_stl, second_season_stl, third_season_stl, fourth_season_stl]
    first = df[(df['division'] == 1) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['STL%'].mean()
    second = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['STL%'].mean()
    third = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['STL%'].mean()
    fourth = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['STL%'].mean()
    stl = [first, second, third, fourth]
    ax.bar(seasons, stl)
    ax.plot(threshold)
    st.pyplot()

if options == 'Average Steal Rate':
    threshold = [first_season_stl, second_season_stl, third_season_stl, fourth_season_stl]
    first = df[(df['division'] == 1) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['STL%'].mean()
    second = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['STL%'].mean()
    third = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['STL%'].mean()
    fourth = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['STL%'].mean()
    stl = [first, second, third, fourth]
    ax.bar(seasons, stl)
    ax.plot(threshold)
    st.pyplot()

if options == 'Average Rebound Rate':
    threshold = [first_season_rb, second_season_rb, third_season_rb, fourth_season_rb]
    first = df[(df['division'] == 1) & (df['YEAR'] == df['year_start']) & (df['fame'] == 1)]['TRB%'].mean()
    second = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 1) & (df['fame'] == 1)]['TRB%'].mean()
    third = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 2) & (df['fame'] == 1)]['TRB%'].mean()
    fourth = df[(df['division'] == 1) & (df['YEAR'] == df['year_start'] + 3) & (df['fame'] == 1)]['TRB%'].mean()
    trb = [first, second, third, fourth]
    ax.bar(seasons, trb)
    ax.plot(threshold)
    st.pyplot()