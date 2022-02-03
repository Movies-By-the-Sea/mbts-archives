const utils = require("../../../models/Instagram/utils");

async function getUserPages(params) {
    let endpointParams = {
        access_token: params.access_token
    }
    let url = params.endpoint_base + "me/accounts";
    return await utils.makeAPICalls(url, endpointParams, params.debug);
}

// let params = utils.getCreds();
// params['debug'] = 'no';
// getUserPages(params)
// .then((resp) => console.log(`
//     \n---- FACEBOOK PAGE INFO ----\N
//     Page Name: \t\t${resp['data']['data'][0]['name']}
//     Page Category: \t${resp['data']['data'][0]['category']}
//     Page ID: \t\t${resp['data']['data'][0]['id']}
// `));