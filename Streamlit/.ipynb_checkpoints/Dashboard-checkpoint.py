import pandas as pd
import numpy as np
import streamlit as st
import requests
import json
from datetime import time
from PIL import Image
import sklearn
from sklearn.neighbors import NearestNeighbors
import streamlit_book as stb

# Import the datasets 
kids = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/6_TablesForStreamlit/kids_imdb_rt1.csv')
directors = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/6_TablesForStreamlit/directors_rt_imdb1.csv')
genre = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/6_TablesForStreamlit/GenreQuestion.csv')
actor = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/6_TablesForStreamlit/bestactors.csv')
rec_sys = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/4_LinkingTables/movies_reco_system_5.csv')
mov_poster = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/4_LinkingTables/tmdb_10.csv')


#add_selectbox = st.sidebar.selectbox(
 #   "Select the topic you want",
  #  ['Dashboard', 'Recommendation System'])

# Introduction
#image1 = Image.open('8_Pictures/intro_picture.jpg')
#image1 = image1.resize((1200, 800))

# Directors & Genres
image_director = Image.open('8_Pictures/director_picto.png')
image_director = image_director.resize((150, 150))

directors['Rotten Tomatoes rating'] = directors['Rotten Tomatoes rating']/10

image_genre = Image.open('8_Pictures/genre_picto.png')
image_genre = image_genre.resize((150, 150))

# Actors & Actresses
image_actor = Image.open('8_Pictures/actors_picto.png')
image_actor = image_actor.resize((150, 150))

# Kids & Family
image_kidspicto = Image.open('8_Pictures/forkid_picto.png')
image_kidspicto = image_kidspicto.resize((150, 150))
#image_kids = Image.open('8_Pictures/child_pictures.png')
#image_kids = image_kids.resize((600, 400))

# Movie Recommendation 

kids = kids[kids['Studio'].notna()]


# STREAMLIT CODE


st.markdown("<h1 style='text-align: center; color: black;'>Movie Theather Dashboard</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color: black;'>Find the best movies for your audience</h2>", unsafe_allow_html=True)

#if add_selectbox == 'Dashboard':

    # image1 = Image.open('/../8_Pictures/intro_picture.jpg')
    
    #st.image(image1)

    # Created the interval year slider 

col1, col2, col3 = st.columns(3)    
with col1:
    st.empty()
with col2:
    date_range = st.slider('Choose the year interval:', 1900, 2022, value = (1990, 2000))
with col3:
    st.empty()

    
col1, col2 = st.columns(2)
with col1:
        st.image(image_director)
        #st.markdown(<p style='text-align: center; color: grey;'>"+img_to_html('8_Pictures/director_picto.png')+"</p>", unsafe_allow_html=True)
# DIRECTORS : Question about the best movies per director 
        
        st.subheader('What are the best movies of your favourite director?')

        options_dir = st.selectbox('Choose the director:', directors['Director name'].unique(), 1)
        
        df_dir = directors[(directors['Director name']==options_dir) & (directors['Year'] >= date_range[0]) & (directors['Year'] <= date_range[1])]

#st.table(df_dir[['Movie title','Year','IMDb rating', 'Rotten Tomatoes rating']].sort_values(by=['IMDb rating','Year', 'Rotten Tomatoes rating'], ascending=False))

        hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df_dir[['Movie title','Year','IMDb rating', 'Rotten Tomatoes rating']].sort_values(by=['IMDb rating','Year', 'Rotten Tomatoes rating'], ascending=False).head(5).style.format({'IMDb rating': '{:.1f}', 'Rotten Tomatoes rating': '{:.1f}'}))

# GENRE: Question about the genre 
with col2:
        st.image(image_genre)

        st.subheader('What are the best movies of your favourite genre?')

        options_genre = st.selectbox('Choose the genre you prefer:', genre['Genre'].unique())

        df_genre = genre[(genre['Genre']==options_genre) & (genre['Year'] >= date_range[0]) & (genre['Year'] <= date_range[1])]

        hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        st.table(df_genre[['Movie title','Year','IMDb rating', 'Rotten Tomatoes rating']].sort_values(by=['IMDb rating'], ascending=False).head(5).style.format({'IMDb rating': '{:.1f}', 'Rotten Tomatoes rating': '{:.1f}'}))



# ACTORS: Question about the actors 
col1, col2 = st.columns(2)
with col1:
    st.image(image_actor)
    st.subheader('Who are the most popular Actors / Actresses?')

    actor['category'] = actor['category'].str.title()

    options_actors = st.selectbox('Choose the Actor / Actress:', actor['category'].unique())

    df_actor = actor[(actor['category']==options_actors)].head(5)

    st.table(df_actor[['Staff name','IMDb rating', 'Nb movies', 'Ranking']].sort_values(by=['Ranking'], ascending=False).style.format({'IMDb rating': '{:.1f}', 'Ranking': '{:.1f}'}))

    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

#date_range = st.slider('Choose the year interval:', 1900, 2022, value = (1990, 2000))

# KIDS: Question about the best movies for kids 
with col2:
    st.image(image_kidspicto)
    st.subheader('What are the best movies for kids?')

#st.subheader('*Where are the orders going to?*')

    options_kids = st.selectbox('Choose the studio:', kids['Studio'].unique())

    df_mov = kids[(kids['Studio']==options_kids) & (kids['Year'] >= date_range[0]) & (kids['Year'] <= date_range[1])]#[['movie_title','tomatometer_rating']]
#df_mov.round({'IMDb rating': 2, 'Rotten Tomatoes rating': 2})
#df_mov.round(2)
#st.table(df_mov[['Movie Title', 'Year', 'Studio', 'IMDb rating', 'Rotten Tomatoes rating']].sort_values(by='Year', ascending=False))

    st.table(df_mov[['Movie Title', 'Year', 'IMDb rating', 'Rotten Tomatoes rating']].sort_values(by=['IMDb rating','Year', 'Rotten Tomatoes rating'], ascending=False).head(5).style.format({'IMDb rating': '{:.1f}', 'Rotten Tomatoes rating': '{:.1f}'}))
    
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    #st.image(image_kids)