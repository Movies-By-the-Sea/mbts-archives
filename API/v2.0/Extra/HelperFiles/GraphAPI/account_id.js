const { getCreds } = require("../../../models/Instagram/utils");
const utils        = require("../../../models/Instagram/utils");

async function getInstagramAccount(params) {
    let endpointParams = {
        access_token: params.access_token,
        fields      : "instagram_business_account"
    };
    url = params.endpoint_base + params.page_id;
    return await utils.makeAPICalls(url, endpointParams, params.debug);
};

// let params = getCreds();
// params['debug'] = 'no';
// getInstagramAccount(params)
// .then((resp) => console.log(`
//     \n---- INSTAGRAM ACCOUNT INFO ----\n
//     Page ID: \t\t\t${resp['data']['id']}
//     IG Business Account ID: \t${resp['data']['instagram_business_account']['id']}
// `));