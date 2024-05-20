import streamlit as st
import openai
from langchain_openai import ChatOpenAI

# Set your OpenAI API key here
#openai.api_key = "your_openai_api_key"
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Define local slang equivalents (add more as needed)
slang_equivalents = {
    'hello': 'yo',
    'goodbye': 'later gator',
    'thank you': 'cheers',
    'please': 'pretty please',
    'sorry': 'my bad',
    'yes': 'yep',
    'no': 'nah',
}

# Function to convert text to local slang
def convert_to_local_slang(text, target_language):
    #response = openai.Completion.create(
    #    engine="text-davinci-003",
    #    prompt=text,
    #    temperature=0.5,
    #    max_tokens=100,
    #    stop=["\n"]
    #)
    llm = ChatOpenAI(api_key=openaikey, model_name="gpt-3.5-turbo", temperature = 0.5)
    response = llm.invoke("Give the local slang of {text} in {target_language}")
    translated_text = response.choices[0].text.strip()
    for word, slang in slang_equivalents.items():
        translated_text = translated_text.replace(word, slang)
    return translated_text

# Streamlit App
st.title('English to Local Slang Converter')

# User input
text_to_translate = st.text_area('Enter English text:', '')
target_language = st.selectbox('Select target language:', ['es', 'fr', 'de'])  # Spanish, French, German

# Convert text to local slang
if st.button('Convert'):
    if text_to_translate:
        translated_text = convert_to_local_slang(text_to_translate, target_language)
        st.write('Translated text with local slang:', translated_text)
    else:
        st.write('Please enter English text to translate.')
