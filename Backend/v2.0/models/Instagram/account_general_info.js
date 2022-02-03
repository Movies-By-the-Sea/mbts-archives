const utils = require("./utils");

async function getAccountInfo(params) {
    let endpointParams = {
        fields      : "business_discovery.username(" + params.ig_username + "){username,website,name,ig_id,profile_picture_url,biography,follows_count,followers_count,media_count}",
        access_token: params.access_token
    };
    let url = params.endpoint_base + params.instagram_account_id;
    return await utils.makeAPICalls(url, endpointParams, params.debug);
}

// let params = utils.getCreds();
// params['debug'] = 'no';
// getAccountInfo(params)
// .then((resp) => console.log(`
// \n---- ACCOUNT INFO ----\n
// Username            : \t\t${resp['data']['business_discovery']['username']}
// Website             : \t\t${resp['data']['business_discovery']['website']}
// Number of posts     : \t${resp['data']['business_discovery']['media_count']}
// Followers           : \t\t${resp['data']['business_discovery']['followers_count']}
// Following           : \t\t${resp['data']['business_discovery']['follows_count']}
// Profile Picture URL : \t${resp['data']['business_discovery']['profile_picture_url']}
// Biography           : \t\t${resp['data']['business_discovery']['biography']}
// `));

module.exports = getAccountInfo