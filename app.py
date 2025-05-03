import streamlit as st
import requests

st.title('Piadas do Chuck Norris')

api_url = 'https://api.api-ninjas.com/v1/chucknorris'
response = requests.get(
    api_url, 
    headers={
        'X-Api-Key': st.secrets['API_KEY']
    }
)
