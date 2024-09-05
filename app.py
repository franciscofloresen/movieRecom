from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Reemplaza con tu API Key de TMDb
API_KEY = 'TU_API_KEY'

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('home.html')

# Ruta para manejar la búsqueda de películas
@app.route('/search', methods=['POST'])
def search():
    movie_name = request.form.get('movie_name')
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url).json()

    # Extraemos resultados de la búsqueda
    movies = response.get('results', [])
    return render_template('home.html', movies=movies, movie_name=movie_name)

if __name__ == '__main__':
    app.run(debug=True)