from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Obtener la API Key desde el archivo .env
API_KEY = os.getenv('API_KEY')

# Página principal
@app.route('/')
def home():
    # Obtener los géneros desde la API de TMDb
    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}"
    genres = requests.get(genre_url).json().get('genres', [])
    return render_template('home.html', genres=genres)

# Búsqueda de películas
@app.route('/search', methods=['GET', 'POST'])
def search():
    movie_name = request.args.get('movie_name') or request.form.get('movie_name')
    genre_id = request.args.get('genre') or request.form.get('genre')
    page = request.args.get('page', 1, type=int)

    # URL de búsqueda con el filtro de género y la paginación
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}&page={page}"
    if genre_id:
        url += f"&with_genres={genre_id}"

    response = requests.get(url).json()
    movies = response.get('results', [])
    return render_template('home.html', movies=movies, movie_name=movie_name, page=page, genre_id=genre_id, genres=response.get('genres', []))

# Detalle de película
@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    # Obtener los detalles de una película por su ID
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    movie = requests.get(url).json()
    return render_template('movie_detail.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)