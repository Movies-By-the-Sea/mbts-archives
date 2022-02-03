const axios = require("axios");
require('dotenv').config();

function getCreds() {
    return {
        // HAS LONG LIVE ACCESS TOKEN HERE
        access_token        : process.env.ACCESS_TOKEN,
        client_id           : process.env.GRAPH_CLIENT_ID,
        client_secret       : process.env.GRAPH_CLIENT_SECRET,
        graph_domain        : process.env.GRAPH_DOMAIN,
        graph_version       : process.env.GRAPH_VERSION,
        endpoint_base       : process.env.GRAPH_ENDPOINT_BASE,
        page_id             : process.env.PAGE_ID,
        instagram_account_id: process.env.IG_ACCOUNT_ID,
        ig_username         : process.env.IG_USERNAME,
        debug               : "no"
    }
}

async function makeAPICalls(url, endpoints, debug) {
    let res = await axios.get(url, {
        params: endpoints
    });
    let result = {
        url            : url,
        endpoint_params: endpoints,
        data           : res.data
    }
    if(debug === "yes") {
        console.log(result);
    }
    return result;
}

module.exports = {
    getCreds    : getCreds,
    makeAPICalls: makeAPICalls
}