const database = require("./database");
require("dotenv").config();


  


//=====================================================================
//=====================================================================

async function maskDataByAuth(req, getUnique=false) {
    const data = getUnique ? await database.getDataByTableID(req.body.table, req.body.id) : await database.getAllData(req.body.table);
    if((data[0] === undefined) && getUnique) {
        return {
            data: "No such review with given ID found",
            type: "Invalid request"
        }
    }
    if(req.body.uid === undefined) {
        let publicData = new Array();
        data.forEach((doc) => {
            publicData.push({
                "ID"  : doc.id,
                "data": {
                  name    : doc.name,
                  director: doc.director,
                  year    : doc.year,
                  lead    : doc.lead,
                  genre   : doc.genre,
                  review  : doc.review,
                  poster  : doc.poster,
                  ratings : {
                    story     : doc.story,
                    acting    : doc.acting,
                    execution : doc.execution,
                    profundity: doc.profundity,
                    overall   : doc.overall
                  },
                  foreign     : doc.foreign,
                  must_watch  : doc.must_watch,
                  amazon_prime: doc.prime,
                  netflix     : doc.netflix,
                  trailer     : doc.trailer
                }
              });
        })
        return {
            data: publicData,
            type: "Public Request"
        };
    } else {
        if(await database.getAccessLevel(req.body.uid) === 5) {
            return {
                data: data,
                type: "Admin Request"
            };
        } else {
            let temp = data;
            temp.forEach((doc) => doc.author_uid = "access denied");
            return {
                data: temp,
                type: "Non-admin authorized request"
            };
        }
    }
}

//=====================================================================
//=====================================================================





//=====================================================================
//=====================================================================

function mapAccessLevel(accessLevel) {
    switch(accessLevel) {
        case 1 : return "Reader Access";
        case 2 : return "Writer Access";
        case 3 : return "Manager Access";
        case 4 : return "Analytics Access";
        case 5 : return "Admin Access";
        default: return "Public Access";
    }
}

//=====================================================================
//=====================================================================





//=====================================================================
//=====================================================================

async function formatResponse(req, res, status, resp) {
    if(status != 200) {
        return res.status(status).json({
            error: { message: resp.message }
        });
    };
    let info = {
        remark : resp.remark || "Query successful",
        request: {
            type: resp.requestType || 'GET',
            auth: resp.auth || mapAccessLevel(await database.getAccessLevel(req.body.uid)),
            URL : process.env.SERVER + resp.URL,
            body: req.body || []
        },
        response: resp.response
    }
    if(resp.response === undefined) {
        info.size = resp.size || 0
    } else {
        info.size = resp.response.length
    }
    
    return res.status(status).json(info)
}

//=====================================================================
//=====================================================================





module.exports = {
    maskDataByAuth        : maskDataByAuth,
    formatResponse        : formatResponse,
}