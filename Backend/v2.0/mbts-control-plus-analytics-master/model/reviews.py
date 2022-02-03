import requests
import streamlit as st
import dotenv
import os

from controller import makeAPICall
from view.frame import Frame

dotenv.load_dotenv(dotenv.find_dotenv())




class Reviews():


#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def getHighlights(table, uid):
        data = makeAPICall('GET', '/reviews/general',{'table':table, 'uid':uid})
        try:
            return data['remark'], data['response'], True
        except:
            return data['error']['message'], [], False


#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def getAll(table,uid):
        data = makeAPICall('GET','/reviews',{'table':table, 'uid':uid})
        try:
            resp = Frame.tableFrame(data['response'], table)
            return data['remark'], data['size'], resp, True
        except:
            return data['error']['message'], 0, [], False



#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def updateIG(table, id, val, uid):
        data = makeAPICall('PATCH','/reviews/updateIG',{
            'table'    : table,
            'id'       : id,
            'instagram': val,
            'uid'      : uid
        })
        try:
            return data['remark'], data, True
        except:
            return data['error']['message'], [], False


#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def delete(table, id, uid):
        resp = makeAPICall('DELETE','/reviews/delete',{
            'table': table,
            'id'   : id,
            'uid'  : uid
        })
        try:
            return resp['remark'], resp, True
        except:
            return resp['error']['message'], [], False


#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def getReview(table, id, uid):
        data = makeAPICall('GET', '/reviews/get',{
            'table': table,
            'id'   : id,
            'uid'  : uid
        })
        try:
            return data['remark'], data, True
        except:
            return data['error']['message'], [], False


#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def uploadReview(table, data, uid):
        resp = makeAPICall('POST','/reviews/upload', {
            'author'     : os.getenv('EMAIL'),
            'table'      : table,
            'update_data': data,
            'uid'        : uid
        })
        try:
            return resp['remark'], resp, True
        except:
            return resp['error']['message'], [], False