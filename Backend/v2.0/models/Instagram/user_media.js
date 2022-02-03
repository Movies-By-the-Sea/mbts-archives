const utils = require("./utils");

async function getUserMedia(params) {
    let endpointParams = {
        fields      : "id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username",
        access_token: params.access_token
    };
    let url = params.endpoint_base + params.instagram_account_id + "/media";
    return await utils.makeAPICalls(url, endpointParams, params.debug);
}

// let params = utils.getCreds();
// params['debug'] = 'no';
// getUserMedia(params)
// .then((resp) => console.log(`
//     \n---- LATEST POST ----\n
//     Link to post : \t${resp['data']['data'][0]['permalink']}
//     Media Type   : \t${resp['data']['data'][0]['media_type']}
//     Posted at    : \t${resp['data']['data'][0]['timestamp']}
//     Post Caption : \n\n${resp['data']['data'][0]['caption']}
// `))