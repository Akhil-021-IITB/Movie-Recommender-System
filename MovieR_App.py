import streamlit as st
import pickle
import pandas as pd

def recommend(movie, selected_movie_name):  # Pass selected_movie_name as a parameter
    index = movie[movie['title'] == selected_movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommend_movies = []
    for i in distances[1:6]:
        recommend_movies.append(movie.iloc[i[0]].title)
    return recommend_movies

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'How would you like to be contacted? ',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(movies, selected_movie_name)  # Pass movies and selected_movie_name as arguments
    for i in recommendations:
        st.write(i)

