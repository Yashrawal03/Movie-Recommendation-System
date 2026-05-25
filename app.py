import pandas as pd
import pickle
import gradio as gr

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


interface = gr.Interface(
    fn=recommend,
    inputs=gr.Textbox(label="Movie Name"),
    outputs=gr.Textbox(label="Recommendations"),
    title="🎬 Movie Recommendation System"
)

interface.launch()