// const firebase   = require('firebase');
// require('dotenv').config();

// const firebaseConfig = {
//     apiKey           : process.env.API_KEY,
//     authDomain       : process.env.AUTH_DOMAIN,
//     databaseURL      : process.env.DATABASE_URL,
//     projectId        : process.env.PROJECT_ID,
//     storageBucket    : process.env.STORAGE_BUCKET,
//     messagingSenderId: process.env.MESSAGING_SENDER_ID,
//     appId            : process.env.APP_ID
// };
// if(!firebase.apps.length) {
//     firebase.initializeApp(firebaseConfig);
// }
// const database = firebase.database();

// // firebase.auth().signInWithEmailAndPassword(process.env.FIREBASE_AUTH_EMAIL, process.env.FIREBASE_AUTH_PASSWORD)
// //     .then((userCredentials) => {
// //         var user = userCredentials.user;
// //     })
// //     .catch((error) => {
// //         var errorCode = error.code;
// //         var errorMessage = error.message;
// //     })

// module.exports = database;

const admin = require("firebase-admin");
require("dotenv").config();

const firebaseConfig = {
  apiKey: process.env.API_KEY,
  authDomain: process.env.AUTH_DOMAIN,
  databaseURL: process.env.DATABASE_URL,
  projectId: process.env.PROJECT_ID,
  storageBucket: process.env.STORAGE_BUCKET,
  messagingSenderId: process.env.MESSAGING_SENDER_ID,
  appId: process.env.APP_ID,
  measurementId: process.env.MEASUREMENT_ID,
};
admin.initializeApp(firebaseConfig);

const db = admin.firestore();
module.exports = db;