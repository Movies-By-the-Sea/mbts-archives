const { db, auth } = require("../firebase");
const utils        = require("../models/utils");
const bcrypt       = require("bcrypt");
require("dotenv").config({path:"../.env"});
const saltRounds = parseInt(process.env.SALT_ROUNDS);





//=====================================================================
//=====================================================================

async function createUser(req, res) {
    const { name, email, password, accessLevel } = req.body;
    if(!name || !email || !password || !accessLevel) {
        return utils.formatResponse(req, res, 400, {message: 'Missing Fields'});
    };
    if(accessLevel > 5) {
        return utils.formatResponse(req, res, 400, {message: 'Cannot have access level above 5'});
    };
    const hash = await bcrypt.hash(password, saltRounds);
    await auth.createUser({
        name    : name,
        email   : email,
        password: hash
    })
    .then(async (userRecord) => {
        await auth.setCustomUserClaims(userRecord.uid, {
            accessLevel: accessLevel
        });
        await db
        .collection("users")
        .doc(userRecord.uid)
        .set({
            name       : name,
            email      : email,
            accessLevel: accessLevel,
            password   : hash
        });
        info = {
            remark     : 'User successfully created',
            requestType: 'POST',
            URL        : '/admin' + '/create',
            response   : userRecord
        };
        return utils.formatResponse(req, res, 200, info);
    })
};

//=====================================================================
//=====================================================================





//=====================================================================
//=====================================================================

async function deleteUser(req, res) {
    db
    .collection("users")
    .doc(req.body.delete_uid)
    .delete()
    .then(async () => {
        await auth
            .deleteUser(req.body.delete_uid)
            .then(() => {
                info = {
                    remark     : 'User deleted successfully',
                    requestType: 'DELETE'
                }
                return utils.formatResponse(req, res, 200, info);
            });
    });
};

//=====================================================================
//=====================================================================





//=====================================================================
//=====================================================================

async function getAllUsers(req, res) {
    auth
    .listUsers()
    .then((userRecords) => {
        info = {
            URL     : '/admin',
            response: userRecords.users
        };
        return utils.formatResponse(req, res, 200, info);
    })
}

//=====================================================================
//=====================================================================





//=====================================================================
//=====================================================================

async function updateClaim(req, res) {
    if((req.body.accessLevel > 5) || (req.body.accessLevel <= 0)) {
        return utils.formatResponse(req, res, 400, {message:'Specified access level invalid'})
    };
    await auth
        .setCustomUserClaims(req.body.update_uid, {
            accessLevel: req.body.accessLevel
        })
        .then(async () => {
            const ref = db.collection("users").doc(req.body.update_uid);
            await ref.update({
                accessLevel: req.body.accessLevel
            });
            info = {
                remark     : 'User claims updated successfully',
                URL        : '/admin' + '/claims',
                requestType: 'PATCH'
            };
            return utils.formatResponse(req, res, 200, info);
        })
}

//=====================================================================
//=====================================================================





module.exports = {
    createUser : createUser,
    deleteUser : deleteUser,
    getAllUsers: getAllUsers,
    updateClaim: updateClaim
}