import pandas as pd
import numpy as np
import streamlit as st
from datetime import time
from PIL import Image

# Import the datasets 
kids = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/kids_imdb_rt1.csv')
directors = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/directors_rt_imdb1.csv')
genre = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/GenreQuestion.csv')
actor = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project3MRS/main/bestactors.csv')

add_selectbox = st.sidebar.selectbox(
    "Select the topic you want",
    ['Introduction', 'Directors & Genres', "Actors & Actresses", "Kids & Family"],
    )

if add_selectbox == 'Introduction':

    image1 = Image.open('intro_picture.jpg')
    image1 = image1.resize((1200, 800))
    st.image(image1)


elif add_selectbox == 'Directors & Genres':


    # Created the interval year slider 
    date_range = st.slider('Choose the year interval:', 1900, 2022, value = (1990, 2000))

    image_director = Image.open('director_picto.png')
    image_director = image_director.resize((150, 150))
    st.image(image_director)


    # DIRECTORS : Question about the best movies per director 

    st.subheader('What are the best movies of your favourite director?')

    directors['Rotten Tomatoes rating'] = directors['Rotten Tomatoes rating']/10

    options_dir = st.selectbox('Choose the director:', directors['Director name'].unique())
                                    
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


#st.dataframe(df.style.format("{:.2%}"))
#st.table(df.style.format({'Quantidade': '{:.1f}', 'PVP': '{:.2f}', 'Dias de Venda': '{:.2f}'}))

    # GENRE: Question about the genre 

    image_genre = Image.open('genre_picto.png')
    image_genre = image_genre.resize((150, 150))
    st.image(image_genre)

    st.subheader('What are the top 5 movies per genre and best reviews?')

    options_genre = st.selectbox('Choose the genre you prefer:', genre['Genre'].unique())

    df_genre = genre[(genre['Genre']==options_genre) & (genre['Year'] >= date_range[0]) & (genre['Year'] <= date_range[1])]

    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.table(df_genre[['Movie title','Year','IMDb rating', 'Rotten Tomatoes rating', 'Genre']].sort_values(by=['IMDb rating'], ascending=False).head(5).style.format({'IMDb rating': '{:.1f}', 'Rotten Tomatoes rating': '{:.1f}'}))





elif add_selectbox == "Actors & Actresses":


    image_director = Image.open('actors_picto.png')
    image_director = image_director.resize((150, 150))
    # st.image(image_director, width = 150)
    st.image(image_director)

    # Try to round the IMDb and RT rating 
    #st.table(df_genre.style.format("{:.2%}"))

        # ACTORS: Question about the actors 
    st.subheader('What are the best Actors / Actresses?')

    actor['category'] = actor['category'].str.title()

    options_actors = st.selectbox('Choose the Actor / Actress:', actor['category'].unique())

    df_actor = actor[(actor['category']==options_actors)].head(10)

    st.table(df_actor[['Staff name','IMDb rating', 'Nb movies', 'Ranking']].sort_values(by=['Ranking'], ascending=False).style.format({'IMDb rating': '{:.1f}', 'Ranking': '{:.1f}'}))

    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    #st.table(df_dir[['Movie title','Year','IMDb rating', 'Rotten Tomatoes rating']].sort_values(by=['IMDb rating','Year', 'Rotten Tomatoes rating'], ascending=False))




else:


    date_range = st.slider('Choose the year interval:', 1900, 2022, value = (1990, 2000))


    # KIDS: Question about the best movies for kids 

    st.subheader('What are the best movies for kids?')

    #st.subheader('*Where are the orders going to?*')

    options_kids = st.selectbox('Choose the studio:', kids['Studio'].unique())
                                
    df_mov = kids[(kids['Studio']==options_kids) & (kids['Year'] >= date_range[0]) & (kids['Year'] <= date_range[1])]#[['movie_title','tomatometer_rating']]
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
    st.table(df_mov[['Movie Title', 'Year', 'Studio', 'IMDb rating', 'Rotten Tomatoes rating']].sort_values(by=['IMDb rating','Year', 'Rotten Tomatoes rating'], ascending=False).head(5).style.format({'IMDb rating': '{:.1f}', 'Rotten Tomatoes rating': '{:.1f}'}))

    image_kids = Image.open('child_pictures.png')
    #image_kids = image_kids.resize((600, 400))
    # st.image(image_kids, width = 150)
    st.image(image_kids)

