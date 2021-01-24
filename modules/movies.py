# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name('./static/credentials.json',scope)
# clients = gspread.authorize(creds)
# sheet = clients.open('mbts_reviews').sheet1
# data = sheet.get_all_records()

import requests
from modules import db

data = list(db.child('Reviews').get().val().values())
data_sf = list(db.child('Short_Films').get().val().values())


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