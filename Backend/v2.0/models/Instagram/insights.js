const utils = require("./utils");



async function getUserMedia(params) {
    let endpointParams = {
        fields      : "id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username",
        access_token: params.access_token
    };
    let url = params.endpoint_base + params.instagram_account_id + "/media";
    return await utils.makeAPICalls(url, endpointParams, params.debug);
};



async function getMediaInsights(params) {
    let endpointParams = {
        metric      : "engagement,impressions,reach,saved",
        access_token: params.access_token
    };
    let url = params.endpoint_base + params.latest_media_id + "/insights";
    return await utils.makeAPICalls(url, endpointParams, params.debug);
}



async function getUserInsights(params) {
    let endpointParams = {
        metric      : "follower_count,impressions,profile_views,reach",
        period      : "day",
        access_token: params.access_token
    };
    let url = params.endpoint_base + params.instagram_account_id + "/insights";
    return await utils.makeAPICalls(url, endpointParams, params.debug);
}



// params = utils.getCreds();
// getUserMedia(params)
//     .then((resp) => console.log(`
//         \n---- LATEST POST ----\n
//         Link to post : \t${resp['data']['data'][0]['permalink']}
//         Media type   : \t${resp['data']['data'][0]['media_type']}
//         Posted at    : \t${resp['data']['data'][0]['timestamp']}
//         Caption      : \n${resp['data']['data'][0]['caption']}
//     `));

// getUserMedia(params)
// .then((resp) => {
//     let posts = resp['data']['data'];
//     posts.forEach((item,i) => {
//         let params = utils.getCreds();
//         params['latest_media_id'] = item['id'];
//         getUserInsights(params)
//         .then((response) => {
//             insights = response['data']['data'];
//             console.log(`\n---- POST INSIGHTS ----\n`);
//             insights.forEach((ins, i) => console.log(`
//                 Title       :\t\t${ins.title}
//                 Period      :\t\t${ins.period}
//                 Description :\t${ins.description}
//                 Value       :\n${ins.values}
//             `))
//         })
//     });
// })



module.exports = {
    getMediaInsights: getMediaInsights,
    getUserInsights : getUserInsights,
    getUserMedia    : getUserMedia
}