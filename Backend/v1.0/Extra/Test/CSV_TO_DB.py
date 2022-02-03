import json
from firebase import firebase
from firebase_admin import credentials, initialize_app, storage

# Init firebase with your credentials
cred = credentials.Certificate("mbts-storage.json")
initialize_app(cred, {'storageBucket': 'movies-by-the-sea-ca0b5.appspot.com'})


firebase = firebase.FirebaseApplication("https://movies-by-the-sea-ca0b5-default-rtdb.firebaseio.com/", None)

with open('reviews.json') as json_file:
    data = json.load(json_file)
    for item in data:

        filePath = "Movies/" + item['Poster']
        fileName = item['Poster']
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(filePath)

        blob.make_public()

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
            'Image': blob.public_url,
            'Trailer': item['Trailer']
        }
        result = firebase.post('/Reviews',DB_entry)
        print(result)