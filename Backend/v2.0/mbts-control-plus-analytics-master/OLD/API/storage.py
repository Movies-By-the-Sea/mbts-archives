import os
from firebase_admin import storage




#======================================================================================
# SAVING FILES LOCALLY

def saveFile(file):
    with open(os.path.join('uploads', file.name), "wb") as f:
        f.write(file.getbuffer())

#======================================================================================





#======================================================================================
# UPLOADING FILE TO FIREBASE STORAGE

def uploadToFirebase(file):

    saveFile(file)
    filePath =  os.getcwd() +'/uploads/' + file.name
    fileName = file.name
    blob     = storage.bucket().blob(fileName)
    blob.upload_from_filename(filePath)
    blob.make_public()

    os.remove(os.getcwd() + '/uploads/' + fileName)

    return blob.public_url

#======================================================================================




#======================================================================================
# DELETING FILE FROM FIREBASE STORAGE

def deleteFromFirebase(fileName):

    bucket = storage.bucket()
    blob   = bucket.blob(fileName)
    blob.delete()

#======================================================================================