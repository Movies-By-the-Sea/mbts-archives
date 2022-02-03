import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from view.utilities import newLine, lineBreak





class Chart():


#=========================================================================================================
#=========================================================================================================

    @staticmethod
    def Reviews(data, table):

        total     = data['Total']
        instagram = data['Instagram']['size']
        genres    = [{item:data['Genre'][item]['size']} for item in data['Genre']]

        if table=='movie-reviews':

            must_watch = data['Must_Watch']['size']
            foreign    = data['Foreign']['size']
            available  = [data['Netflix']['size'], data['Prime']['size'], total - (data['Netflix']['size'] + data['Prime']['size'])]

            names = 'Netflix ' + str(available[0]) + ' %', 'Amazon Prime ' + str(available[1]) + ' %', 'Others ' + str(available[2]) + ' %'
            fig   = plt.figure()
            fig.patch.set_facecolor('#141414')
            plt.rcParams['text.color'] = '#b76e79'
            plt.rcParams['font.size']  = 14
            my_circle = plt.Circle( (0,0), 0.7, color='#141414')
            plt.pie(available, labels=names)
            p = plt.gcf()
            p.gca().add_artist(my_circle)


            lineBreak(st)
            st.subheader('Movie Reviews')
            col1, col2, col3 = st.beta_columns([1,1,2])
            newLine(col1,2)
            col1.markdown('__{}__ : total number of items'.format(total))
            col1.markdown('__{} %__ : of reviews uploaded on Instagram'.format(int(instagram*100/total)))
            col1.markdown('__{} %__ : of must watch films'.format(int(must_watch*100/total)))
            col1.markdown('__{} %__ : of foreign films'.format(int(foreign*100/total)))
            col2.pyplot(p)
            col3.bar_chart(pd.DataFrame(genres))

        elif table == 'short-film-reviews':

            lineBreak(st)
            st.subheader('Short Film Reviews')
            col1, col2 = st.beta_columns(2)
            newLine(col1,2)
            col1.markdown('__{}__ : total number of items'.format(total))
            col1.markdown('__{} %__ : of reviews uploaded on instagram'.format(int(instagram*100/total)))
            col2.bar_chart(pd.DataFrame(genres))
            st.markdown('---')
