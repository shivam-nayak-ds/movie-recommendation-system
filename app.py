import streamlit as st
import pickle
import requests

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Fetch poster from TMDB
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=2c96bec745415843559394b629d4fc26"
        response = requests.get(url, timeout=5)
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500" + data['poster_path']
        return "https://placehold.co/500x750/1a1a1a/888888?text=No+Poster"
    except:
        return "https://placehold.co/500x750/1a1a1a/888888?text=No+Poster"

# Recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in distances:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Page config
st.set_page_config(page_title='Movie Recommender', page_icon='🎬', layout='wide')

# CSS
st.markdown("""
<style>
body { background-color: #0a0a0a; }
.main { background-color: #0a0a0a; }

.header {
    text-align: center;
    padding: 40px 0 10px 0;
}
.header h1 {
    font-size: 56px;
    font-weight: 900;
    color: #e50914;
    margin: 0;
}
.header p {
    font-size: 18px;
    color: #aaaaaa;
    margin-top: 8px;
}
.stButton > button {
    background-color: #e50914;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
    border-radius: 30px;
    padding: 14px 40px;
    width: 100%;
    transition: 0.3s;
}
.stButton > button:hover {
    background-color: #ff2020;
    color: white;
}
.movie-card {
    background-color: #1a1a1a;
    border-radius: 12px;
    padding: 10px;
    text-align: center;
    border: 1px solid #2a2a2a;
    transition: 0.3s;
}
.movie-card:hover {
    border: 1px solid #e50914;
}
.movie-name {
    color: white;
    font-size: 13px;
    font-weight: 600;
    margin-top: 10px;
    text-align: center;
}
.section-title {
    color: white;
    font-size: 26px;
    font-weight: 700;
    margin: 30px 0 15px 0;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <h1>🎬 Movie Recommender</h1>
    <p>Select a movie and discover similar ones you will love!</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Movie selection
selected_movie = st.selectbox('🔍 Search or Select a Movie', movies['title'].values)

# Recommend button - centered
col1, col2, col3 = st.columns([1.5, 1, 1.5])
with col2:
    recommend_btn = st.button('🎯 Recommend')

# Show recommendations
if recommend_btn:
    with st.spinner('🍿 Finding best movies for you...'):
        recommended_movies, recommended_posters = recommend(selected_movie)

    st.markdown('<p class="section-title">🍿 Top 5 Recommendations</p>', unsafe_allow_html=True)
    st.divider()

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown('<div class="movie-card">', unsafe_allow_html=True)
            st.image(recommended_posters[i], width=180)
            st.markdown(f'<p class="movie-name">{recommended_movies[i]}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.markdown('<p style="text-align:center; color:#555555;">Made with ❤️ using Streamlit & TMDB API</p>', unsafe_allow_html=True)