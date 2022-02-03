const admin = require("firebase-admin");
require("dotenv").config({path:"./.env"});
const serviceAccount = {
  "type"                       : process.env.TYPE,
  "project_id"                 : process.env.PROJECT_ID,
  "private_key_id"             : process.env.PRIVATE_KEY_ID,
  "private_key"                : process.env.PRIVATE_KEY.replace(/\\n/g, '\n'),
  "client_email"               : process.env.CLIENT_EMAIL,
  "client_id"                  : process.env.CLIENT_ID,
  "auth_uri"                   : process.env.AUTH_URI,
  "token_uri"                  : process.env.TOKEN_URI,
  "auth_provider_x509_cert_url": process.env.AUTH_PROVIDER_X509_CERT_URL,
  "client_x509_cert_url"       : process.env.CLIENT_X509_CERT_URL
}

admin.initializeApp({
  credential : admin.credential.cert(serviceAccount)
});

admin.firestore().collection("short-film-reviews").get().then(function(querySnapshot) {
    querySnapshot.forEach(function(doc) {
        console.log(doc.id);
        doc.ref.update({
            author: 'writer@mbts.com',
        });
    });
});