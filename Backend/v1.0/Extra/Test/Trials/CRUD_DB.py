from os.path import join, dirname
from dotenv import load_dotenv
import os
import ast

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)





#=====================================================================
#=====================================================================
#=====================================================================
#==================                        ===========================
#================== REALTIME DB OPERATIONS ===========================
#==================                        ===========================
#=====================================================================
#=====================================================================
#=====================================================================


import json
from firebase import firebase

firebase = firebase.FirebaseApplication(os.getenv('DATABASE_URL'), None)





#=====================================================================
#======================= ADD DATA TO DB ==============================
#=====================================================================

with open('reviews.json') as json_file:
    data = json.load(json_file)
    for item in data:

        DB_entry = {
            'ID' : item['ID'],
            'Name': item['Name'],
            'Review': item['Review'],
            'Instagram': item['Instagram'],
            'Netflix': item['Netflix'],
            'Prime': item['Prime'],
            'Year': item['Year'],
            'Director': item['Director'],
            'Lead': item['Lead'],
            'Acting': item['Acting'],
            'Story': item['Story'],
            'Execution': item['Execution'],
            'Profundity': item['Profundity'],
            'Overall': item['Overall'],
            'Poster': item['Poster'],
            'Genre1': item['Genre1'],
            'Genre2': item['Genre2'],
            'Links': item['Links'],
            'Image': item['Image-url'],
            'Trailer': item['Trailer']
        }
        result = firebase.post('/Reviews',DB_entry)
        print(result)





#=====================================================================
#===================== GET DATA FROM DB ==============================
#=====================================================================

firebase = firebase.FirebaseApplication(os.getenv('DATABASE_URL'), None)
result = firebase.get('Reviews','')
res = list(result.values()) 
print(res[0])





#=====================================================================
#====================== UPDATE DATA TO DB ============================
#=====================================================================

DB_entry = {
    'Name': 'TESTING2',
}
result = firebase.post('/Reviews',DB_entry)
print(result)










#=====================================================================
#=====================================================================
#=====================================================================
#====================                    =============================
#==================== STORAGE OPERATIONS =============================
#====================                    =============================
#=====================================================================
#=====================================================================
#=====================================================================


from firebase import firebase as FB
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import initialize_app

import datetime





#=====================================================================
#======================== UPLOAD IMAGE ===============================
#=====================================================================

# Init firebase with your credentials
cred = credentials.Certificate(ast.literal_eval(os.environ["FIREBASE_CREDS"]))
initialize_app(cred, {'storageBucket': os.getenv('STORAGE_BUCKET')})

# Put your local file path 
filePath = "../../modules/mclaren.png"
fileName = 'mclaren.png'
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(filePath)

# Opt : if you want to make public access from the URL
blob.make_public()

print("your file url", blob.public_url)





#=====================================================================
#========================== GET IMAGE ================================
#=====================================================================

# Fetch the service account key JSON file contents
cred = credentials.Certificate(ast.literal_eval(os.environ["FIREBASE_CREDS"]))
firebase_admin.initialize_app(cred)


# Initialize the app with a service account, granting admin privileges
app = firebase_admin.initialize_app(cred, {
    'storageBucket': os.getenv('STORAGE_BUCKET'),
}, name='storage')

bucket = storage.bucket(app=app)
blob = bucket.blob("1917.jpg")

print(blob.generate_signed_url(datetime.timedelta(days=99999), method='GET'))





#=====================================================================
#========================== DELETE IMAGE =============================
#=====================================================================

firebase = FB.FirebaseApplication(os.getenv('DATABASE_URL'), None)
cred = firebase_admin.credentials.Certificate(ast.literal_eval(os.environ["FIREBASE_CREDS"]))
app_fb = firebase_admin.initialize_app(cred, {'storageBucket': os.getenv('STORAGE_BUCKET'),}, name='storage')

bucket = storage.bucket(app=app_fb)
blob = bucket.blob('111.png')
blob.delete()