import pandas as pd
import numpy as np
import streamlit as st
from datetime import time

movies = pd.read_csv('Downloads/out2 (5).csv')


st.title('Best movies for kids')

#st.subheader('*Where are the orders going to?*')
#date_range = st.slider('Choose date interval:', value = movies['year_release'])

options = st.selectbox('Choose the studio:', movies['Studio'].unique())

#movies['year_release']= movies['year_release'].astype(int)

                  
                  
df_mov = movies[movies['Studio']==options].head(5)#[['movie_title','tomatometer_rating']]
st.table(df_mov[['Movie Title','Rotten Tomatoes rating', 'Year']])