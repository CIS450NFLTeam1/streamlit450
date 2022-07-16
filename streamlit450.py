
from pickle import TRUE
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
st.set_page_config(layout="wide")


st.title('CIS 450 NFL Data Exploration')
st.text('This dataset contains NFL game data from 1965-2019')

st.sidebar.title('Nagivation')
options = st.sidebar.radio('Pages',options = ['Introduction','Data Overview','General Stats','Win/Loss Stats','Win vs. Loss','Offensive/Defensive Leaders','Game Prediction (Draft)'])


df = pd.read_csv('streamlit_file.csv')
df_group = pd.read_csv('group_by2.CSV')
df_analysis = df.copy()
df_analysis.drop(['game_time_eastern','game_time_local'],inplace = True,axis = 1)
full_groupby = df.groupby('team').agg('mean')[['points_for', 'points_against',
       'point_diff', 'previous_week_point_diff', 'points_combined',
       'completions', 'pass_attempts', 'completion_pct', 'passing_yards',
       'passing_tD', 'Int', 'sacks', 'sack_yards', 'qb_rating',
       'rush_attempts', 'rush_yards', 'rush_yards_per_attempt', 'rush_td',
       'total_yards', 'o_num_plays', 'o_yards_per_play', 'd_num_plays',
       'd_yards_per_play', 'turnovers_lost']]
win_loss_mean = df.groupby('win_loss_num').agg('mean')[['points_for', 'points_against',
       'point_diff', 'previous_week_point_diff', 'points_combined',
       'completions', 'pass_attempts', 'completion_pct', 'passing_yards',
       'passing_tD', 'Int', 'sacks', 'sack_yards', 'qb_rating',
       'rush_attempts', 'rush_yards', 'rush_yards_per_attempt', 'rush_td',
       'total_yards', 'o_num_plays', 'o_yards_per_play', 'd_num_plays',
       'd_yards_per_play', 'turnovers_lost']]


def home():
    
    st.subheader('This is a web app for CIS 450, NFL Data Group 1')
    st.subheader('In this application, we will showcase a number of features surrounding our data') 
    st.markdown('* A general overview of the dataset we will be utilizing to perform our analysis')
    st.markdown('* A summation of general statistics, offensive statistics, and defensive statistics')
    st.markdown('* A machine learning model that can predict the outcome of a game better than the flip of a coin')
    st.text('')
    st.text('(Navigate to other pages by clicking arrow in top left)')
    st.subheader('Group Members:')
    st.text('Matthew Bierman, Ben Reeder, Kyle Kriho, Chris Homren, and Ricardo Dinatale') 
    st.image('nfl.jpg')
    st.markdown("https://app.powerbi.com/groups/me/reports/7777a2cc-c206-4299-86de-531705b8a581/ReportSection",unsafe_allow_html= True)
    st.text('New')


def general():
    st.header('General Statistics')
    st.subheader('Number of games started at each hour (EST)')
    fig4 = px.bar(df['game_hour'].value_counts(),df['game_hour'].value_counts().index,df['game_hour'].value_counts().values)
    st.plotly_chart(fig4)
    st.subheader("Number of games that started in each 'Time Slot'")
    st.markdown('* First Slot - 10-2 EST')
    st.markdown('* Second Slot - 3-5 EST') 
    st.markdown('* Third Slot - 6-9 EST')
    fig5 = px.bar(df['time_of_day'].value_counts(),df['time_of_day'].value_counts().index,df['time_of_day'].value_counts().values)
    st.plotly_chart(fig5)
    st.subheader('Count of games by the day of the week that they were played on')
    fig6 = px.bar(df['Day'].value_counts(),df['Day'].value_counts().index,df['Day'].value_counts().values)
    st.plotly_chart(fig6)
    st.subheader('Count of whether games ended in OT or Regulation')
    fig6 = px.bar(df['OT'].value_counts(),df['OT'].value_counts().index,df['OT'].value_counts().values)
    st.plotly_chart(fig6)


def stats():
    st.header('Data Statistics/Header')
    st.subheader('General Data Statistics:')
    st.write(df_analysis.describe())
    st.subheader('Head of Data:')
    st.write(df_analysis.head())


def init_plots():
    st.header('Win/Loss Visualizations')
    if st.checkbox('Show dataframe'):
        st.text('Sort by clicking on column header')
        st.dataframe(df_group)
    st.header('Total Wins')
    fig = px.bar(df_group, x=df_group.sort_values('wins',ascending = False)['team'], y=df_group.sort_values('wins',ascending = False)['wins'].values,color = df_group.sort_values('wins',ascending = False)['wins'].values )
    st.plotly_chart(fig)
    st.header('Total Games Played')
    fig8 = px.bar(df_group, x=df_group.sort_values('total_games',ascending = False)['team'], y=df_group.sort_values('total_games',ascending = False)['total_games'].values,color = df_group.sort_values('total_games',ascending = False)['total_games'].values )
    st.plotly_chart(fig8)
    st.header('Win Percentage')
    fig9 = px.bar(df_group, x=df_group.sort_values('win_pct',ascending = False)['team'], y=df_group.sort_values('win_pct',ascending = False)['win_pct'].values,color = df_group.sort_values('win_pct',ascending = False)['win_pct'].values )
    st.plotly_chart(fig9)




