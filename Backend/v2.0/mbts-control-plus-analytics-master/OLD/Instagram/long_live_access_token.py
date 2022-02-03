from Instagram import getCreds, makeAPICall

def getLongLiveAccessToken(params):

    """ Get long live access token

    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={ypur-access-token}

    Returns:
        object: data from the endpoint

    """

    endpointParams = {
        'grant_type'       : 'fb_exchange_token',
        'client_id'        : params['client_id'],
        'client_secret'    : params['client_secret'],
        'client_id'        : params['client_id'],
        'fb_exchange_token': params['access_token']
    }

    url = params['endpoint_base'] + 'oauth/access_token'

    return makeAPICall(url, endpointParams, params['debug'])



# params = getCreds()
# params['debug'] = 'yes'
# resp = getLongLiveAccessToken(params)


# print('\n ----------- ACCESS TOKEN INFO --------------')
# print('Access token : ')
# print(resp['json_data']['access_token'])