# MBtS Control and Analytics Panel

Used to write, upload, update and delete reviews for the Movies By the Sea blog-site. Made completely using python

**NOTE** : Analytics added once GA is integrated with the frontend

![Screen shot](./Extra/1.png)

## Installation

Make sure you have python and pip installed.

1. Clone/Download this repository.
2. Go to [SDK setup and configuration](https://console.firebase.google.com/project/mbts-backend/settings/general/web:MGZlNThiZWQtYjNkOC00MGQzLWFiMWMtOWVlMTE5M2UwZTdl) and copy paste the CDN accordingly into a .env file.
3. Run the following command which will automatically install all the dependencies.

```
pipenv shell
pipenv install
```

4. Start the webapp by running command :

```
streamlit run app.py
```

## Architecture

Admin Panle will help manage the reviews on the website. Helper APIs will be used to make the process of uploading a review easier. This panel will also house APIs for Google analytics, instagram, etc.

Main frontend site will have read only privilages. Backend API will take the data from the Database and perform complex queries required for the frontend display.

![bla](https://user-images.githubusercontent.com/46018242/118792144-ff31a600-b8b4-11eb-8182-a7503caeff03.png)

### Tech Stack

1. **Web-Frontend** : ReactJS, tailwind.css <br>
2. **Backend** : NodeJS, Express <br>
3. **Database** : NoSQL (Google Firebase) <br>
4. **Admin + Analytics** : Streamlit (Python) <br>

### Authentication

**Service** : Google OAuth-2.0

#### Admin Panel Autherization Process
![bla_ad_au](https://user-images.githubusercontent.com/46018242/118786774-c6430280-b8af-11eb-85ca-8b81ef935bcf.png)

#### Frontend Site Autherization Process
![bla_gen_au](https://user-images.githubusercontent.com/46018242/118789958-ecb66d00-b8b2-11eb-84e9-88b79bf774f6.png)
