import streamlit as st
from transformers import pipeline

st.title("Omdena DHI Dzongkha-English Translation Application")

def get_option(option):
    if option == "Dzongkha to English":
        sentence = st.text_area('Enter your text here...')
        if sentence:
            summarization = pipeline("summarization")
            summary_text = summarization(sentence)[0]['summary_text']
            st.write(summary_text)

option = st.sidebar.selectbox("Select option",  ("Dzongkha to English","English to Dzongkha"))

get_option(option)
