import time

import streamlit as st

from model import uploadToFirebase
from datetime import datetime
from controller import getMovieInfo
from view.utilities import newLine




class Frame(object):



#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def tableFrame(data, table):
        temp = []
        for item in data:
            if table == 'movie-reviews':
                info = {
                    'Instagram'  : '✅' if item['instagram'] else '➖',
                    "ID"         : item['id'],
                    'Name'       : item['name'],
                    'Author'     : item['author'],
                    'Author_UID' : item['author_uid'],
                    'Director'   : item['director'],
                    'Timestamp'  : datetime.fromtimestamp(item['timestamp']),
                    'Lead'       : item['lead'],
                    "Year"       : item['year'],
                    "Review"     : item['review'],
                    "Genre"      : item['genre'],
                    "Prime"      : '✔️' if item['prime'] else '✖️',
                    "Netflix"    : '✔️' if item['netflix'] else '✖️',
                    "Foreign"    : '✔️' if item['foreign'] else '✖️',
                    "Must Watch" : '✔️' if item['must_watch'] else '✖️',
                    "Story"      : item['story'],
                    "Acting"     : item['acting'],
                    "Execution"  : item['execution'],
                    "Profundity" : item['profundity'],
                    "Overall"    : item['overall'],
                    "Poster"     : item['poster'],
                    "Poster Link": item['poster_link'],
                    "Trailer"    : item['trailer']
                }
            elif table == 'short-film-reviews':
                info = {
                    'Instagram'  : '✅' if item['instagram'] else '➖',
                    "ID"         : item['id'],
                    "Name"       : item['name'],
                    "Author"     : item['author'],
                    "Author ID"  : item['author_uid'], 
                    "Director"   : item['director'],
                    "Timestamp"  : datetime.fromtimestamp(item['timestamp']),
                    "Description": item['description'],
                    "Duration"   : item['duration'],
                    "Genre"      : item['genre'],
                    "Link"       : item['link'],
                    "Poster"     : item['poster_name'],
                    "Poster Link": item['poster_link'],  
                }
            temp.append(info)
        return temp
        

#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def writeReviewFormat(table):

        newLine(st, 1)
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
                "instagram" : False,
                "timestamp" : time.time()
            }

            if table == 'movie-reviews':

                poster     = col1.file_uploader('Upload poster image')
                review     = col2.text_area('Review', height=400)

                cola, colb, colc = st.beta_columns(3)

                acting     = col3.slider('Acting rating', 0.0, 5.0, 2.5)
                story      = col3.slider('Story rating', 0.0, 5.0, 2.5)
                execution  = col3.slider('Execution rating', 0.0, 5.0, 2.5)
                profundity = col3.slider('Profundity rating', 0.0, 5.0, 2.5)
                must_watch = col3.checkbox('Must Watch')

                cola, colb, colc, cold, cole = st.beta_columns([1,1,1,0.75,1])
                netflix    = cola.checkbox('Available on Netflix')
                prime      = colb.checkbox('Available on Amazon Prime')
                mubi       = colc.checkbox('Availabe on Mubi')
                foreign    = cold.checkbox('Foreign Film')

                if name != '' :
                    
                    extra = getMovieInfo(name)

                    result['review']     = review
                    result['year']       = extra['year']
                    # result['length']     = extra['length']
                    result['actor']      = extra['cast']
                    result['netflix']    = netflix
                    result['amazon']     = prime
                    result['mubi']       = mubi
                    result['must_watch'] = must_watch
                    result['foreign']    = foreign
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
