const express  = require('express');
const database = require('../../firebase');
const router   = express.Router();
require('dotenv').config();




//=================================================================================
// GET ALL REVIEWS

router.get('/all', (req, res, next) => {
    database
    .ref('movie-reviews')
    .once('value', (snapshot) => {
        return res
            .status(200)
            .json({
                message  : 'success',
                size     : Object.keys(snapshot.val()).length,
                request  : {
                    type     : 'GET',
                    url      : process.env.SERVER + '/movie-reviews/all'
                },
                response : snapshot.val(),
        });
    });
});

//=================================================================================





//=================================================================================
// GET REVIEW OF FILM SPECIFIED BY ID

router.get('/:movie_id', (req, res, next) => {
    database
    .ref('movie-reviews')
    .once('value', (snapshot) => {
        result = snapshot.val()[req.params.movie_id];
        if(result) {
            return res
            .status(200)
            .json({
                message  : 'success',
                movie_id : req.params.movie_id,
                request  : {
                    type     : 'GET',
                    url      : process.env.SERVER + '/movie-reviews/' + req.params.movie_id
                },
                response : result,
            });
        }
        return res
            .status(404)
            .json({
                message : 'No such film with given ID found'
            })
    });
});

//=================================================================================





//==================================================================================
// GETTING GENERAL INFO

router.get('/', (req, res, next) => {
    database
    .ref('movie-reviews')
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
                request : {
                    type : 'GET',
                    url  : process.env.SERVER + '/movie-reviews/'
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
// GET ALL MOVIES UPDATED ON INSTAGRAM

router.get('/instagram', (req, res, next) => {
    database
    .ref('movie-reviews')
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
                type    : 'GET',
                url     : process.env.SERVER + '/movie-reviews/instagram'
            },
            response : movies
        });

    });
});
//=================================================================================





//=================================================================================
// GET ALL MOVIES AVAILABLE ON AMAZON PRIME

router.get('/amazon-prime', (req, res, next) => {
    database
    .ref('movie-reviews')
    .once('value', (snapshot) => {

        let reviews = snapshot.val();
        let movies  = [];
        let count   = 0;

        for(item in reviews) {
            if(reviews[item]['amazon']) {
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
                url      : process.env.SERVER + '/movie-reviews/amazon-prime'
            },
            response : movies
        });

    });
});
//=================================================================================





//=================================================================================
// GET ALL MOVIES AVAILABLE ON NETFLIX

router.get('/netflix', (req, res, next) => {
    database
    .ref('movie-reviews')
    .once('value', (snapshot) => {

        let reviews = snapshot.val();
        let movies  = [];
        let count   = 0;

        for(item in reviews) {
            if(reviews[item]['netflix']) {
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
                url      : process.env.SERVER + '/movie-reviews/netflix'
            },
            response : movies
        });

    });
});
//=================================================================================






module.exports = router;