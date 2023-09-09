import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=771467681cb027e511201ad372ffb961&language=en-US'.format(movie_id))
    data = response.json()
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=771467681cb027e511201ad372ffb961&language=en-US'.format(movie_id))
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list2 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list2:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        # Fetch Poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = pickle.load(open('movies.pkl','rb'))
movies_list3 = movies_list['title'].values

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select a Movie',
    movies_list3
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col_width = 250
    col1, col2, col3, col4, col5 = st.columns(5, gap = "large")

    with col1:
        st.write(names[0])
        st.image(posters[0])
    with col2:
        st.write(names[1])
        st.image(posters[1])
    with col3:
        st.write(names[2])
        st.image(posters[2])
    with col4:
        st.write(names[3])
        st.image(posters[3])
    with col5:
        st.write(names[4])
        st.image(posters[4])