def offensive_plot():
    st.header('Offensive Visualizations')
    st.subheader('These visualizations show the Top 10 teams in average offensive output by the field selected')
    sort_option_o = st.selectbox('Select field to Show Graph for',options = ['completions', 'pass_attempts', 'completion_pct', 'passing_yards',
       'passing_tD', 'Int', 'sacks', 'sack_yards', 'qb_rating',
       'rush_attempts', 'rush_yards', 'rush_yards_per_attempt', 'rush_td',
       'total_yards', 'o_num_plays', 'o_yards_per_play', 'turnovers_lost'])
    if st.checkbox('Show Table'):
        st.table(full_groupby.sort_values(sort_option_o,ascending = False)[:10][sort_option_o])
    fig2 = px.bar(full_groupby, x=full_groupby.sort_values(sort_option_o,ascending = False)[:10].index, y=full_groupby.sort_values(sort_option_o,ascending = False)[:10][sort_option_o].values,color = full_groupby.sort_values(sort_option_o,ascending = False)[:10][sort_option_o].values )
    st.plotly_chart(fig2)
    st.header('Defensive Visualizations')
    st.subheader('These visualizations show Teams by average defensive output by the field selected')
    st.header('Defensive Number of Plays')
    if st.checkbox('Show  Defensive Number of Plays Table'):
        st.text('Sort by clicking on column header')
        st.dataframe(full_groupby['d_num_plays'])
    fig3 = px.bar(full_groupby, x=full_groupby.sort_values('d_num_plays',ascending = False).index, y=full_groupby.sort_values('d_num_plays',ascending = False)['d_num_plays'].values,color = full_groupby.sort_values('d_num_plays',ascending = False)['d_num_plays'].values )
    st.plotly_chart(fig3)
    st.header('Defensive Yards per Play')
    if st.checkbox('Show  Defensive Yards per Play Table'):
        st.text('Sort by clicking on column header')
        st.dataframe(full_groupby['d_yards_per_play'])
    fig3 = px.bar(full_groupby, x=full_groupby.sort_values('d_yards_per_play',ascending = False).index, y=full_groupby.sort_values('d_yards_per_play',ascending = False)['d_yards_per_play'].values,color = full_groupby.sort_values('d_yards_per_play',ascending = False)['d_yards_per_play'].values )
    st.plotly_chart(fig3)
    st.header('From this data we can gather that:')
    st.markdown('* There is not much variation in the defensive stats that we have at hand')
    st.markdown('* These defensive statistics may not be of much use when predicting W/L')



def ml():
    st.header('Logistic Regression/Decision Tree model creation in progress')
    st.subheader('On this page, we plan to showcase our Machine Learning Model based off of user input. ')
    st.markdown('* User will be able to select a game to be played')
    st.markdown('* Based on our model and the user input, the user will see whether a Win or Loss is predicted')
    st.markdown('* The user should also be able to see our models confidence in prediction')
    st.subheader('(These values are not based on a model, they are just hardcoded to demonstrate our plan to display our model)')
    game_played = st.selectbox('Choose a game to be Played:',['ARI @ WAS', 'TAM @ PIT','....'])
    st.subheader('Here we will showcase the fields that are most valuable in predicting a win. For example:')
    if game_played == '....':
        pass
    else:
        st.write('The Home Team is',game_played.split('@')[1], 'and the Away team is',game_played.split('@')[0])
    st.write('The game will be played at 1 P.M. EST')
    st.write('In their previous games', game_played.split('@')[1],'won and ', game_played.split('@')[0],'lost' )
    st.write("We predict that", game_played.split('@')[1],"will win with 68.2% confidence")

    # team_pick = st.selectbox('Choose a Home Team:',df_group.sort_values('team')['team'].values)
    # opp_pick = st.selectbox('Choose an Away Team:',df_group.sort_values('team', ascending = False)['team'].values)
    # if team_pick == opp_pick:
    #     st.write('Choose an opponent other than',team_pick)
    # else:
    #     prev_home = st.selectbox('Previous Result For Home Team:',['Won','Lost/Tied'])
    #     prev_away = st.selectbox('Previous Result For Away Team:',['Won','Lost/Tied'])
    #     day_of_game = st.selectbox('Day Game will be Played: ',['Sunday','Monday','Thursday'])
    #     tod = st.selectbox('Time Slot:',['First Slot (Early Afternoon)','Second Slot (Afternoon)','Last Slot (Night)'])
    #     st.subheader('Variables Chosen:')
    #     st.write( opp_pick, ' @ ', team_pick)
    #     st.write('In their previous games,',team_pick, prev_home,' and', opp_pick, prev_away)
    #     st.write('The game will be played on',day_of_game)
    #     st.write('The game will be played in the ', tod)
    #     st.header('Prediction:')
    #     st.text("We predict 'Winning Team variable' will win with 'Model-Based Confidence'")


def wvsl():
    win_v_loss = st.selectbox('Select a Statistical Field',win_loss_mean.columns)
    col1,col2 = st.columns(2)
    col1.metric('Loss:',np.round(win_loss_mean.loc[0][win_v_loss],2))
    col2.metric('Win:',np.round(win_loss_mean.loc[1][win_v_loss],2))
    st.markdown("https://app.powerbi.com/groups/me/reports/a3f44c6e-e692-49b7-9b4e-912f074f1ebe/ReportSectionab3a9f1618ddae25a6c5",unsafe_allow_html= True)
    


if options == 'Introduction':
    home()
elif options == 'Data Overview':
    stats()
elif options == 'Win/Loss Stats':
    init_plots()
elif options == 'Offensive/Defensive Leaders':
    offensive_plot()
elif options == 'General Stats':
    general()
elif options == 'Game Prediction (Draft)':
    ml()
elif options == 'Win vs. Loss':
    wvsl()






