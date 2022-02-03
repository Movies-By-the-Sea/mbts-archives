const { db, admin } = require("../firebase");
const auth          = require("../Auth/authorize");
const utils         = require("./utils");





//=====================================================================================
//=====================================================================================

async function updateIGStatus(req, res) {
  const ref = db.collection(String(req.body.table)).doc(req.body.id);
  const doc = await ref.get();
  if (!doc.exists) {
    return utils.formatResponse(req, res, 404, {message:'No such review with given ID found'});
  } else {
    await ref.update({
      "instagram": req.body.instagram,
    });
    info = {
      size       : 0,
      remark     : 'Review IG status updated successfully',
      requestType: 'PATCH',
      URL        : '/reviews' + '/updateIG'
    }
    return utils.formatResponse(req, res, 200, info);
  }
}

//=====================================================================================
//=====================================================================================





//=====================================================================================
//=====================================================================================

async function updateReview(req, res) {
  const ref = db.collection(req.body.table).doc(req.body.id);
  const doc = await ref.get();
  if (!doc.exists) {
    return utils.formatResponse(req, res, 404, {message:'No such review with given ID found'});
  } else {
    const bool = await auth.sharedAuthorize(req.body.uid, doc.data().author_uid, 3);
    if(bool) {
      await ref.update(req.body.update_data);
      info = {
        size       : 0,
        remark     : 'Review updated successfully',
        requestType: 'PUT',
        URL        : '/reviews' + '/update'
      }
      return utils.formatResponse(req, res, 200, info);
    } else {
      return utils.formatResponse(req, res, 400, {message:'Do not have permission to update another user posts'});
    }
  }
}

//=====================================================================================
//=====================================================================================





//=====================================================================================
//=====================================================================================

async function uploadReview(req, res) {
    let data        = req.body.update_data;
    data.author     = req.body.author;
    data.author_uid = req.body.uid
    const doc = await db.collection(req.body.table).add(data);
    info = {
      size       : 1,
      remark     : 'Review uploaded successfully',
      requestType: 'POST',
      URL        : '/reviews' + '/upload',
      response   : doc.id
    }
    return utils.formatResponse(req, res, 200, info);   
}

//=====================================================================================
//=====================================================================================





//=====================================================================================
//=====================================================================================

async function deleteReview(req, res) {
  const ref = db.collection(req.body.table).doc(req.body.id);
  const doc = await ref.get();
  const bool = await auth.sharedAuthorize(req.body.uid, doc.data().author_uid, 3);
  if(bool) {
    await db.collection(req.body.table).doc(req.body.id).delete();
    info = {
      size       : 0,
      remark     : 'Review deleted successfully',
      requestType: 'DELETE',
      URL        : '/reviews' + '/delete'
    }
    return utils.formatResponse(req, res, 200, info);
  } else {
    return utils.formatResponse(req, res, 400, {message:'Do not have permission to update another user posts'});
  }
}

//=====================================================================================
//=====================================================================================





module.exports = {
    updateIGStatus: updateIGStatus,
    updateReview  : updateReview,
    uploadReview  : uploadReview,
    deleteReview  : deleteReview
}