#=====================================================================
#=====================================================================
#=====================================================================
#=====================                   =============================
#===================== AUTHENTICATE USER =============================
#=====================                   =============================
#=====================================================================
#=====================================================================
#=====================================================================



import os
import ast
import pyrebase
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PYREBASE_CONFIG = {
    "apiKey"           : os.getenv('FIREBASE_API_KEY'),
    "authDomain"       : os.getenv('AUTH_DOMAIN'),
    "databaseURL"      : os.getenv('DATABASE_URL'),
    "projectId"        : os.getenv('PROJECT_ID'),
    "storageBucket"    : os.getenv('STORAGE_BUCKET'),
    "messagingSenderId": os.getenv('MESSAGING_SENDER_ID'),
    "appId"            : os.getenv('APP_ID'),
    "serviceAccount"   : ast.literal_eval(os.getenv("FIREBASE_CREDS"))
    }


firebase = pyrebase.initialize_app(PYREBASE_CONFIG)
auth = firebase.auth()

email=os.getenv('EMAIL')
password=os.getenv('PASSWORD')

user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()




#=====================================================================
#=====================================================================
#=====================================================================
#========================             ================================
#======================== CREATE USER ================================
#========================             ================================
#=====================================================================
#=====================================================================
#=====================================================================

import os
import pyrebase
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

firebase = pyrebase.initialize_app(os.getenv('PYREBASE_CONFIG'))
auth = firebase.auth()
email = 'saumi10600@gmail.com'
password = 'ThisIsMyMBTS1'

user = auth.create_user_with_email_and_password(email, password)
print('success!!')