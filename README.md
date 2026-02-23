<h1 align="center">🎬 Movie Recommendation System</h1>

<p align="center">
A <b>Machine Learning powered Movie Recommendation Web Application</b> built using
<b>Python & Streamlit</b> that suggests similar movies based on content similarity.
</p>

<hr>

<h2>🚀 Project Overview</h2>
<p>
This project is a <b>content-based movie recommender system</b> that helps users discover
movies similar to their interests. The system analyzes movie metadata such as
<b>genres, keywords, cast, crew, and overview</b> and recommends movies using
<b>cosine similarity</b>.
</p>

<p>
The application is deployed as an <b>interactive Streamlit web app</b> with a clean dark UI
and movie posters fetched using the <b>TMDB API</b>.
</p>

<hr>

<h2>✨ Key Highlights</h2>
<ul>
  <li>🎯 Content-based filtering using textual movie metadata</li>
  <li>🧠 Machine Learning similarity matching (Cosine Similarity)</li>
  <li>🎨 Modern dark UI built with Streamlit & custom CSS</li>
  <li>🎞️ Movie posters and metadata using TMDB API</li>
  <li>⚡ Fast recommendations using precomputed pickle files</li>
</ul>

<hr>

<h2>🌟 Features</h2>
<ul>
  <li>Search or select a movie from dropdown</li>
  <li>Get top 5 similar movie recommendations</li>
  <li>Display movie posters with titles</li>
  <li>Responsive Streamlit web interface</li>
  <li>Efficient model loading using Pickle</li>
</ul>

<hr>

<h2>🛠️ Technology Stack</h2>
<ul>
  <li><b>Programming Language:</b> Python</li>
  <li><b>Data Processing:</b> Pandas, NumPy</li>
  <li><b>Machine Learning:</b> Scikit-learn</li>
  <li><b>Vectorization:</b> CountVectorizer</li>
  <li><b>Similarity Measure:</b> Cosine Similarity</li>
  <li><b>Web Framework:</b> Streamlit</li>
  <li><b>Model Storage:</b> Pickle</li>
</ul>

<hr>

<h2>📊 Dataset</h2>
<p>
The project uses the <b>TMDB 5000 Movies Dataset</b> and <b>TMDB 5000 Credits Dataset</b>.
</p>

<ul>
  <li>Movie titles</li>
  <li>Genres</li>
  <li>Overview</li>
  <li>Keywords</li>
  <li>Cast & crew</li>
</ul>

<hr>

<h2>⚙️ How It Works</h2>
<ol>
  <li>Movie and credits datasets are merged</li>
  <li>Important features are combined into a single text column</li>
  <li>Text data is vectorized using CountVectorizer</li>
  <li>Cosine similarity is calculated between movies</li>
  <li>Top similar movies are recommended to the user</li>
</ol>

<hr>

<h2>▶️ How to Run the Project Locally</h2>

<pre>
pip install -r requirements.txt
streamlit run app.py
</pre>

<hr>

<h2>📁 Project Structure</h2>

<pre>
movie-recommendation-system/
│
├── app.py
├── movies.pkl
├── requirements.txt
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
├── data_understanding.ipynb
├── screenshots/
│   ├── home.png
│   └── recommendations.png
└── README.md
</pre>

<hr>

<h2>📸 Application Preview</h2>
<p align="center">
  <img src="screenshots/home.png" width="800">
</p>

<p align="center">
  <img src="screenshots/recommendations.png" width="800">
</p>

<hr>

<h2>🔮 Future Improvements</h2>
<ul>
  <li>Add collaborative filtering</li>
  <li>User-based recommendations</li>
  <li>Improve similarity model</li>
  <li>Deploy with cloud hosting</li>
</ul>

<hr>

<h2>👤 Author</h2>
<p>
<b>Shivam Nayak</b><br>
Aspiring Data Scientist / Machine Learning Engineer
</p>

<p>
If you found this project useful, please ⭐ the repository.
</p>
