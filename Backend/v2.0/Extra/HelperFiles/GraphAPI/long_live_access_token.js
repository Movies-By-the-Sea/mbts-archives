const utils = require("../../../models/Instagram/utils");

async function getLongLiveAccessToken(params) {
    let endpointParams = {
        grant_type       : "fb_exchange_token",
        client_id        : params.client_id,
        client_secret    : params.client_secret,
        fb_exchange_token: params.access_token
    };
    let url = params.endpoint_base + "oauth/access_token";
    return await utils.makeAPICalls(url, endpointParams, params.debug);
}

// let params = utils.getCreds();
// params.debug = "no";
// getLongLiveAccessToken(params)
// .then((resp) => console.log(`Long live access token : \n${resp['data']['access_token']}`));