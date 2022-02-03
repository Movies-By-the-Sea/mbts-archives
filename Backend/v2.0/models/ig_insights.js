const instagram   = require('./Instagram/insights');
const accountInfo = require("./Instagram/account_general_info");
const ig          = require('./Instagram/utils');
const utils       = require("./utils");





//=====================================================================
//=====================================================================

async function getLatestPost(req, res) {
    await instagram
    .getUserMedia(ig.getCreds())
    .then((resp) => {
        info = {
            URL     : '/instagram' + '/latest',
            response: resp.data['data'][0]
        }
        return utils.formatResponse(req, res, 200, info)
    });
};

//=====================================================================
//=====================================================================





//=====================================================================
//=====================================================================

async function getBusinessInfo(req, res) {
    await accountInfo(ig.getCreds())
    .then((resp) => {
        info = {
            URL     : '/instagram',
            response: resp.data.business_discovery
        }
        return utils.formatResponse(req, res, 200, info);
    });
};

//=====================================================================
//=====================================================================





//=====================================================================
//=====================================================================

async function getAllPosts() {
    const result = [];
    await instagram
    .getUserMedia(ig.getCreds())
    .then((resp) => {
        posts = resp['data']['data'];
        posts.forEach((item, i) => {
            result.push({
                id       : item['id'],
                timestamp: item['timestamp']
            });
        });
    });
    return result
};

//=====================================================================
//=====================================================================





//=====================================================================
//=====================================================================

async function getPostInsights(req, res) {
    let posts    = await getAllPosts();
    let insights = [];
    for(const item of posts) {
        let params = ig.getCreds();
        params['latest_media_id'] = item['id'];
        await instagram
        .getMediaInsights(params)
        .then((resp) => {
            insights.push({
                id       : item['id'],
                timestamp: item['timestamp'],
                insights : {
                    engagement: {
                        period     : resp['data']['data'][0]['period'],
                        description: resp['data']['data'][0]['description'],
                        values     : resp['data']['data'][0]['values']
                    },
                    impressions: {
                        period     : resp['data']['data'][1]['period'],
                        description: resp['data']['data'][1]['description'],
                        values     : resp['data']['data'][1]['values']
                    },
                    reach: {
                        period     : resp['data']['data'][2]['period'],
                        description: resp['data']['data'][0]['description'],
                        values     : resp['data']['data'][2]['values']
                    },
                    saved: {
                        period     : resp['data']['data'][3]['period'],
                        description: resp['data']['data'][3]['description'],
                        values     : resp['data']['data'][3]['values']
                    }
                }
            });
        });
    };
    info = {
        URL     : '/instagram' + '/insights',
        response: insights
    };
    return utils.formatResponse(req, res, 200, info)
};

//=====================================================================
//=====================================================================





//=====================================================================
//=====================================================================

async function getDailyUserInsights(req, res) {
    let params = ig.getCreds();
    await instagram
    .getUserInsights(params)
    .then((resp) => {
        info = {
            URL     : '/instagram' + '/users',
            response: resp.data['data']
        };
        return utils.formatResponse(req, res, 200, info);
    })
}

//=====================================================================
//=====================================================================





module.exports = {
    getLatestPost       : getLatestPost,
    getBusinessInfo     : getBusinessInfo,
    getPostInsights     : getPostInsights,
    getDailyUserInsights: getDailyUserInsights
}