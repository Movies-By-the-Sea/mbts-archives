const express      = require('express');
const asyncHandler = require('express-async-handler');
const operations   = require("../models/operations");
const reviews      = require("../models/reviews");
const auth         = require("../Auth/authorize");
const router       = express.Router();



// THESE ROUTES ARE ACCESSIBLE PUBLICALLY  |  MASKED ONLY IF UID IS NOT SPECIFIED
router.get("/",    asyncHandler((req, res) => reviews.getAllReviews(req, res)));
router.get("/get", asyncHandler((req, res) => reviews.getReviewByID(req, res)));



// ONLY AUTHLEVEL 1 USERS CAN ACCESS THESE ROUTES
router.get("/general",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 1)),
    asyncHandler((req, res)       => reviews.getGeneralInfo(req, res))
);



// ONLY AUTHLEVEL 2 USERS CAN ACCESS THESE ROUTES
router.post("/upload",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 2)),
    asyncHandler((req, res)       => operations.uploadReview(req, res))
);



// MANAGER AND WRITERS WITH MATCHING AUTHOR_UID CAN UNIVERSALLY USE THESE
router.put("/update",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 2)),
    asyncHandler((req, res)       => operations.updateReview(req, res))
);
router.delete("/delete",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 2)),
    asyncHandler((req, res)       => operations.deleteReview(req, res))
);



// ONLY AUTHLEVEL 3 USERS CAN ACCESS THESE ROUTES
router.patch("/updateIG",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 3)),
    asyncHandler((req, res)       => operations.updateIGStatus(req, res))
);





module.exports = router;