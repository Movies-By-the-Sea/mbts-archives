const express = require("express");
const ash = require("express-async-handler");
const db = require("../../firebase");
const router = express.Router();
require("dotenv").config();


// =======================================================================================
// UPDATING INSTAGRAM STATUS

router.patch("/updateIG", ash(async (req, res) => {
  const ref = db.collection(String(req.body.table)).doc(req.body.id);
  const doc = await ref.get();
  if (!doc.exists) {
    return res
        .status(404)
        .json({
          message: "No such review with given ID found",
        });
  } else {
    await ref.update({
      "instagram": req.body.instagram,
    });
    return res
        .status(200)
        .json({
          message: "Query successful",
          id: req.body.id,
          table: req.body.table,
          instagram: req.body.instagram,
          request: {
            type: "PATCH",
            url: process.env.SERVER + "/operations" + "/updateIG",
          },
        });
  }
}));

// =======================================================================================


// =======================================================================================
// UPDATING A REVIEW

router.put("/update", ash(async (req, res) => {
  const ref = db.collection(String(req.body.table)).doc(req.body.id);
  const doc = await ref.get();
  if (!doc.exists) {
    return res
        .status(404)
        .json({
          message: "No such review with given ID found",
        });
  } else {
    await ref.update(req.body.update_data);
    return res
        .status(200)
        .json({
          message: "Query successful",
          id: req.body.id,
          table: req.body.table,
          update_data: req.body.update_data,
          request: {
            type: "PATCH",
            url: process.env.SERVER + "/operations" + "/updateIG",
          },
        });
  }
}));

// =======================================================================================


// ==================================================================================
// WRTING A REVIEW

router.post("/upload", ash(async (req, res) => {
  const data = {
    name: req.body.name,
    director: req.body.director,
    genre: req.body.genre,
    instagram: req.body.instagram,
    poster_name: req.body.poster_name,
    poster_link: req.body.poster_link,
  };
  const table = req.body.table;
  if (table == "movie-reviews") {
    data.review = req.body.review;
    data.year = req.body.year;
    data.actor = req.body.actor;
    data.netflix = req.body.netflix;
    data.amazon = req.body.amazon;
    data.acting = req.body.acting;
    data.story = req.body.story;
    data.execution = req.body.execution;
    data.profundity = req.body.profundity;
    data.overall = req.body.overall;
    data.trailer = req.body.trailer;
  } else if (table == "short-film-reviews") {
    data.link = req.body.link;
    data.description = req.body.description;
    data.duration = req.body.duration;
  }
  const doc = await db.collection(req.body.table).add(data);
  return res
      .status(200)
      .json({
        message: "Post added successfully",
        request: {
          type: "POST",
          url: process.env.SERVER + "/operations" + "/upload",
        },
        response: {
          table: req.body.table,
          id: doc.id,
          data_uploaded: data,
        },
      });
}));

// =======================================================================================


// =======================================================================================
// DELETING REVIEW

router.delete("/delete", ash(async (req, res) => {
  await db.collection(req.body.table).doc(req.body.id).delete();
  return res
      .status(200)
      .json({
        message: "Document deleted successfully",
        request: {
          type: "DELETE",
          url: process.env.SERVER + "/operations" + "/delete",
        },
      });
}));

// =======================================================================================


module.exports = router;
