from flask import Flask
from os.path import join, dirname
from dotenv import load_dotenv

import firebase_admin
import pyrebase
import ast
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
certi = ast.literal_eval(os.environ["FIREBASE_CREDS"])

PYREBASE_CONFIG = {
    "apiKey"           : os.getenv('FIREBASE_API_KEY'),
    "authDomain"       : os.getenv('AUTH_DOMAIN'),
    "databaseURL"      : os.getenv('DATABASE_URL'),
    "projectId"        : os.getenv('PROJECT_ID'),
    "storageBucket"    : os.getenv('STORAGE_BUCKET'),
    "messagingSenderId": os.getenv('MESSAGING_SENDER_ID'),
    "appId"            : os.getenv('APP_ID'),
    "serviceAccount"   : certi
}

firebase = pyrebase.initialize_app(PYREBASE_CONFIG)
auth = firebase.auth()
db = firebase.database()

cred = firebase_admin.credentials.Certificate(certi)
app_fb = firebase_admin.initialize_app(cred, {'storageBucket': os.getenv('STORAGE_BUCKET'),}, name='storage')
app = Flask('__name__')
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

# from flask_mail import Mail
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = 'saumya.bhatt106@gmail.com'
# app.config["MAIL_PASSWORD"] = 'bla'
# mail = Mail()
# mail.init_app(app)

from modules import routes