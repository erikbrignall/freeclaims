import pandas as pd
import time
import json
import streamlit as st
import requests

st.set_page_config(page_title='Streamlit chat interface - DEMO')
st.title('Streamlit chat demo - Claims data - DEMO')
st.write('The following is a demo of using streamlit as an interface for chat apps. ')

#openai.api_key = st.secrets["OpenAIapikey"]

# Input Query
with st.form(key='my_form_to_submit'):
    st.write('Please paste the free claims text to generate a structured breakdown.')
    query_text = st.text_input('Enter Free text data')
    submit_button = st.form_submit_button(label='Submit')

    
if submit_button:    

        st.write("Here is the structured data from the free text:")

        url = "https://europe-west2-alt24-developments.cloudfunctions.net/claims-structure"
        
        apikey = st.secrets["apikey"]
        request_data = {"input": query_text, "apikey": apikey}

        with st.spinner('Cogs a whirrin...'):
            start_time = time.time()
            response = requests.post(url, json=request_data)
            end_time = time.time()
            response_time = end_time - start_time
            
            LLMresponse = response
            st.write("Here is the JSON response:")
    
            st.write(response.json())
            st.write('Response Time:')
            st.write(response_time)
            #print(response.status_code)
