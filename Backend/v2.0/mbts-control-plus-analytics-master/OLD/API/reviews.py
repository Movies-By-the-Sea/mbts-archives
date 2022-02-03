import streamlit as st

from API import Database
from modules.format import Format
from modules import newLine, checkIfUpdated, checkIfFilledRequired





#=============================================================================================
# CLASS TO PERFORM CRUD OPERATIONS ON THE REVIEWS TABLE

class Reviews(object):





    # GETTING AND DISPLAYING ALL REVIEWS
    @staticmethod
    def display():

        with st.beta_expander('Movie Reviews'):
            st.caption('Reviews displayed in first-in-last-out method. Meaning Latest review is displayed at the top.')
            result = Database.getAllReviews('movie-reviews')
            st.dataframe(Format.tableFormat(result))

        with st.beta_expander('Short-film reviews'):
            st.caption('Reviews displayed in first-in-last-out method. Meaning Latest review is displayed at the top.')
            result = Database.getAllReviews('short-film-reviews')
            st.dataframe(Format.tableFormat(result)) 


    


    # EDITING INSTAGRAM STATUS
    @staticmethod
    def editIG(st_obj):

        with st_obj:
            with st.form(key='update_ig'):
                st.subheader('Update Instagram Status')
                st.markdown('Copy and paste the ID of the review that you want its IG status to be updated')

                update_id    = st.text_input('Enter review ID')
                update_val   = st.selectbox('Uploaded on Instagram?', [True, False])
                update_table = st.selectbox('Enter table to be updated',['movie-reviews', 'short-film-reviews'])
                submit_ig    = st.form_submit_button('Confirm instagram update status')

            if submit_ig:

                Database.updateIG(update_table, update_id, update_val)





    # DELETING ANY REVIEW
    @staticmethod
    def delete(st_obj):

        with st_obj:
            with st.form(key='delete_review'):

                st.subheader('Delete review from database')
                st.markdown('Copy and paste the ID of the review to be deleted')
                update_id    = st.text_input('Enter review ID', key='delete')
                update_table = st.selectbox('Enter table to be deleted from',['movie-reviews', 'short-film-reviews'])
                st.info('This action is non-reversible. Once deleted, review cannot be recovered.')
                submit_delete = st.form_submit_button('Confirm deletion of selected review')

            if submit_delete:

                Database.deleteReview(update_table, update_id)





    # GETTING A REVIEW
    @staticmethod
    def getReview():

        with st.form(key='get_review'):

            col1, col2, col3  = st.beta_columns([2,2,1])
            update_table      = col1.selectbox('Enter table to be updated', ['movie-reviews', 'short-film-reviews'])
            update_id         = col2.text_input('Enter movie/short-film review ID')
            newLine(2, col3)
            get_review_submit = col3.form_submit_button(label='Get review for update')

        res = Database.getReview(update_table, update_id)
        if len(res) == 1:
            st.error(res['message'])
            return [{}, False]

        if len(res) == 3:
            st.info('Enter a review ID to continue to edit form')
            return [{}, False]
        
        data          = res['response']
        data['table'] = update_table
        data['id']    = update_id
        data = dict( sorted(data.items(), key=lambda x: x[0].lower()) )
        return [data, True]

    


    
    # EDITING A REVIEW
    @staticmethod
    def edit():

        original_data, got_data = Reviews.getReview()
        if got_data:
            
            updated_data                 = Format.editForm(original_data)
            changed_items, change_status = checkIfUpdated(original_data, updated_data)
            if change_status:
                id    = original_data['id']
                table = original_data['table']
                Database.updateReview(id, table, changed_items)
            




    # WRITING A REVIEW
    @staticmethod
    def write():

        select_table = st.radio('Select to which table to write a review to', ('movie-reviews', 'short-film-reviews'))
        upload_data  = Format.writeReviewFormat(select_table)

        if checkIfFilledRequired(upload_data):
            Database.writeReview(select_table, upload_data)