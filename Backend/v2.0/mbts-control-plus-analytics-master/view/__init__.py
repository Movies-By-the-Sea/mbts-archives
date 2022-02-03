import streamlit as st

from controller.review_controller import Review_Controller

st.set_page_config(layout='wide', initial_sidebar_state="expanded")






class Page():


#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def mainHeader():
        st.title('MBtS Admin and Analytics Panel')
        st.markdown('Manage and view insights into MBtS platform')


#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def siteFunctions(uid):
        site_functionalities = ['None', 'Manage reviews', 'Edit a review', 'Write a review']
        user_selection       = st.sidebar.selectbox('Choose site functionality', site_functionalities)

        if user_selection == site_functionalities[1]:

            Review_Controller.highlights(uid)
            Review_Controller.display(uid)
            col1, col2 = st.beta_columns(2)
            Review_Controller.updateIG(uid, col1)
            Review_Controller.deleteReview(uid, col2)

        elif user_selection == site_functionalities[2]:

            st.header('Edit reviews')
            st.markdown('Select a review with their ID from their respective table to edit them')
            response, status = Review_Controller.getReviewByID(uid)
            if status: st.json(response)

        elif user_selection == site_functionalities[3]:

            Review_Controller.uploadReview(uid)
