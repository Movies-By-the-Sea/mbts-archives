const express      = require('express');
const asyncHandler = require('express-async-handler');
const insights     = require('../models/ig_insights');
const auth         = require("../Auth/authorize");
const router       = express.Router();



// ONLY AUTHLEVEL 4 USERS CAN ACCESS THESE ROUTES
router.get("/",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 4)),
    asyncHandler((req, res)       => insights.getBusinessInfo(req, res))
);
router.get("/users",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 4)),
    asyncHandler((req, res)       => insights.getDailyUserInsights(req, res))
);
router.get("/latest",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 4)),
    asyncHandler((req, res)       => insights.getLatestPost(req,res))
);
router.get("/insights",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 4)),
    asyncHandler((req, res)       => insights.getPostInsights(req, res)));

    

module.exports = router;