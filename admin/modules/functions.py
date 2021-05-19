from modules import db, app_fb
from modules.frame import GetData, bool2binary, save_poster, remove_img, return_node
from os.path import join, dirname
from dotenv import load_dotenv
from flask import request

from firebase_admin import storage

import os
import requests

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
db_data = GetData()


def MovieInfo(query):

    url1 = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"+query
    url2 = "https://youtube-search-results.p.rapidapi.com/youtube-search/"
    headers1 = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key' : os.getenv("API_KEY_1")
        }
    headers2 = {
    'x-rapidapi-key': os.getenv("API_KEY_2"),
    'x-rapidapi-host': "youtube-search-results.p.rapidapi.com"
    }

    querystring = {"q":query + " Trailer"}
    store1 = requests.request("GET", url1, headers=headers1).json()
    store2 = requests.request("GET", url2, headers=headers2, params=querystring).json()
    return {
        'year'  : store1['year'],
        'actors': [i['actor'] for i in store1['cast'][:2]],
        'trailer': store2['items'][1]['link']
    }



class DatabaseOperations():


    def upload_review(self, input_data, token):

        save_poster(input_data.image.data)
        f_name,f_ext = os.path.splitext(input_data.image.data.filename)
        picture_fn = f_name + f_ext
        filePath = 'Extra/Images/' + picture_fn
        bucket = storage.bucket(app=app_fb)
        blob = bucket.blob(picture_fn)
        blob.upload_from_filename(filePath)
        blob.make_public()
        
        dets = MovieInfo(input_data.name.data)

        DB_entry = {
            'ID' : len(db_data.get_reviews()) + 1,
            'Name': input_data.name.data,
            'Review': input_data.review.data,
            'Instagram': 0,
            'Netflix': bool2binary(input_data.netflix.data),
            'Prime': bool2binary(input_data.prime.data),
            'Year': int(dets['year']),
            'Director': input_data.director.data,
            'Lead': str(dets['actors'][0]) + ', ' + str(dets['actors'][1]),
            'Acting': float(input_data.acting.data),
            'Story': float(input_data.story.data),
            'Execution': float(input_data.execution.data),
            'Profundity': float(input_data.profundity.data),
            'Overall': float(input_data.overall.data),
            'Poster': picture_fn,
            'Genre1': input_data.genre1.data,
            'Genre2': input_data.genre2.data,
            'Links': input_data.link.data,
            'Image': blob.public_url,
            'Trailer': dets['trailer']
        }

        result = db.child("Reviews").push(DB_entry, token['idToken'])
        # result = db.child("Reviews").push(DB_entry, user_token['idToken'])
        print(result)
        remove_img('Extra/Images', picture_fn)






    def update_review(self, update_data, update_id):
        updated_list = {
            'Name' : update_data.name.data,
            'Review' : update_data.review.data,
            'Netflix' : bool2binary(update_data.netflix.data),
            'Prime' : bool2binary(update_data.prime.data),
            'Director' : update_data.director.data,
            'Acting': update_data.acting.data,
            'Story': update_data.story.data,
            'Execution': update_data.execution.data,
            'Profundity': update_data.profundity.data,
            'Overall': update_data.overall.data,
            'Genre1': update_data.genre1.data,
            'Genre2': update_data.genre2.data,
            'Links': update_data.link.data,
        }

        if update_data.image.data is None:
            db.child("Reviews").child(update_id).update(updated_list)
        else:

            old_img = db.child('Reviews').child(update_id).get().val()['Poster']
            bucket = storage.bucket(app=app_fb)
            blob = bucket.blob(old_img)
            blob.delete()

            save_poster(update_data.image.data)
            f_name,f_ext = os.path.splitext(update_data.image.data.filename)
            picture_fn = f_name + f_ext
            filePath = 'Extra/Images/' + picture_fn
            bucket = storage.bucket(app=app_fb)
            blob = bucket.blob(picture_fn)
            blob.upload_from_filename(filePath)
            blob.make_public()

            updated_list['Poster'] = picture_fn
            updated_list['Image'] = blob.public_url
            db.child("Reviews").child(update_id).update(updated_list)
            remove_img('Extra/Images', picture_fn)



    def delete_review(self, review_id):
        item = return_node(review_id, 'Reviews', 'ID', nodeValue=True)
        bucket = storage.bucket(app=app_fb)
        blob = bucket.blob(item[0][1]['Poster'])
        blob.delete()
        db.child("Reviews").child(item[0][0]).remove()
        return 'Review ID : ' + str(item[0][0]) + ' of movie number : ' + str(review_id) + ' was deleted'



    def delete_message(self):
        string = request.args.get('message_id')
        string1 = string.replace('+',' ')
        string2 = string1.replace('%3A',':')
        string3 = string2.replace('%2F','/')
        message_id = return_node(string3, 'Contact-Us', 'Subject')
        db.child("Contact-Us").child(message_id[0]).remove()
        return 'Message ID: ' + str(message_id) + ' was deleted'


    def update_ig(self, review_id):
        item = return_node(review_id, 'Reviews', 'ID')
        db.child("Reviews").child(item[0]).update({'Instagram':1})
        return 'Review ID : ' + str(item) + ' was updated to Instagram'