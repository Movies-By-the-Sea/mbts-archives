import requests
import json
import os

from dotenv import load_dotenv
load_dotenv('../.env')



def getCreds():
    return {
        'access_token' : os.getenv('FB_ACCESS_TOKEN'),
        'client_id'    : os.getenv('FB_CLIENT_ID'),
        'client_secret': os.getenv('FB_CLIENT_SECRET'),
        'graph_domain' : 'https://graph.facebook.com/',
        'graph_version': 'v11.0',
        'endpoint_base': 'https://graph.facebook.com/v11.0/',
        'debug'        : 'no'
    }



def displayAPICallData(response):
    print('\nURL : ')
    print(response['url'])
    print('\nEndpoint_params : ')
    print(response['endpoint_params'])
    print('\nResponse : ')
    print(response['json_data'])



def makeAPICall(url, endpointParams, debug):
    data = requests.get(url, endpointParams)
    response = {
        'url'            : url,
        'endpoint_params': json.dumps(endpointParams, indent = 4),
        'json_data'      : json.loads(data.content)
    }

    if debug == 'yes' :
        displayAPICallData(response)
    return response