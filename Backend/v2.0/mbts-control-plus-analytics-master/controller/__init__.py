import requests
import dotenv
import json
import os

dotenv.load_dotenv(dotenv.find_dotenv())



#==============================================================================================================================
#==============================================================================================================================

def makeAPICall(reqType, route, params=None):
    url = os.getenv('API_ENDPOINT') + route
    if params != None:
        return json.loads(requests.request(reqType, url=url, json=params).text)
    return json.loads(requests.request(reqType, url=url).text)



#==============================================================================================================================
#==============================================================================================================================

def getMovieInfo(movie):
    query   = movie.replace(' ', '%20')
    url     = os.getenv('MOVIE_API_URL')
    headers = {
        'x-rapidapi-key' : os.getenv('MOVIE_API_HEADER_KEY'),
        'x-rapidapi-host': os.getenv('MOVIE_API_HEADER_HOST')
        }
    response = requests.request("GET", url+query, headers=headers)
    res      = json.loads(response.text)

    try:
        return {
            'year'   : int(res['year']) or 42,
            'length' : res['length'] or 'UPDATE MANUALLY',
            'trailer': res['trailer']['link'] or 'UPDATE MANUALLY',
            'cast'   : [res['cast'][0]['actor'], res['cast'][1]['actor'], res['cast'][2]['actor']] or ['UPDATE MANUALLY']
        }
    except:
        return {
            'year' : 42,
            'length' : 'UPDATE MANUALLY',
            'trailer' : 'UPDATE MANUALLY',
            'cast' : ['UPDATE MANUALLY']
        }