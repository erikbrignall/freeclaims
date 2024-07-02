import pandas as pd
import time
import json
import streamlit as st

st.set_page_config(page_title='Streamlit chat interface - DEMO')
st.title('Streamlit chat demo - Claims data - DEMO')
st.write('The following is a demo of using streamlit as an interface for chat apps. ')

#openai.api_key = st.secrets["OpenAIapikey"]

# Input Query
with st.form(key='my_form_to_submit'):
    st.write('Please paste the free claims text to generate a structured breakdown.')
    query_text = st.text_input('Enter Free text data')
    submit_button = st.form_submit_button(label='Submit')


## The below function loops through the JSON structure and returns any value matching the key
def extract_values(obj, key):
        """Pull all values of specified key from nested JSON."""
        arr = []

        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        results = extract(obj, arr, key)
        return results


    
if submit_button:    
#if query_text is not None:   
        #print("we have a query now")
        # FETCH RESPONSE
        st.write("Here is the structured data from the free text:")

        url = "https://europe-west2-alt24-developments.cloudfunctions.net/claims-structure"
        
        apikey = st.secrets["apikey"]
        request_data = {"input": query_text, "apikey": apikey}

        start_time = time.time()
        response = requests.post(url, json=request_data)
        end_time = time.time()
        response_time = end_time - start_time
        st.write('Response Time:')
        st.write()
        
        LLMresponse = response
        st.write("Here is the JSON response:")

        st.write(response.json())
        #print(response.status_code)
