import pandas as pd
import time
import json
import streamlit as st
import requests

st.set_page_config(page_title='Streamlit chat interface - DEMO')
st.title('Streamlit LLM interface demo')
st.header('Claims data - DEMO')
st.write('The following is a demo of using streamlit as an interface for chat apps. ')

#openai.api_key = st.secrets["OpenAIapikey"]

# Input Query
with st.form(key='my_form_to_submit'):
    st.write('Please paste the free claims text to generate a structured breakdown.')
    query_text = st.text_area('Enter Free text data')
    submit_button = st.form_submit_button(label='Submit')

    
if submit_button:    

        st.write("Here is the structured data from the free text:")

        url = "https://europe-west2-alt24-developments.cloudfunctions.net/claims-structure"
        
        apikey = st.secrets["apikey"]
        request_data = {"input": query_text, "apikey": apikey}

        with st.spinner('Analysing Claims Data...'):
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
st.header('Free claims examples')
st.subheader('Account 1: Minor Prang')
st.write('While driving on High Street, I was stopped at a red light. The car behind me, a blue Ford Fiesta, failed to stop in time and bumped into the rear of my vehicle. The impact was minor, resulting in a small dent on my rear bumper. Both drivers exchanged insurance details, and no injuries were reported.')
st.subheader('Account 2: Multi-Vehicle Collision')
st.write('At approximately 8:30 AM, I was traveling eastbound on the M4 when traffic suddenly slowed down due to an accident ahead. I managed to stop in time, but the car behind me, a white BMW, was unable to stop and collided with my vehicle, pushing me into the car in front, a red Toyota. The impact caused significant damage to the front and rear of my car. Emergency services were called, and I was treated for minor whiplash at the scene. All drivers exchanged insurance details, and the police provided a report number.')
st.subheader('Account 3: Pedestrian Involved Accident')
st.write('It was raining lightly and I was driving westbound on Bath Road at around 5:00 PM, a pedestrian suddenly stepped onto the road from between parked cars. Despite braking immediately, I was unable to avoid hitting the pedestrian. The pedestrian sustained a broken leg and was taken to the hospital by ambulance. I remained at the scene and provided a statement to the police. My car’s front bumper and windshield were damaged. The police have recorded the incident, and I have provided my insurance details to the pedestrian.')
