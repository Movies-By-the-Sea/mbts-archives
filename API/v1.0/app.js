const express = require('express');
const morgan  = require('morgan');


// const movieReviewRoutes      = require('./api/routes/movie-reviews');
// const shortFilmReviewsRoutes = require('./api/routes/short-film-reviews');
// const operations             = require('./api/routes/op_bla');
const reviewRoute = require("./api/routes/reviews");
const operationsRoute = require("./api/routes/operations");
require('dotenv').config();



// REQUIRED MIDDLEWARES
const app = express();
app.use(morgan('dev'));
app.use(express.static(__dirname))
app.use(express.urlencoded({ extended: true }));
app.use(express.json());



// API ROUTES
app.get('/hello', (req, res) => {
    return res.status(200).json({
        message : "Hello world!"
    });
});
app.use("/reviews", reviewRoute);
app.use("/operations", operationsRoute);
// app.use('/movie-reviews',      movieReviewRoutes);
// app.use('/short-film-reviews', shortFilmReviewsRoutes);
// app.use('/operations',         operations);



// ALLOW CORS REQUESTS
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header(
        'Access-Control-Allow-Headers', 
        'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    ); 
    if(req.method == 'OPTIONS') {  
        res.header('Access-Control-Allow-Methods', 'PUT, POST, PATCH, DELETE, GET');
        return res.status(200).json({});
    }
    next();
});



// HANDLING SERVER SIDE ERRORS
app.use((req, res, next) => {
    const error  = new Error('Not found');
    error.status = 400;
    next(error);  
})
app.use((error, req, res, next) => {
    res.status(error.status || 500);
    res.json({
        error : {
            message : error.message, 
        }
    });
});




module.exports = app;