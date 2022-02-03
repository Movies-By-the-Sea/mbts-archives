import os
import json
import time

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, firestore, storage

load_dotenv('../.env')
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {'storageBucket' : os.getenv('FIRESTORE_STORAGE_URL')})
firestore_db = firestore.client()


SHORT_FILMS = False

if not SHORT_FILMS:
    REVIEW_PATH          = '../../checkpoint/movies.json'
    FILE_PATH            = '../../checkpoint/movies_posters/'
    FIRESTORE_COLLECTION = u'movie-reviews'
else: 
    REVIEW_PATH          = '../../checkpoint/short_films.json'
    FILE_PATH            = '../../checkpoint/sf_posters/'
    FIRESTORE_COLLECTION = u'short-film-reviews'





with open(REVIEW_PATH) as json_file:
    data = json.load(json_file)
    for count, item in enumerate(data, start=1):

        filePath = FILE_PATH + item['Poster']
        fileName = item['Poster']
        blob = storage.bucket().blob(fileName)
        blob.upload_from_filename(filePath)
        blob.make_public()

        if not SHORT_FILMS:
            temp = {
                'name'       : item['Name'],
                'review'     : item['Review'],
                'instagram'  : bool(item['Instagram']),
                'netflix'    : bool(item['Netflix']),
                'prime'      : bool(item['Prime']),
                'year'       : item['Year'],
                'director'   : item['Director'],
                'lead'       : [item['Lead1'],item['Lead2'],item['Lead2']],
                'acting'     : item['Acting'],
                'story'      : item['Story'],
                'execution'  : item['Execution'],
                'profundity' : item['Profundity'],
                'overall'    : item['Overall'],
                'poster'     : item['Poster'],
                'must_watch' : bool(item['Must_Watch']),
                'foreign'    : bool(item['Foreign']),
                'genre'      : [item['Genre1'],item['Genre2'],item['Genre3']],
                'trailer'    : item['Trailer'],
                'poster_link': blob.public_url,
                'timestamp'  : time.time()
            }
        else:
            temp = {
                'name'       : item['Name'],
                'director'   : item['Director'],
                'description': item['Description'],
                'genre'      : [item['Genre1'], item['Genre2']],
                'instagram'  : bool(item['Instagram']),
                'duration'   : item['Duration'],
                'link'       : item['Link'],
                'poster_name': item['Poster'],
                'poster_link': blob.public_url,
                'timestamp'  : time.time()
            }

        firestore_db.collection(FIRESTORE_COLLECTION).add(temp)
        print('{}\tUploaded to collection: {}  |  {}'.format(str(count), FIRESTORE_COLLECTION, item['Name']))


