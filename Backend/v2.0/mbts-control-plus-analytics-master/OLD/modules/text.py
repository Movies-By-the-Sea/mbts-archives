import streamlit as st

from API import Analytics
from API.reviews import Reviews

from Instagram.format import IGLayout







#======================================================================
# CLASS TO DISPLAY THE TEXT AND VARIOUS FUNCTIONS WITHIN THE MAIN PAGE

class Page(object):

    state = False





    # DISPLAYING THE MAIN TITLE
    @staticmethod
    def title():
        st.title('MBtS Control and Analytics Panel')
        st.markdown('Manage reviews, blog posts and monitor analytics')





    # LOGIN METHOD CONNECTED TO FIREBASE
    @staticmethod
    def login(auth):
        with st.beta_expander('Sign in and Logout panel'):
            with st.form('login_panel'):
            
                email        = st.text_input('Enter email')
                password     = st.text_input('Enter password')
                submit_login = st.form_submit_button('Login to the dashboard')

            if submit_login:
                login = auth.sign_in_with_email_and_password(email, password)
                if(login):
                    Page.state = True
                    st.success('Signed in!  Logging you in')

            if st.button('Log out from current session'):
                Page.state = False
    




    # DISPLAY HIGHLIGHTS FROM THE DATABSE
    @staticmethod
    def highlights():

        res = Analytics.getHighlights()
        st.sidebar.title('Highlights')
        st.sidebar.markdown('1. **' + str(res[0]['response']['allReviews']) + '** movie reviews written. **' + str(res[0]['response']['allInstagram']) + '** uploaded on Instagram')
        st.sidebar.markdown('2. **' + str(res[1]['response']['allReviews']) + '** short-film reviews written. **' + str(res[1]['response']['allInstagram']) + '** uploaded on Instagram')





    # METHOD TO INVOKE VARIOUS CRUD OPERATIONS ON DATABASE
    @staticmethod
    def siteFunctions():

        st.sidebar.title('Site Functions')
        st.sidebar.markdown('Manage reviews for movies and shortfilms')
        
        site_functionalities = ['None', 'Display all reviews', 'Edit a review', 'Write movie review']
        user_selection       = st.sidebar.selectbox('Choose site functionality', site_functionalities)



        if user_selection == site_functionalities[1]:


            st.header('Manage Reviews')
            st.markdown('Edit, updte and delete reviews in the database. Refresh browser to reflect the changes.')
            Reviews.display()

            col1, col2 = st.beta_columns(2)
            Reviews.editIG(col1)
            Reviews.delete(col2)


        elif user_selection == site_functionalities[2]:


            st.header('Edit Review')
            st.markdown('Copy and paste the ID of the review to perform any changes on the review')
            Reviews.edit()


        elif user_selection == site_functionalities[3]:


            st.header('Write a review')
            st.markdown('Fill in the required details. The external helper APIs will fill in the rest automatically.')
            Reviews.write()





    # DISPLAYING ANALYTICS FROM INSTAGRAM
    @staticmethod
    def instagram():

        st.sidebar.title('Instagram')
        st.sidebar.markdown('Gain insights into how posts are performing on Instagram')

        if st.sidebar.checkbox('Open IG analytics panel') :

            st.header('Instagram Insights')
            st.markdown('Analyze how your posts are performing on Instagram using the Facebook Graph API.')

            IGLayout.apiTokenDisplay()