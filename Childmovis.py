import pandas as pd
import numpy as np
import streamlit as st
from datetime import time

movies = pd.read_csv('Downloads/out2 (5).csv')


st.title('Best movies for kids')

#st.subheader('*Where are the orders going to?*')
date_range = st.slider('Choose the year interval:', min_valuevalue = movies['year_release'])

options = st.selectbox('Choose the studio:', movies['Studio'].unique())
                 
                  
df_mov = movies[movies['Studio']==options & movies['Year']==date_range].head(5)#[['movie_title','tomatometer_rating']]
st.table(df_mov[['Movie Title','Rotten Tomatoes rating', 'Year']])