const express      = require('express');
const asyncHandler = require('express-async-handler');
const auth         = require("../Auth/authorize");
const admin        = require("../Auth/admin");
const router       = express.Router();



// ONLY AUTHLEVEL 5 USERS CAN CREATE OTHER USERS
router.get("/",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 5)),
    asyncHandler((req, res)       => admin.getAllUsers(req, res))
);
router.post("/create",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 5)),
    asyncHandler((req, res)       => admin.createUser(req, res))
);
router.delete("/delete",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 5)),
    asyncHandler((req, res)       => admin.deleteUser(req, res))
);
router.patch("/claims",
    asyncHandler((req, res, next) => auth.isAuthorized(req, res, next, 5)),
    asyncHandler((req, res)       => admin.updateClaim(req, res))
);



module.exports = router;