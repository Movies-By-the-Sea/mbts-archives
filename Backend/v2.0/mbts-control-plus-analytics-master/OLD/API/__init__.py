import streamlit as st
from modules import callREST
from REST.storage import deleteFromFirebase





#==================================================================
# CLASS TO MAKE CALLS TO GET THE GENERAL OVERVIEW

class Analytics(object):

    @staticmethod
    def getHighlights():
        return callREST(reqtype='GET', routes=['/movie-reviews', '/short-film-reviews'])

#==================================================================





#==================================================================
# COMMON CLASS TO PERFORM CRUD OPERATIONS ON BOTH REVIEW TABLES

class Database(object):



    @staticmethod
    def getAllReviews(table):
        try:
            return callREST(reqtype='GET', routes=['/' + table + '/all'])
        except:
            return False




    
    @staticmethod
    def getReview(table, id):
        try:
            return callREST(reqtype='GET', routes=['/' + table + '/' + id])[0]
        except:
            return False




    
    @staticmethod
    def updateReview(id, table, data):
        edit_data = {
            "id"         : id,
            "table"      : table,
            "update_data": data
        }
        response = callREST(reqtype='PUT', jsonVal=edit_data, routes=['/operations/updateReview'])
        st.success(response[0]['message'])
        with st.beta_expander('Examine API response'):
            st.json(response)
        return





    @staticmethod
    def updateIG(table, id, val):
        mismatch_input_check = Database.getReview(table, id)
        if len(mismatch_input_check) == 1:
            st.error(mismatch_input_check['message'])
            return
        data = {
            "id"       : id,
            "table"    : table,
            "instagram": val
        }
        response = callREST(reqtype='PATCH', jsonVal=data, routes=['/operations/updateIG'])
        st.success(response[0]['message'])
        with st.beta_expander('Examine API response'):
            st.json(response)
        return 





    @staticmethod
    def deleteReview(table, id):
        mismatch_input_check = Database.getReview(table, id)
        if len(mismatch_input_check) == 1:
            st.error(mismatch_input_check['message'])
            return

        deleteFromFirebase(mismatch_input_check['response']['poster_name'])

        data = {
            "id"   : id,
            "table": table,
        }
        response = callREST(reqtype='DELETE', jsonVal=data, routes=['/operations/delete'])
        st.success(response[0]['message'])
        with st.beta_expander('Examine API response'):
            st.json(response)
        return 





    @staticmethod
    def writeReview(table, data):
        data['table'] = table
        response = callREST(reqtype='POST', jsonVal=data, routes=['/operations/upload'])
        st.success('Review added successfully to table : ' + table)
        with st.beta_expander('Examine API response'):
            st.write(response)