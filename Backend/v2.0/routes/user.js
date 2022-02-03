const express      = require('express');
const asyncHandler = require('express-async-handler');
const auth         = require("../Auth/authorize");
const user         = require("../models/users");
const router       = express.Router();



// THESE ROUTES ARE ACCESSIBLE BY ANY USER HAVING VALID UID TOKENS
router.get("/",
    asyncHandler((req, res, next) => auth.isAuthenticated(req, res, next)),
    asyncHandler((req, res)       => user.getInfo(req, res))
);
router.put("/update",
    asyncHandler((req, res, next) => auth.isAuthenticated(req, res, next)),
    asyncHandler((req, res)       => user.updateInfo(req, res))
)
router.get("/posts",
    asyncHandler((req, res, next) => auth.isAuthenticated(req, res, next)),
    asyncHandler((req, res)       => user.getUserPosts(req, res))
);



module.exports = router;