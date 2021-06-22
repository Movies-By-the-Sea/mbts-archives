import os
import csv
from dotenv import load_dotenv
from firebase import Firebase
load_dotenv('./.env')



# WILL BY DEFAULT DOWNLOAD DATA OF MOVIES
# SET THIS TI TRUE TO DOWNLOAD FOR SHORT-FILMS
SHORT_FILMS = False

if SHORT_FILMS :
    TABLE_PATH = 'short-film-reviews'
else:
    TABLE_PATH = 'movie-reviews'
config = {
    "apiKey"       : os.getenv('API_KEY'),
    "authDomain"   : os.getenv('AUTH_DOMAIN'),
    "databaseURL"  : os.getenv('DATABASE_URL'),
    "storageBucket": os.getenv('STORAGE_BUCKET_URL')
  }


# INITIALIZING FIREBASE
firebase = Firebase(config)
db = firebase.database()
storage = firebase.storage()


# GETTING DATA FROM DATABASE
result = db.child(TABLE_PATH).get()
reviews = list(result.val().values())
keys = reviews[0].keys()


# CONVERTING DATA TO CSV FILE
with open('REVIEWS.csv','w',newline='') as review_file:
        dict_writer = csv.DictWriter(review_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(reviews)


# DOWNLOADNG IMAGES
for item in reviews:
    name = item['poster_name']
    storage.child(name).download(os.getcwd() + '/DOWNLOAD_FILES/' + name)


print('DOWNLOAD COMPLETE')