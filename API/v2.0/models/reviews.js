const utils = require("./utils");
const db    = require("./database");





//=====================================================================================
//=====================================================================================

async function getAllReviews(req, res) {
  await utils.maskDataByAuth(req).then((result) => {
    info = {
      remark     : "Reviews ordered by timestamp",
      auth       : result.type,
      URL        : '/reviews',
      response   : result.data
    };
    return utils.formatResponse(req, res, 200, info); 
  })
}

//=====================================================================================
//=====================================================================================





//=====================================================================================
//=====================================================================================

async function getReviewByID(req, res) {
  await utils.maskDataByAuth(req, getUnique=true).then((result) => {
    info = {
      auth       : result.type,
      URL        : '/reviews' + '/get',
      response   : result.data
    }
    return utils.formatResponse(req, res, 200, info);
  })
}

//=====================================================================================
//=====================================================================================





//=====================================================================================
//=====================================================================================

async function getGeneralInfo(req, res) {
  info = {
    URL        : '/reviews' + '/general',
    response   : {
      Total     : await db.getDataSize(req.body.table),
      Instagram : await db.getQueryData(req.body.table, "instagram"),
      Netflix   : await db.getQueryData(req.body.table, "netflix"),
      Prime     : await db.getQueryData(req.body.table, "prime"),
      Must_Watch: await db.getQueryData(req.body.table, "must_watch"),
      Foreign   : await db.getQueryData(req.body.table, "foreign"),
      Genre     : {
        Lighthearted : await db.getDataByGenre(req.body.table, "Lighthearted"),
        Comedy       : await db.getDataByGenre(req.body.table, "Comedy"),
        Romance      : await db.getDataByGenre(req.body.table, "Romance"),
        Horror       : await db.getDataByGenre(req.body.table, "Horror"),
        Thriller     : await db.getDataByGenre(req.body.table, "Thriller"),
        Animated     : await db.getDataByGenre(req.body.table, "Animated"),
        Dark         : await db.getDataByGenre(req.body.table, "Dark"),
        Meta         : await db.getDataByGenre(req.body.table, "Meta"),
        War          : await db.getDataByGenre(req.body.table, "War"),
        Crime        : await db.getDataByGenre(req.body.table, "Crime"),
        Inspirational: await db.getDataByGenre(req.body.table, "Inspirational"),
        Sci_Fi       : await db.getDataByGenre(req.body.table, "Sci_Fi"),
        True_Story   : await db.getDataByGenre(req.body.table, "True_Story"),
        Drama        : await db.getDataByGenre(req.body.table, "Drama"),
        Fantasy      : await db.getDataByGenre(req.body.table, "Fantasy"),
        Action       : await db.getDataByGenre(req.body.table, "Action"),
        Indie        : await db.getDataByGenre(req.body.table, "Indie"),
        Mystery      : await db.getDataByGenre(req.body.table, "Mystery"),
      }
    }
  };
  return utils.formatResponse(req, res, 200, info);
}

//=====================================================================================
//=====================================================================================





module.exports = {
    getAllReviews : getAllReviews,
    getReviewByID : getReviewByID,
    getGeneralInfo: getGeneralInfo
}