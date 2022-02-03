import firebase_admin
import dotenv
import os

from view import Page
from firebase       import Firebase
from firebase_admin import credentials, initialize_app

dotenv.load_dotenv(dotenv.find_dotenv())
uid=os.getenv('UID')



if not firebase_admin._apps:
    cred = credentials.Certificate(os.getcwd() + '/.streamlit/storage_adminsdk.json') 
    default_app = initialize_app(cred, {'storageBucket' : os.getenv('STORAGE_BUCKET')})

config = {
    "apiKey"       : os.getenv('API_KEY'),
    "authDomain"   : os.getenv('AUTH_DOMAIN'),
    "databaseURL"  : os.getenv('DATABASE_URL'),
    "storageBucket": os.getenv('STORAGE_BUCKET_URL')
}

firebase = Firebase(config)
auth     = firebase.auth()

Page.mainHeader()
Page.siteFunctions(uid)