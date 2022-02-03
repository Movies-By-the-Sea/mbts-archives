import streamlit as st
import datetime

from modules import newLine
from Instagram.debug_access_token import debugAccessToken
from Instagram import getCreds

class IGLayout(object):

    @staticmethod
    def apiTokenDisplay():

        newLine(1, st)
        with st.beta_expander('Examine Graph API token'):

            creds = getCreds()
            response = debugAccessToken(creds)

            st.subheader('Manage Graph API tokens from here')
            col1, col2, col3 = st.beta_columns([3,1,1])

            col1.markdown('If past the expiry, go over to [developers.facebook.com/tools/explorer](https://developers.facebook.com/tools/explorer/) to generate new Access Token and paste it in the field below. Refresh the app to reflect changes.')
            col1.text_input('New graph API token')

            col2.markdown('__App Name__ : ')
            col2.markdown('__Data Access expires at__ : ')
            col2.markdown('__Token expires at__ :')
            col2.markdown('__Token issued on__ : ')

            
            col3.write(response['json_data']['data']['application'])            
            col3.write(datetime.datetime.fromtimestamp(response['json_data']['data']['data_access_expires_at']))
            col3.write(datetime.datetime.fromtimestamp(response['json_data']['data']['expires_at']))
            col3.write(datetime.datetime.fromtimestamp(response['json_data']['data']['issued_at']))

            # col1.markdown('__Scopes issued__ : ')
            # col2.write(response['json_data']['data']['scopes'])
            # st.write(response)
