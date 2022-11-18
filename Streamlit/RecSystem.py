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

st.set_page_config(layout="wide")


def movie_recommendation():

    rec_sys['Year'] = rec_sys['startYear_x'].astype(str)
    rec_sys['title_year'] = rec_sys['primaryTitle']+' '+rec_sys['Year']

    options_reco = st.selectbox('Choose a movie:', rec_sys['title_year'].unique())

    X=rec_sys[['startYear_st', 'runtimeMinutes_st', 'averageRating_st', 'numVotes_st', 'action', 'adult', 'adventure' ,'animation' ,'biography', 'comedy', 'crime', 'documentary', 'drama', 'family', 'fantasy', 'fi', 'history' ,'horror' ,'music', 'musical', 'mystery' ,'news' ,'reality', 'romance' ,'sci' ,'sport' ,'thriller','tv', 'war' ,'western']]          

    model = NearestNeighbors(n_neighbors=6)
    model.fit(X)

    array_1, array_2 = model.kneighbors(rec_sys.loc[rec_sys['title_year'] == options_reco, ['startYear_st', 'runtimeMinutes_st', 'averageRating_st', 'numVotes_st', 'action', 'adult', 'adventure' ,'animation' ,'biography', 'comedy', 'crime', 'documentary', 'drama', 'family', 'fantasy', 'fi', 'history' ,'horror' ,'music', 'musical', 'mystery' ,'news' ,'reality', 'romance' ,'sci' ,'sport' ,'thriller','tv', 'war' ,'western']])

    index_array = array_2
    index_list = index_array.flatten().tolist() #to appear in vertical
    index_df = pd.DataFrame(index_list).rename(columns={0:'Index_array'})

    rec_sys.drop(['level_0'], axis=1, inplace=True)
    rec_sys.reset_index(inplace=True)
    Output_final=index_df.merge(rec_sys, how='left', left_on='Index_array', right_on='level_0')

    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    Output_final = Output_final.rename(columns = {'averageRating':'IMDb rating', 'primaryTitle':'Movie title',
                                                    'genres_x':'Genres'})
    return Output_final


def fetch_poster(movie_id):
    if movie_id==0:
      return ''
    else:
      url = "https://api.themoviedb.org/3/movie/{}?api_key=39976f73499bf65190665011272a5caf".format(movie_id)
      data = requests.get(url)
      data = data.json()
      poster_path = data['poster_path']
      full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
      return full_path


# STREAMLIT CODE



with st.expander("Try our Movie Recommendation System"):

    Output_final = movie_recommendation()
    movies_poster = pd.merge(Output_final, mov_poster, how='left', left_on='tconst', right_on='imdb_id')
    movies_poster['id'].fillna(0, inplace=True)
    movies_poster['poster'] = movies_poster['id'].apply(fetch_poster)

#st.table(movies_poster[['Movie title', 'Genres', 'IMDb rating', 'poster']].iloc[1:6].style.format({'IMDb rating': '{:.1f}'}))
    if st.button('Show Recommendation'):

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(movies_poster['Movie title'][1])
            if movies_poster['poster'][1]=='':
                st.empty()
            else:
                st.image(movies_poster['poster'][1])

        with col2:
            st.text(movies_poster['Movie title'][2])
            if movies_poster['poster'][2]=='':
                st.empty()
            else:
                st.image(movies_poster['poster'][2])
        with col3:
            st.text(movies_poster['Movie title'][3])
            if movies_poster['poster'][3]=='':
                st.empty()
            else:
                st.image(movies_poster['poster'][3])
        with col4:
            st.text(movies_poster['Movie title'][4])
            if movies_poster['poster'][4]=='':
                st.empty()
            else:
                st.image(movies_poster['poster'][4])
        with col5:
            st.text(movies_poster['Movie title'][5])
            if movies_poster['poster'][5]=='':
                st.empty()
            else:
                st.image(movies_poster['poster'][5])
                    

col1, col2 = st.columns(2)

with col1:
    if st.button('Enjoy your movie'):
        st.balloons()
with col2:
    st.empty()