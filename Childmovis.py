import pandas as pd
import numpy as np
import streamlit as st
from datetime import time

# Import the datasets 
kids = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/kids_imdb_rt1.csv')
directors = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/directors_rt_imdb1.csv')
genre = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/GenreQuestion.csv')

# Created the interval year slider 
date_range = st.slider('Choose the year interval:', 1900, 2022, value = (1990, 2000))

    # DIRECTORS : Question about the best movies per director 
st.subheader('What are the best movies of your favourite director?')

options_dir = st.selectbox('Choose the director:', directors['Director name'].unique())
                                
df_dir = directors[(directors['Director name']==options_dir) & (directors['Year'] > date_range[0]) & (directors['Year'] < date_range[1])].head(5)

#st.table(df_dir[['Movie title','Year','IMDb rating', 'Rotten Tomatoes rating']].sort_values(by=['IMDb rating','Year', 'Rotten Tomatoes rating'], ascending=False))

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(df_dir[['Movie title','Year','IMDb rating', 'Rotten Tomatoes rating']].sort_values(by=['IMDb rating','Year', 'Rotten Tomatoes rating'], ascending=False))

    # KIDS: Question about the best movies for kids 

st.subheader('Best movies for kids')

#st.subheader('*Where are the orders going to?*')

options_kids = st.selectbox('Choose the studio:', kids['Studio'].unique())
                            
df_mov = kids[(kids['Studio']==options_kids) & (kids['Year'] > date_range[0]) & (kids['Year'] < date_range[1])].head(5)#[['movie_title','tomatometer_rating']]
#df_mov.round({'IMDb rating': 2, 'Rotten Tomatoes rating': 2})
#df_mov.round(2)
#st.table(df_mov[['Movie Title', 'Year', 'Studio', 'IMDb rating', 'Rotten Tomatoes rating']].sort_values(by='Year', ascending=False))

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(df_mov[['Movie Title', 'Year', 'Studio', 'IMDb rating', 'Rotten Tomatoes rating']].sort_values(by=['IMDb rating','Year', 'Rotten Tomatoes rating'], ascending=False))

    # GENRE: Question about the genre 
st.subheader('What are the top 5 movies per genre and best reviews?')

options_genre = st.selectbox('Choose the genre you prefer:', genre['Genre'].unique())

df_genre = genre[(genre['Genre']==options_genre) & (genre['Year'] > date_range[0]) & (genre['Year'] < date_range[1])].head(5)

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.table(df_genre[['Movie title','Year','IMDb rating', 'Rotten Tomatoes rating', 'Genre']].sort_values(by=['IMDb rating'], ascending=False))

#'Rotten Tomatoes rating'

# PB with the interval of the data range[0] and [1] 

    # ACTORS: Question about the actors 
