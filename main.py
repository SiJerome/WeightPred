import pickle
import streamlit as st
import numpy as np
import pandas as pd

data_in = pickle.load(open('dataset.pkl', 'rb'))
pickle_in = open('Model_Regression.pkl', 'rb')
classifier = pickle.load(pickle_in)



def main():
    # front end elements of the web page
    html_temp = """ 
       <div style ="background-color:yellow;padding:13px"> 
       <h1 style ="color:black;text-align:center;">FISH WEIGHT PREDICTOR</h1> 
       </div> 
       """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    species = st.selectbox('Species', data_in['class'].unique())

    if species == 'grouper':
        length = st.number_input("Length in CM", min_value=1.0, max_value=238.0)
    elif species == 'skipjack':
        length = st.number_input("Length in CM", min_value=1.0, max_value=238.00)
    else:
        length = st.number_input("Length in CM", min_value=1.0, max_value=238.00)

    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):

        if species == 'grouper':
            species = 0
        elif species == 'skipjack':
            species = 1
        else:
            species = 2

        # length_cm = np.float32(length)
        # query = np.array([species, length])
        # query = query.reshape(1,2)
        result = classifier.predict(pd.DataFrame([[species, length]], columns=['class', 'length_cm']))
        # result = classifier.predict(query)
        # st.success("The predicted weight of this species is " + str(float(np.floor(classifier.predict(query)[0]))))
        st.success("The predicted weight of this species based on length is " + str(float(np.around(result, decimals=2)))+"kg")


if __name__=='__main__':
    main()