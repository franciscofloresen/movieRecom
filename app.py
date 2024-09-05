from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Obtener la API key desde el archivo .env
API_KEY = os.getenv('API_KEY')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    movie_name = request.form.get('movie_name')
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url).json()

    movies = response.get('results', [])
    return render_template('home.html', movies=movies, movie_name=movie_name)

if __name__ == '__main__':
    app.run(debug=True)