# Database Schema for MBtS backend

_Last updated : Friday, 2nd July, 2021_

The serverless database used here is document based. Poster images are stored onto Google Cloud storage whose URL links are mapped to complimentary review and stored int the Firebase Firestore.

There are 2 main tables - movie-reviews and short-film-reviews. Their structure and fields are described below.

---

## movie-reviews Table

| Field       | Data type     | Description                                       |
| ------------| --------------| ------------------------------------------------- |
| name        | string        | Name of the movie                                 |
| director    | string        | Name of the director                              |
| review      | string        | Film review within 500 words                      | 
| year        | integer       | Year the film was released                        |
| genre       | array<String> | Array(4) of generes from predefined list          |
| actor       | array<String> | Array(3) of lead actors/actresses                 |
| netflix     | boolean       | Is the film available on netflix or not           |
| amazon      | boolean       | Is the film available on amazon Prime or not      |
| foreign     | boolean       | Is the film hollywood or foreign film             |
| must_watch  | boolean       | Does the film fall under must-watch column        |
| instagram   | boolean       | Has the film review been posted on IG page or not |
| acting      | float         | Ratings out of 5                                  |
| story       | float         | Ratings out of 5                                  |
| execution   | float         | Ratings out of 5                                  |
| profundity  | float         | Ratings out of 5                                  |
| overall     | float         | Ratings out of 5                                  |
| trailer     | string        | Trailer for the movie                             |
| poster_name | string        | So as to map it between database and storage      |
| poster_link | string        | Cloud Storage URL link to the poster              |
| timestamp   | DateTime      | Time of creation of the post                      |
| author      | String        | Author of the said review                         |
| author_uid  | String        | UID of the author (access-controlled)             |

---

## short-film-reviews Table

| Field       | Data type     | Description                                       |
| ----------- | ------------- | ------------------------------------------------- |
| name        | string        | Name of the movie                                 |
| director    | string        | Name of the director                              |
| genre       | array<String> | Array(2) of generes from predefined list          |
| description | string        | Short brief about the film                        |
| duration    | string        | What the runtime of the short film is             |
| instagram   | boolean       | Has the film review been posted on IG page or not |
| link        | string        | link to watch the short film                      |
| poster_name | string        | So as to map it between database and storage      |
| poster_link | string        | Cloud Storage URL link to the poster              |
| timestamp   | DateTime      | Time of creation of the post                      |
| author      | String        | Author of the said review                         |
| author_uid  | String        | UID of the author (access-controlled)             |

---

## users Table

__NOTE :__ This table can only be accessed by the backend server and not by any user irrespective of their access level.

| Field       | Data type     | Description                                       |
| ----------- | ------------- | ------------------------------------------------- |
| name        | String        | Name of the user                                  |
| email       | String        | Registered email ID of the user                   |
| password    | String        | User password stored in Hash by SHA-256           |
| accessLevel | integer       | Access level claim of said user                   |