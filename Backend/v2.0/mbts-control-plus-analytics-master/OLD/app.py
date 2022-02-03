import os
import streamlit as st
import firebase_admin

from firebase       import Firebase
from dotenv         import load_dotenv
from modules.text   import Page
from firebase_admin import credentials, initialize_app





#=================================================================
# FIREBASE CONFIGURATIONS

load_dotenv('./.env')
st.set_page_config(layout='wide', initial_sidebar_state="expanded")

if not firebase_admin._apps:
    cred = credentials.Certificate(os.getcwd() + '/uploads/storage_adminsdk.json') 
    default_app = initialize_app(cred, {'storageBucket' : os.getenv('STORAGE_BUCKET_URL')})

config = {
    "apiKey"       : os.getenv('API_KEY'),
    "authDomain"   : os.getenv('AUTH_DOMAIN'),
    "databaseURL"  : os.getenv('DATABASE_URL'),
    "storageBucket": os.getenv('STORAGE_BUCKET_URL')
}

firebase = Firebase(config)
auth     = firebase.auth()



#===================================================================





#==================================================================
# MAIN DISPLAY 

Page.title()
Page.login(auth)

if(Page.state) :

    Page.highlights()
    Page.siteFunctions()
    Page.instagram()

#=====================================================================