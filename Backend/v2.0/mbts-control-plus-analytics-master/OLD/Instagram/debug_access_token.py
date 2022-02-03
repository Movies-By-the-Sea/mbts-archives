from Instagram import getCreds, makeAPICall
import datetime




def debugAccessToken(params):

    """ Get info on access token

    API Endpoint:
        https://graph.facebook.com/
        debug_token?input_token={input-token}&access_token={valid-access-token}

    Returns:
        object: data from the endpoint

    """

    endpointParams = {
        'input_token' : params['access_token'],
        'access_token': params['access_token']
    }

    url = params['graph_domain'] + '/debug_token'

    return makeAPICall(url, endpointParams, params['debug'])



# params = getCreds()
# params['debug'] = 'yes'
# resp = debugAccessToken(params)
# print('\nExperies at : ', datetime.datetime.fromtimestamp(resp['json_data']['data']['data_access_expires_at']))