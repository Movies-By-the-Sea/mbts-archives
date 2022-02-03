const { db, auth } = require("../firebase");
const database     = require("../models/database")
const utils        = require("../models/utils");
require("dotenv").config({path:"../.env"});





//=====================================================================
//=====================================================================

async function isAuthorized(req, res, next, authLevel) {
    await auth
    .getUser(req.body.uid)
    .then((userRecord) => {
        if(userRecord.customClaims['accessLevel'] >= authLevel) {
            return next();
        } else {
            return res
                .status(400)
                .json({
                    error : {
                        message : "Access level unauthorized"
                    }
                });
        }
    })
};

//=====================================================================
//=====================================================================



//=====================================================================
//=====================================================================

async function sharedAuthorize(uid, author_uid, level) {
    const authLevel = database.getAccessLevel(uid);
    if((author_uid === uid) || authLevel >= level) {
        return true;
    }
    return false;
}

//=====================================================================
//=====================================================================



//=====================================================================
//=====================================================================

function isAuthenticated(req, res, next) {
    if((req.body.email !== undefined) && (req.body.password != undefined)) {
        return next();
    }
    if(req.body.uid === undefined) {
        return res.status(401).json({message : "Unauthorized"});
    }
    return next();
}

//=====================================================================
//=====================================================================



//=====================================================================
//=====================================================================

function enforcer(req, res, next) {
    if(req.body.table === undefined) {
        return next();
    } else {
        if(req.body.table === 'users') {
            return res.status(400).json({error : {message: "Cannot access this table"}});
        }
    }
    return next();
}

//=====================================================================
//=====================================================================





module.exports = {
    isAuthorized   : isAuthorized,
    isAuthenticated: isAuthenticated,
    sharedAuthorize: sharedAuthorize,
    enforcer       : enforcer 
};