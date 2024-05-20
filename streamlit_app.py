import streamlit as st
import openai
from langchain_openai import ChatOpenAI

# Set your OpenAI API key here
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Function to convert text to local slang
def convert_to_local_slang(text, target_language):
    llm = ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature = 0.5)
    prompt=f"{text} in {target_language}"
    response = llm.stream(prompt)
    return (response)

# Streamlit App
st.title('English to Local Slang Converter')

# User input
text_to_translate = st.text_area('Enter English text:', '')
target_language = st.selectbox('Select target language:', ['Texan','British','Australian','California','Canadian','New York', 'Southern', 'Midwest'])  

# Convert text to local slang
if st.button('Convert'):
    if text_to_translate:
        translated_text = convert_to_local_slang(text_to_translate, target_language)
        st.write('Translated text with local slang:', translated_text)
    else:
        st.write('Please enter English text to translate.')
