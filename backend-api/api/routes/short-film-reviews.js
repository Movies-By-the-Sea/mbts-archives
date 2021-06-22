const express  = require('express');
const database = require('../../firebase');
const router   = express.Router();
require('dotenv').config();





//=================================================================================
// GET ALL REVIEWS

router.get('/all', (req, res, next) => {
    database
    .ref('short-film-reviews')
    .once('value', (snapshot) => {
        return res
            .status(200)
            .json({
                message  : 'success',
                size     : Object.keys(snapshot.val()).length,
                request  : {
                    type     : 'GET',
                    url      : process.env.SERVER + '/short-film-reviews/all'
                },
                response : snapshot.val()
        });
    });
});

//=================================================================================




//==================================================================================
// GETTING GENERAL INFO

router.get('/', (req, res, next) => {
    database
    .ref('short-film-reviews')
    .once('value', (snapshot) => {

        let reviews = snapshot.val();
        let count   = 0;

        for(item in reviews) {
            if(reviews[item]['instagram']) {
                count++;
            }
        }

        return res
            .status(200)
            .json({
                message     : 'success',
                request     : {
                    type : 'GET',
                    url  : process.env.SERVER + '/short-film-reviews/'
                },
                response : {
                    allReviews  : Object.keys(snapshot.val()).length,
                    allInstagram: count
                }
            })
    })
})

//==================================================================================






//=================================================================================
// GET REVIEW OF FILM SPECIFIED BY ID

router.get('/:short_film_id', (req, res, next) => {
    database
    .ref('short-film-reviews')
    .once('value', (snapshot) => {
        result = snapshot.val()[req.params.short_film_id];
        if(result) {
            return res
            .status(200)
            .json({
                message  : 'success',
                movie_id : req.params.short_film_id,
                request  : {
                    type     : 'GET',
                    url      : process.env.SERVER + '/short-film-reviews/' + req.params.short_film_id
                },
                response : result,
            });
        }
        return res
            .status(404)
            .json({
                message : 'No such short-film with given ID found'
            })
    });
});

//=================================================================================






//=================================================================================
// GET ALL SHORT-FILMS UPDATED ON INSTAGRAM

router.get('/instagram', (req, res, next) => {
    database
    .ref('short-film-reviews')
    .once('value', (snapshot) => {

        let reviews = snapshot.val();
        let movies  = [];
        let count   = 0;

        for(item in reviews) {
            if(reviews[item]['instagram']) {
                movies.push(reviews[item]);
                count++;
            }
        }

        return res
        .status(200)
        .json({
            message  : 'success',
            size     : count,
            request  : {
                type     : 'GET',
                url      : process.env.SERVER + '/short-film-reviews/instagram'
            },
            response : movies
        });

    });
});

//=================================================================================







module.exports = router;