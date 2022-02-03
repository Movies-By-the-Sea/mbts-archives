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


item =  {
   "Name"      : "The Lighthouse",
   "Review"    : "Set in the early 20th century, this is a movie of two men who are stuck at a lighthouse island and their gradual descent into madness. Robert Eggers very clearly flexes his impeccable sense of direction here. It creates an eerie sense of unsettling while keeping you drawn to the fantastic setting. What boosts this prospect is that the movie is shot in square frame and is in BnW. As all greate psychological thrillers, this too has a quite bit of symbolism which like I suggest in my previous reviews encourage you to read more about the movie after it ends to actually feel the message that the story writer wanted to send across. But what truely makes this a masterpiece is the oscar worthy acting by both Williem Defoe and Robert Pattinson (who may have have proved his mettle as an actor with this movie). They could easily have won an oscar (Defoe should've gotten for supporting actor imo) had it not been for a certain Joker. Overall this is powerfull watch which would dazzle you with it's acting, setting and symbolism rather than the story itself. Reserve it for those cold winter evenings and watch as it acts out the insanities and depravities of man when forced into isolation (hey!).",
   "Instagram" : 1,
   "Netflix"   : 0,
   "Prime"     : 0,
   "Year"      : 2019,
   "Director"  : "Robert Eggers",
   "Lead1"     : "Robert Pattinson",
   "Lead2"     : "Williem Defoe",
   "Lead3"     : "Logan Hawkes",
   "Acting"    : "4.4",
   "Story"     : 3.2,
   "Execution" : 4,
   "Profundity": 2,
   "Overall"   : 3.4,
   "Poster"    : "lighthouse.jpg",
   "Foreign"   : 0,
   "Must_Watch": 0,
   "Genre1"    : "Dark",
   "Genre2"    : "Thriller",
   "Genre3"    : "Meta",
   "Trailer"   : "https://www.youtube.com/watch?v=Hyag7lR8CPA"
 }

fileName = item['Poster']
blob = storage.bucket().blob(fileName)

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
print('Uploaded to collection: {}  |  {}'.format(FIRESTORE_COLLECTION, item['Name']))


