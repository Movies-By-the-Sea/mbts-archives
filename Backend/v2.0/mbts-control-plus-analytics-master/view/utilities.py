import streamlit as st




#=========================================================================================================
#=========================================================================================================

def newLine(obj, numLines):
    for _ in range(numLines):
        obj.markdown('')


#=========================================================================================================
#=========================================================================================================

def lineBreak(obj):
    return obj.markdown('---')


#=========================================================================================================
#=========================================================================================================

def checkIfFilledRequired(data):
    if not data : return False
    reqFlag = False
    for key in data:
        if key == 'poster_name' and data[key] is None:
            reqFlag = True
        if key == 'duration' and data[key] == 0.0:
            reqFlag = True
        if key == 'genre' and len(data[key]) < 2:
            reqFlag = True        
        if data[key] == '' :
            reqFlag = True
        if reqFlag:
            st.error('Please fill in the key : ' + key)
            return False    
    return True