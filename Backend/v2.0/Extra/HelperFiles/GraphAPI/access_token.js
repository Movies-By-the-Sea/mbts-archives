const util = require("../../../models/Instagram/utils");

async function debugAccessToken(params) {
    endpointParams = {
        input_token : params.access_token,
        access_token: params.access_token
    };
    url = params.graph_domain + "/debug_token";
    return await util.makeAPICalls(url, endpointParams, params.debug);
}


// let params = util.getCreds();
// params.debug = "no";
// debugAccessToken(params)
// .then((resp) => console.log(`Expires at : ${new Date(resp['data']['data']['expires_at']).toTimeString()}`));