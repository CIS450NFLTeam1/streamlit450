
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from st_btn_select import st_btn_select




st.title('CIS 450 NFL Data Exploration')
st.text('This dataset contains NFL game data from 1965-2019')

from st_btn_select import st_btn_select

page = st_btn_select(['Project Introduction','Data Statistics/Header','General Stats','Win/Loss Visualizations','Offensive Data','Defensive Data','ML Model'],nav=True)


#st.sidebar.title('Navigation')
#options = st.sidebar.radio('Pages', options = ['Project Introduction','Data Statistics/Header','General Stats','Win/Loss Visualizations','Offensive Data','Defensive Data','Machine Learning Model'])


df = pd.read_csv('streamlit_file.csv')
df_group = pd.read_csv('group_by.csv')
df_analysis = df.copy()
df_analysis.drop(['game_time_eastern','game_time_local','time_of_possession'],inplace = True,axis = 1)
full_groupby = df.groupby('team').agg('mean')[['points_for', 'points_against',
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


def defensive_plot():
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


if page == 'Project Introduction':
    home()
elif page == 'Data Statistics/Header':
    stats()
elif page == 'Win/Loss Visualizations':
    init_plots()
elif page == 'Offensive Data':
    offensive_plot()
elif page == 'Defensive Data':
    defensive_plot()
elif page == 'General Stats':
    general()
elif page == 'ML Model':
    ml()






