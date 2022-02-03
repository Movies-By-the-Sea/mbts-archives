const express = require("express");
const ash = require("express-async-handler");
const db = require("../../firebase");
const router = express.Router();
require("dotenv").config();


// =================================================================================
// GET ALL REVIEWS

router.get("/", ash(async (req, res) => {
  const data = [];
  const reviewsRef = db.collection(String(req.body.table));
  const snapshot = await reviewsRef.orderBy("timestamp").get();
  snapshot.forEach((doc) => {
    data.push({
      "ID": doc.id,
      "Data": doc.data(),
    });
  });
  return res
      .status(200)
      .json({
        message: "Query successful",
        size: data.length,
        request: {
          type: "GET",
          url: process.env.SERVER + req.body.table + "/reviews",
        },
        response: data,
      });
}));

// =================================================================================


// =================================================================================
// GET REVIEW OF FILM SPECIFIED BY ID

router.get("/get", ash(async (req, res) => {
  const reviewRef = db.collection(String(req.body.table)).doc(req.body.id);
  const doc = await reviewRef.get();
  if (!doc.exists) {
    return res
        .status(404)
        .json({
          message: "No such review with given ID found",
        });
  } else {
    return res
        .status(200)
        .json({
          message: "Query successful",
          movie_id: req.body.id,
          request: {
            type: "GET",
            url: process.env.SERVER + "/reviews" + "/get",
          },
          response: doc.data(),
        });
  }
}));

// =================================================================================


// ==================================================================================
// GETTING GENERAL INFO

async function getData(table, query) {
  const data = {
    size: 0,
    response: [],
  };
  let counter = 0;
  const reviewRef = db.collection(String(table));
  const snap = await reviewRef
      .where(query, "==", true)
      .get();
  snap.forEach((doc) => {
    data.response.push(doc.id);
    counter++;
  });
  data.size = counter;
  return data;
}

router.get("/general", ash(async (req, res) => {
  return res
      .status(200)
      .json({
        message: "Query successful",
        request: {
          type: "GET",
          url: process.env.SERVER + "/reviews" + "/general",
        },
        response: {
          Instagram: await getData(req.body.table, "instagram"),
          Netflix: await getData(req.body.table, "netflix"),
          Prime: await getData(req.body.table, "prime"),
          Must_Watch: await getData(req.body.table, "must_watch"),
          Foreign: await getData(req.body.table, "foreign"),
        },
      });
}));

// ==================================================================================


module.exports = router;
