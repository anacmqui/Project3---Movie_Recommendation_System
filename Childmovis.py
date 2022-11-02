import pandas as pd
import numpy as np
import streamlit as st
from datetime import time

kids = pd.read_csv('Documents/GitHub/Project3MRS/kids_imdb_rt1.csv')
#directors = pd.read_csv('Documents/GitHub/Project3MRS/Director question.csv')

date_range = st.slider('Choose the year interval:', 1910, 2022, value = (1990, 2000))

#st.subheader('What are the best movies of your favourite director?')

#options_dir = st.selectbox('Choose the director:', directors['Director name'].unique())
                            
#directors['Year'] = directors['Year'].apply(lambda x: int(x))
    
#df_dir = directors[(directors['Director name']==options_dir) & (directors['Year'] > date_range[0]) & (directors['Year'] < date_range[1])].head(5)

#st.table(df_dir[['Movie title','IMDb rating', 'Year']].sort_values(by=['IMDb rating','Year'], ascending=False))

st.subheader('Best movies for kids')

#st.subheader('*Where are the orders going to?*')


options_kids = st.selectbox('Choose the studio:', kids['Studio'].unique())
                            
df_mov = kids[(kids['Studio']==options_kids) & (kids['Year'] > date_range[0]) & (kids['Year'] < date_range[1])].head(5)#[['movie_title','tomatometer_rating']]
st.table(df_mov[['Movie Title', 'Year', 'Studio', 'IMDb rating', 'Rotten Tomatoes rating']].sort_values(by='Year', ascending=False))