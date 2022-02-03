import streamlit as st
from model.reviews import Reviews
from view.utilities import newLine
from view.charts import Chart
from view.frame import Frame
from view.utilities import checkIfFilledRequired





class Review_Controller():


#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def highlights(uid):
        st.header('Review Manager')
        st.markdown('Refresh the page to reflect any changes done.')
        remark_1, resp_1, status = Reviews.getHighlights('movie-reviews', uid)
        remark_2, resp_2, status = Reviews.getHighlights('short-film-reviews', uid)
        if status:
            Chart.Reviews(resp_1,'movie-reviews')
            Chart.Reviews(resp_2, 'short-film-reviews')
        else:
            st.error('Movie Database Error : ' + remark_1)
            st.error('Short Film Database Error : ' + remark_2)



#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def display(uid):      

        with st.beta_expander('Movie Reviews'):
            remark, size, response, status = Reviews.getAll('movie-reviews', uid)
            if status:
                st.markdown('__{}__ movie reviews currently in database'.format(size))
                st.dataframe(response)
                st.success(remark)
            else:
                st.error(remark)

        with st.beta_expander('Short Film Reviews'):
            remark, size, response, status = Reviews.getAll('short-film-reviews', uid)
            if status:
                st.markdown('__{}__ short-film reviews currently in database'.format(size))
                st.dataframe(response)
                st.success(remark)
            else:
                st.error(remark)



#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def updateIG(uid, col):
        with col.form(key='update_ig'):
            st.subheader('Update Instagram Status')
            st.markdown('Copy and paste the ID of the review that you want its IG status to be updated')

            update_id    = st.text_input('Enter review ID')
            update_val   = st.selectbox('Uploaded on Instagram?', [True, False])
            update_table = st.selectbox('Enter table to be updated',['movie-reviews', 'short-film-reviews'])
            submit_ig    = st.form_submit_button('Confirm instagram update status')

        if submit_ig:
            remark, response, status = Reviews.updateIG(update_table, update_id, update_val, uid)
            if status:
                st.success(remark)
                with st.beta_expander('Examine API response'):
                    st.json(response)
            else:
                st.error(remark)



#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def deleteReview(uid, col):
        with col.form(key='delete_review'):
            st.subheader('Delete a review')
            st.markdown('Copy and paste the ID of the review that you want to delete')

            delete_id    = st.text_input('Enter review ID')
            delete_table = st.selectbox('Enter table to be deleted from',['movie-reviews','short-film-reviews'])
            st.warning('Once deleted, review cannot be recovered')
            submit       = st.form_submit_button('Confirm review deletion')

        if submit:
            remark, response, status = Reviews.delete(delete_table, delete_id, uid)
            if status:
                st.success(remark)
                with st.beta_expander('Examine API response'):
                    st.json(response)
            else:
                st.error(remark)



#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def getReviewByID(uid):
        with st.form(key='get_review_by_id'):
            col1, col2, col3 = st.beta_columns([3,3,1])
            rev_id           = col1.text_input('Enter review ID')
            rev_table        = col2.selectbox('Enter table to which review belongs to',['movie-reviews', 'short-film-reviews'])
            newLine(col3, 2)
            submit           = col3.form_submit_button('Fetch Review')
        if submit:
            remark, response, status = Reviews.getReview(rev_table, rev_id, uid)
            if status:
                st.success(remark)
            else:
                st.error(remark)
            return response, status
        return [], False



#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def uploadReview(uid):

        st.header('Write review')
        st.markdown('Fill in the required details. The external helper APIs will fill in the rest automatically.')
        select_table = st.radio('Select to which table to write a review to', ('movie-reviews', 'short-film-reviews'))
        upload_data  = Frame.writeReviewFormat(select_table)
        if checkIfFilledRequired(upload_data):
            resp, data, status = Reviews.uploadReview(select_table, upload_data, uid)
            if status:
                st.success(resp)
                with st.beta_expander('Examine API response'):
                    st.json(data)
            else:
                st.error(resp)