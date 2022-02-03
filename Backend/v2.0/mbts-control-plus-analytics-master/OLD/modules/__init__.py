import os
import json
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv('../.env')





#===================================================================
# HAVING NEWLINE IN STREAMLIT

def newLine(num, obj):
    for _ in range(num):
        obj.markdown('\n')

#===================================================================





#===================================================================
# METHOD TO CALL THE REST API BACKEND

def callREST(reqtype, routes, jsonVal=None):
    result = []
    for route in routes:
        url = os.getenv('REST_API') + route
        if jsonVal is None:
            res = json.loads(requests.request(reqtype, url=url).text)
        else:
            res = json.loads(requests.request(reqtype, url=url, json=jsonVal).text)
        result.append(res)
    return result

#===================================================================





#=======================================================================
# METHOD TO CHECK IF THE INPUT DATA HAS BEEN MODIFIED OR NOT

def checkIfUpdated(original, updated):
    if not updated : return [[], False]
    temp = [{item1 : updated[item2]} for item1, item2 in zip(original, updated) if original[item1] != updated[item2]]
    changed = {}
    for item in temp:
        for key in item:
            changed[key] = item[key]
    if not changed : return [changed, False]
    return [changed, True]

#======================================================================





#============================================================================
# GET MOVIE INFO FROM EXTERNAL HELPER API

def getMovieInfo(movie):
    query   = movie.replace(' ', '%20')
    url     = os.getenv('MOVIE_API_URL')
    headers = {
        'x-rapidapi-key' : os.getenv('MOVIE_API_HEADER_KEY'),
        'x-rapidapi-host': os.getenv('MOVIE_API_HEADER_HOST')
        }
    response = requests.request("GET", url+query, headers=headers)
    res      = json.loads(response.text)

    return {
        'year'   : int(res['year']),
        'length' : res['length'],
        'trailer': res['trailer']['link'],
        'cast'   : res['cast'][0]['actor'] + ', ' + res['cast'][1]['actor']
    }

#============================================================================





#============================================================================
# CHECKING IF USER HAS ENTERED ALL THE REQUIRED FIELDS OR NOT

def checkIfFilledRequired(data):

    if not data : return False
    reqFlag = False

    for key in data:
        if key == 'poster_name' and data[key] is None:
            reqFlag = True
        if key == 'duration' and data[key] == 0.0:
            reqFlag = True
        if key == 'genre' and len(data[key]) < 2:
            reqFlag = True        
        if data[key] == '' :
            reqFlag = True
        
        if reqFlag:
            st.error('Please fill in the key : ' + key)
            return False
            
    return True

#============================================================================