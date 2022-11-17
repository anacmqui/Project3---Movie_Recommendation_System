# GitHub Documentation - Movie recommendation - Data Breakers


# Context 

A movie theater contacted us because he has decided to go digital by creating a website designed for local people.
Our client gave us a database of movies based on the IMDb platform and the database from Rotten Tomatoes complete with the reviews. Our goals were to do an analysis of these databases and to create a movie recommendation engine for our client.  

# Deliverables 
The first part of the project is an analysis of the database where we replied to those questions:
What are the best movies of your favorite director?
What are the top 5 movies per genre and best reviews?
What are the best Actors / Actresses?
What are the best movies for kids?

We also made statistics on those databases:
- The rating’s distribution
- Top 5 directors with the greatest number of films
- Number of votes per year and per movie
- Evolution of movie’s rating
- Critics vs Audience ratings in Rotten Tomatoes
- Rotten Tomatoes vs IMDb ratings
 
The second part of the project is a movie recommendation engine based on an algorithm that returns a list of recommended movies based on movie names chosen by a user. These recommendations are integrated into the “Machine Learning” folder.

All the code is in Github’s folders listed below. 

# GitHub folders - Description 

- FinalColabFiles: What is it? Those are the final Google Colaboratory files that reply to our questions. We also did the statistics on these files. 

- Machine Learning: Those are the code for the algorithms, the recommendation system and the input file.

- Exploratory Data Analysis: This is our initial analysis on the different datasets. 

- LinkingTables: Those are the tables we created to go from one file to another. 

- .ipynb_checkpoints: Those are the support files from Streamlit

- TablesForStreamlit: Those are the final tables we used for Streamlit.

- Old: We used these files before and kept them if necessary. 

- Pictures: This is the folder with the pictures we used for Streamlit.

- StreamlitFinal.py document: This is the final code for the Streamlit. 

# Pre-processing 

# Cleaning explanation
We chose to focus on movies so we excluded the other types (related to TV or video games) and also specific genres (Film-Noir, Game-Show, News, Reality-TV, Short, Talk-Show). 
We cleaned the tables and merged the one we needed to reply to the questions we had.

There were too many unknown movies with 10/10 rate, but not with a lot of votes, so we decided to reduce our dataset for only the movies with more than 6000 votes, which represents 5% of the initial dataset.Therefore, we excluded the movies with less number of votes. 

What is considered as a “best movie”? We defined the best movies as the ones that would belong to the list of the 1000 movies better ranked, from the 5% dataset. 
For the other queries, we decided to use only the 5% of the dataset also to present only the best movies with the best rates. 

# Navigate collab files and tables
1_FinalColabFiles

1) “Project3 - IMDB Title Principals.ipynb”

Goal: clean the table "title.principals"

IN:
-table "title.principals" from IMDb site

OUT:
-table ‘df_titleprincipals2.pickle’


  2) "Project3 - IMDB Title Basics.ipynb"

Goal: clean the table "title.basics"

IN:
-table "title.basics" from IMDb site
-table 'df_titlebasicsv2.pickle'

  3) "Filter_5_percent_movies.ipynb"

Goal: Main file, where the filters and merges where made. It's from here that the tables for Machine Learning algorithm are pushed.

IN:
-title_ratings (from IMDB)
-name_basics (from IMDB)
-"df_titleprincipals2.pickle" - from "Project3 - IMDB Title Principals.ipynb"
-"df_titlebasicsv2.pickle" - from "Project3 - IMDB Title Basics.ipynb"

OUT:
-'ppl_names_allmovies.csv' - Table with All the actors/actresses and movies
-'movies_5percent.csv' - Table with 5% of the movies, used for the other queries
-'bestactors.csv' - Table used for the query of the best 10 actors/actress from the 1000 best movies (best ranking) from the 5% more voted movies of the all dataset
-'df_ml_100_vect.pickle' - Table with all movies per genre, 1 line per movie, used for machine learning

  4) "ML_vectorize_Proj3.ipynb"

Goal: final file with the algorithm to show recommendations

IN:
-"df_ml_100_vect.pickle" - from "Filter_5_percent_movies.ipynb"

  5) RT - Kids movies & Clean dataset for join IMDB (Kaggle)

Goal: Find the best movies for kids based on the top studios

IN: 
-rotten_tomatoes_movies.csv (from: kaggle database)

OUT: 
- kids_movies.csv (to: colab 4)
- out4.csv (new column ‘dir_mov’ for join with IMDB) (to: colab 3 / colab 5)

  6) RT-IMDB merge + Directors.ipynb (Colab)

Goal: Join RT and IMDb tables // Get director’s table for streamlit 

IN: 
- out4.csv (from: colab 2)
- tprn_10 (from: colab 1)

OUT: 
- imdb_rt_ratings.csv (to: colab 4)
- directors_rt_imdb1.csv (to: streamlit / colab 5)

  7) Kids movies - IMDb and RT.ipynb (Colab)

Goal: Join rating from IMBd with kids table

IN: 
- imdb_rt_ratings.csv (from: colab 3)
- kids_movies.csv (from: colab 2)

OUT: 
- kids_imdb_rt1.csv (to: streamlit)

  8) Viz - ratings .ipynb

Goal: Statistics on ratings

IN: 
- out4.csv (from: colab 2)
- tprn_10.csv (from: colab 1)
- directors_rt_imdb1.csv (from: colab 3)

OUT (plots):
- IMDB ratings distribution 
- Evolution of movies’ ratings
- RT vs IMDB ratings

  9) Stats_directors_higher_nbmovies

Goal

IN:
- tprn_10.csv (from: colab 1)

OUT (plots):

  10) list_movies_by_genre.ipynb:

Goal: List of the movies by genre (5% most voted movies)

IN: 
- title.basics.tsv.gz (from: IMDb database)
- title.ratings.tsv.gz (from: IMDb database)
- Rating%20RT.csv

OUT:
- GenreQuestion.csv (to: streamlit)
 
 
# Machine Learning explanation
For the algorithm of the recommendation system we used an unsupervised model - NearestNeighbors - where, based on genre, number of votes, rating, year and runtime, our algorithm is able to suggest 5 movies with similar characteristics. 
We have standardized the variables ‘number of votes’, ‘rating’, ‘year’ and ‘runtime’ via MinMaxScaler() in order to attribute the maximum weight to the genres (dummies).


# Navigate colab files
ML_RecSystem (Colab)
Goal: Develop the algorithm for the recommendation system
IN: 
- df_ml_100_vect.csv (from: colab 1)
OUT: 
- output.csv (to: streamlit)

