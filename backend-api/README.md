# Backend API for MBtS Site

_Designed By : Saumya Bhatt_
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

## Database Schema

_Database Type : *NoSQL*_

_Serverless Database : FirebaseDB_

_Cloud Storage : Firestore_

_Link : [Database Schema](https://dbdiagram.io/d/609fc8c5b29a09603d14fc64)_

Two tables used. One containing information about film and another about short films. Their details can be found out in the above link or from below

The _id_'s are primary keys and will be auto-incremented. Posters would be stored in Firestore whose corresponding link would be stored as links under _img_blob_

<table>
<tr><th>Movies Table</th><th>shortFilms Table</th></tr>
<tr><td>

| Key        |     Type |
| :--------- | -------: |
| id         |      int |
| name       |  varchar |
| review     |  varchar |
| director   |  varchar |
| actor      |  varchar |
| year       |      int |
| amazon     |  boolean |
| netflix    |  boolean |
| instagram  |  boolean |
| acting     |    float |
| story      |    float |
| execution  |    float |
| profundity |    float |
| overall    |    float |
| genre1     |  varchar |
| genre2     |  varchar |
| poster     | img_blob |
| trailer    |  varchar |

</td><td>

| Key         |      Type |
| :---------- | --------: |
| id          |       int |
| name        |   varchar |
| director    |   varchar |
| description |   varchar |
| genre1      |   varchar |
| genre2      |  varcchar |
| instagram   |   boolean |
| duration    | timestamp |
| link        |   varchar |
| poster      |  img_blob |

</td></tr> </table>
