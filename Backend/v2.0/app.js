const reviewRoute  = require("./routes/reviews");
const instaRoute   = require("./routes/instagram");
const adminRoute   = require("./routes/admin");
const userRoute    = require("./routes/user");
const auth         = require("./Auth/authorize");

const express      = require("express");
const cors         = require("cors");
const app          = express();


// MIDDLEWARES
app.use(cors({origin: true}));
app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.use(auth.enforcer);



// PRIMARY ROUTES
app.get('/',          (req, res)=> res.status(200).json({"message":"Hello world"}));
app.use("/user",      userRoute);
app.use("/admin",     adminRoute);
app.use("/reviews",   reviewRoute);
app.use("/instagram", instaRoute);



// HANDLING SERVER SIDE ERRORS
app.use((req, res, next) => {
    const error  = new Error('Route Not found');
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