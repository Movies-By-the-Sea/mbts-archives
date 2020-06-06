from flask import Flask, render_template, url_for, request
app = Flask('__name__')

import csv
with open('static/reviews.csv') as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

import requests
import json

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

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html', data=data, result=userInput('Get Out'))

@app.route('/reviews.html')
def open():
    return render_template('reviews.html', data=data)

@app.route('/', methods=['POST'])
@app.route('/index.html', methods=['POST'])
def my_form_post():
    text = request.form['searchMovie']
    processed_text = userInput(text)
    return render_template('index.html',data=data,result=processed_text)

if __name__ == "__main__":
    app.run(debug=True)