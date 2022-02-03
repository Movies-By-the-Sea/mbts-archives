import firebase_admin
from firebase_admin import firestore, credentials

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Note: Use of CollectionRef stream() is prefered to get()
docs = db.collection(u'movie-reviews').where(u'genre', u'array_contains', u'Romance').stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()['name']}")