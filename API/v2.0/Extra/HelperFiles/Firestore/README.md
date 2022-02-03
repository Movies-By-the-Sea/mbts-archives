# Firestore Helper Files

These scripts have been written to communicate with the server for easy transition to and from the database.

---

### Installing dependencies

Run the following command before using any of the helper files. This will install all the dependencies automatically. Make sure you have pip [installed](https://pypi.org/project/pip/) beforehand.

```
pipenv shell
pipenv install
```

Libraries required to run the _.js_ files are already installed when running `npm install`.

---

## test_query.py

_Input type : Complex queries (sorting, orderBy, where)_

_Returns : result of the input queried into the database_

This file can be used to perform various complex and compounded queries on the database to check their result easily without initializing the API.

### Usage

Make changes to the queries in the file and run the file.

---

## uploadAll.py

_Input type : JSON, img_

_Returns : Reviews with their poster URL mapped, added to Firestore_

Run uploadAll.py to upload all movie reviews to the database. Change the variable *SHORT_FILMS* to true if uploading short films.

### Usage

1. Update the reviews in the movies.json/short_films.json respectively.
2. Update the images in movies_posters/sf_posters respectively.
3. Go to [Service Account](https://console.firebase.google.com/project/mbts-backend/settings/serviceaccounts/adminsdk) and generate new private key.
4. Rename the downloaded key to *credentials.json* and move it to the current folder.
5. Run upload.py


---

## uploadOne.py

_Input type : JSON_

_Returns : Review uploaded to Firestore database_

This file can be used to upload only one review at a time to the firestore database. It is assumed that the poster is already on the cloud storage, so cannot be used to upload any posters. This file will only map the uploaded review to its poster

Use this when any one review in the database has been corrupted, so can be deleted and uploaded again from here.

### Usage

1. Fill the __items__ dictionary in the file with the review which you want to upload.
2. Run the file. It will automatically take care of the mapping of the poster
3. Make sure to change the timestamping if any previous review has been uploaded.

---

## setClaim.js

_Input type : Num input_

_Returns : Updates the claims of the said user without Access Level authorization_

This file can be used to set claims to any user without running the server.

### Usage

1. Set the _uid_ variable to the user id which you want to update to.
2. Uncomment and comment the code accrdingly to check whether the operations has been successful or not.

---

## updateAllFields.js

_Input type : Field to be updated_

_Returns : updates all fields values in the database_

Use this file whenever you want to add or update just one field in the database rather than deleting it all and uploading it again.

### Usage

1. Change the field in _update_ and run the file.
2. The changes would be reflected in the database