import os
import json
from dotenv import load_dotenv
from firebase import firebase
from firebase_admin import credentials, initialize_app, storage

load_dotenv('../.env')


# CHANGE THIS TO TRUE WHEM UPLOADING TO SHORT-FILMS
SHORT_FILMS = True

if(SHORT_FILMS):
    REVIEWS_PATH = '../../checkpoint/short_films.json'
    FILE_PATH = '../../checkpoint/sf_posters/'
    DATA_TABLE = '/short-film-reviews'
else:
    REVIEWS_PATH = '../../checkpoint/movies.json'
    FILE_PATH = '../../checkpoint/movies_posters/'
    DATA_TABLE = '/movie-reviews'




# INITIALIZING FIREBASE
cred = credentials.Certificate('./storage_adminsdk.json')
initialize_app(cred, {'storageBucket' : os.getenv('STORAGE_BUCKET_URL')})
firebase = firebase.FirebaseApplication(os.getenv('DATABASE_URL'), None)



with open(REVIEWS_PATH) as json_file:

    data = json.load(json_file)
    for item in data:

        filePath = FILE_PATH + item['Poster']
        fileName = item['Poster']
        blob = storage.bucket().blob(fileName)
        blob.upload_from_filename(filePath)
        blob.make_public()

        if(SHORT_FILMS):
            DB_ENTRY = {
                'id'         : item['ID'],
                'name'       : item['Name'],
                'director'   : item['Director'],
                'description': item['Description'],
                'genre'      : [item['Genre1'],item['Genre2']],
                'instagram'  : item['Instagram'],
                'duration'   : item['Duration'],
                'link'       : item['Link'],
                'poster_name': item['Poster'],
                'poster_link'     : blob.public_url
            }
        else:
            DB_ENTRY = {
                'id'        : item['ID'],
                'name'      : item['Name'],
                'review'    : item['Review'],
                'director'  : item['Director'],
                'actor'     : item['Lead'],
                'year'      : item['Year'],
                'amazon'    : item['Prime'],
                'netflix'   : item['Netflix'],
                'instagram' : item['Instagram'],
                'acting'    : item['Acting'],
                'story'     : item['Story'],
                'execution' : item['Execution'],
                'profundity': item['Profundity'],
                'overall'   : item['Overall'],
                'genre'     : [item['Genre1'],item['Genre2']],
                'trailer'   : item['Trailer'],
                'poster_name': item['Poster'],
                'poster_link'    : blob.public_url
            }

        result = firebase.post(DATA_TABLE, DB_ENTRY)
        print(result)