from os.path import join, dirname
from dotenv import load_dotenv

import requests
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)



def userInput(query):
    url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"+query
    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key' : os.getenv("API_KEY_1")
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
        'year'  : store['year'],
        'actors': actors
    }
    print(MovieDetails)




url = "https://youtube-search-results.p.rapidapi.com/youtube-search/"
querystring = {"q":"The Girl with the dragon tattoo Trailer"}
headers = {
    'x-rapidapi-key': os.getenv("API_KEY_2"),
    'x-rapidapi-host': "youtube-search-results.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
store2 = response.json()
print(store2['items'][1]['link'])