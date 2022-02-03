# Helper Files

These scripts have been written to facilitate easy and quick transition from serverless database to and from local documents.

### Installing dependencies

Run the following command before using any of the helper files. This will install all the dependencies automatically. Make sure you have pip [installed](https://pypi.org/project/pip/) beforehand.

```
pipenv shell
pipenv install
```

---

## Uploading to Firebase

_Input type : JSON, img_

_Return type : Reviews with their poster URL mapped, added to DB_

Run upload.py to upload all movie reviews to the database. Change the variable *SHORT_FILMS* to true if uploading short films.

### Usage

1. Update the reviews in the movies.json/short_films.json respectively.
2. Update the images in movies_posters/sf_posters respectively.
3. Go to [Service Account](https://console.firebase.google.com/project/mbts-backend/settings/serviceaccounts/adminsdk) and generate new private key.
4. Rename the downloaded key to *storage_adminsdk.json* and move it to the current folder.
5. Run upload.py

---

## Downloading from Firebase

_Return Type : all reviews in .csv format_

Run download.py to download all the reviews from the database into a .csv file making it easier to export.

### Usage

1. Go to [SDK setup and configuration](https://console.firebase.google.com/project/mbts-backend/settings/general/web:MGZlNThiZWQtYjNkOC00MGQzLWFiMWMtOWVlMTE5M2UwZTdl) and copy paste the CDN accordingly into .env file
2. Set the variable *SHORT_FILM* accordingly in the download.py file to download either movie reviews or short-film reviews.
3. Run download.py

Should also download all the posters of the films mapped in the reviews but is currently under maintainance.