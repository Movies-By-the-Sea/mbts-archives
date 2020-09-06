from flask import Flask, render_template, url_for, request
import requests
import json
import csv

app = Flask('__name__')
app.config['SECRET_KEY'] = 'jvkhvtyvuvvbytvchbycgfcg'

with open('static/reviews.csv') as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]


def userInput(query):
    url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"+query

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key' : "42a81c1684msh89e08ede69c15b4p1df539jsn876cffad9666"
        }

    response = requests.request("GET", url, headers=headers)
    store = response.json()

    count = 0
    actors = list()
    for i in store["cast"]:
        if count > 5:
            break
        actors.append(i['actor'])
        count += 1

    MovieDetails = {
        'title' : store['title'],
        'year'  : store['year'],
        'plot'  : store['plot'],
        'actors': actors
    }
    return MovieDetails

import forms

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    movie_inp = forms.MovieSearch()
    if movie_inp.validate_on_submit():
        get_details = userInput(movie_inp.movie_name.data)
        return render_template('index.html',data=data,result=get_details,movie_input=movie_inp)

    temp_result = userInput('Get Out')
    return render_template('index.html', data=data, movie_input=movie_inp,result=temp_result)

@app.route('/reviews')
def open():
    return render_template('reviews.html', data=data)

@app.route('/', methods=['POST'])
@app.route('/index.html', methods=['POST'])
def my_form_post():
    text = request.form['searchMovie']
    processed_text = userInput(text)
    return render_template('index.html',data=data,result=processed_text)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html')

if __name__ == "__main__":
    app.run(debug=True)