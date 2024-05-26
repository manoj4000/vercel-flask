from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world'
    
api_key = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZGQwODMzMGU5OWI2NzUxNjRmZTYxZTViNmM0MDczMyIsInN1YiI6IjY1YzA5YzRmOWYzN2IwMDE3YzVkY2U4NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Kn2fguUxvdLpiqCUilZdCho7vZYi2Mogvxolh7wcaM'

@app.route('/discover-movies', methods=['GET'])
def discover_movies():
    page = request.args.get('page', 1)
    url = 'https://api.themoviedb.org/3/discover/movie'
    headers = {
        'accept': 'application/json',
        'Authorization': api_key
    }
    params = {
        'page': page
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Unable to fetch data'}), response.status_code

@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
