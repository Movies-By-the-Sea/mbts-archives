import streamlit as st
import pandas as pd

from modules import newLine, getMovieInfo
from API.storage import uploadToFirebase, deleteFromFirebase




class Format(object):



    #==================================================================
    # METHOD WHICH RETURNS DATA IN A FORMAT THAT CAN BE SHOWN IN A TABLE

    @staticmethod
    def tableFormat(res):

        data   = res[0]['response']
        keys   = [item for item in data]
        result = [data[item] for item in data]

        for item, key in zip(result, keys):
            item['id']        = key
            item['instagram'] = '✅' if item['instagram'] else '➖'
            item['genre'] = item['genre'][0] + ', ' + item['genre'][1]
            try:
                item['amazon']  = '✔️' if item['amazon'] else '✖️'
                item['netflix'] = '✔️' if item['netflix'] else '✖️'
            except:
                pass

        ans = pd.DataFrame(result)
        ans = ans.iloc[::-1]
        try:
            ans = ans[['instagram', 'id', 'name', 'review', 'director', 'actor', 'year', 'genre', 'acting', 'story', 'execution', 'profundity', 'overall', 'amazon', 'netflix', 'poster_link', 'poster_name', 'trailer']]
        except:
            ans = ans[['instagram', 'id', 'name', 'director', 'description', 'duration', 'genre','link', 'poster_link', 'poster_name']]

        return ans
    #=======================================================================





    #=======================================================================
    # METHOD TO COLLECT THE DATA WHEN UPDATING A REVIEW 

    @staticmethod
    def editForm(data):

        with st.form(key='update_form'):

            genres     = ['Romance','Fantasy','Drama','Lighthearted','Thriller','Meta','Dark','Horror','Inspirational','Animated','International','True Story','Sci-Fi', 'Comedy']
            col1, col2, col3 = st.beta_columns(3)

            col1.image(data['poster_link'],           caption=data['poster_name'])
            name     = col2.text_input('Movie name',    value=data['name'])
            director = col2.text_input('Director name', value=data['director'])
            genre    = col2.multiselect('Genre', genres, data['genre'])

            if data['table'] == 'movie-reviews':

                actor   = col2.text_input('Lead Actor/Actress', value=data['actor'])
                review  = col2.text_area('Review',              value=data['review'], height=250)
                trailer = col3.text_input('Trailer',            value=data['trailer'])
                year    = col3.number_input('Year',             value=int(data['year']))
                overall = col3.slider('Overall Rating',0.0, 5.0, data['overall'])
                newLine(2, col3)
                amazon  = col3.checkbox('Available on Amazon Prime',  value=data['amazon'])
                netflix = col3.checkbox('Available on Netflix',       value=data['netflix'])
                movie_input_list = {
                    'actor'     : actor,
                    'review'    : review,
                    'trailer'   : trailer,
                    'year'      : year,
                    'overall'   : overall,
                    'amazon'    : amazon,
                    'netflix'   : netflix,
                    'acting'    : data['acting'],
                    'story'     : data['story'],
                    'execution' : data['execution'],
                    'profundity': data['profundity'],

                }

            else:

                description = col2.text_area('Description',            value=data['description'], height=130)
                duration    = col3.number_input('Duration in minutes', value=data['duration'])
                link        = col3.text_input('Link',                  value=data['link'])
                short_film_input_list = {
                    'description': description,
                    'duration'   : duration,
                    'link'       : link
                }

            poster = col3.file_uploader('Upload new poster. Make sure the name is not the same as earlier.')
            parent_input_list = {
                'name'       : name,
                'director'   : director,
                'genre'      : genre,
                'id'         : data['id'],
                'instagram'  : data['instagram']
            }

            if poster != None:
                deleteFromFirebase(data['poster_name'])
                link = uploadToFirebase(poster)
                parent_input_list['poster_name'] = poster.name
                parent_input_list['poster_link'] = link
            else:
                parent_input_list['poster_name'] = data['poster_name']
                parent_input_list['poster_link'] = data['poster_link']

            get_update_data = col3.form_submit_button('Confirm update data')

        if get_update_data:
            if data['table'] == 'movie-reviews':
                updated_data = {**parent_input_list, **movie_input_list}
            else:
                updated_data = {**parent_input_list, **short_film_input_list}

            updated_data['table'] = data['table']
            updated_data          = dict( sorted(updated_data.items(), key=lambda x : x[0].lower()))
            return updated_data

    #===========================================================================





    #============================================================================
    # METHOD TO COLLECT DATA WHEN WRITING REVIEW

    @staticmethod
    def writeReviewFormat(table):

        newLine(1, st)
        with st.form(key='write_review_form'):

            genres = ['Romance','Fantasy','Drama','Lighthearted','Thriller','Meta','Dark','Horror','Inspirational','Animated','International','True Story','Sci-Fi', 'Comedy']
            col1, col2, col3 = st.beta_columns([1,2,1])

            name       = col1.text_input('Name')
            director   = col1.text_input('Director')
            genre      = col1.multiselect('Genre', genres)

            result = {
                "name"      : name,
                "director"  : director,
                "genre"     : genre,
                "instagram" : False
            }

            if table == 'movie-reviews':

                poster     = col1.file_uploader('Upload poster image')
                review     = col2.text_area('Review', height=400)

                acting     = col3.slider('Acting rating', 0.0, 5.0, 2.5)
                story      = col3.slider('Story rating', 0.0, 5.0, 2.5)
                execution  = col3.slider('Execution rating', 0.0, 5.0, 2.5)
                profundity = col3.slider('Profundity rating', 0.0, 5.0, 2.5)
                netflix    = col3.checkbox('Available on Netflix')
                prime      = col3.checkbox('Available on Amazon Prime')

                if name != '' :
                    
                    extra = getMovieInfo(name)

                    result['review']     = review
                    result['year']       = extra['year']
                    # result['length']     = extra['length']
                    result['actor']      = extra['cast']
                    result['netflix']    = netflix
                    result['amazon']     = prime
                    result['acting']     = acting
                    result['story']      = story
                    result['execution']  = execution
                    result['profundity'] = profundity
                    result['overall']    = sum([acting, story, execution, profundity]) / 4
                    result['trailer']    = extra['trailer']
                    


            elif table == 'short-film-reviews':

                description = col2.text_area('Give short description', height=250)
                link        = col3.text_input('Streaming Link')
                duration    = col3.number_input('Run-time in minutes')
                poster  = col3.file_uploader('Upload poster image')

                result['link']        = link
                result['description'] = description
                result['duration']    = duration

            if poster is not None:
                link = uploadToFirebase(poster)
                result['poster_name'] = poster.name
                result['poster_link'] = link

            submit_review = st.form_submit_button('Confirm Upload Review')

        if submit_review:
            return result

    #============================================================================