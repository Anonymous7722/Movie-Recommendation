import streamlit as st
import pandas as pd
import pickle
import requests
import json


movies_dict=pickle.load(open('movies.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))
new_pt=pd.DataFrame(movies_dict)


st.title('Movie Recommender System')

option = st.selectbox(
"Enter Movie name for Recommendation",
new_pt['title'].values,
index=None,
placeholder="Select the Movie...",
)




def get_poster(id):
    poster_list=[]
    for i in id:
        resposne = requests.get(f'https://api.themoviedb.org/3/movie/{i}?api_key=abd852ac04b170c5fd5e1b376536a632')
        data=resposne.json()
        poster_list.append('https://image.tmdb.org/t/p/original/'+data['poster_path'])
    return poster_list





def movie_recommendation(Movie_Name):
    movie_id=new_pt[new_pt['title'].str.contains(Movie_Name)].index[0]
    items=sorted(list(enumerate(similarity[movie_id])),reverse=True, key=lambda x:x[1])[0:10]
    movie_list = []
    poster_id= []
    for i in items:
        movie_list.append(new_pt['title'].iloc[i[0]])
        poster_id.append(new_pt['id'].iloc[i[0]])

    return movie_list,poster_id




if st.button('Recommend'):
    recommended_movie_names,poster_id=movie_recommendation(option)
    recommended_movie_posters=get_poster(poster_id)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])










