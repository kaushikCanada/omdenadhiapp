import streamlit as st
from transformers import pipeline


def get_option(option):
    if option == "Text Summarisation":
        sentence = st.text_area('Enter your text here...')
        if sentence:
            summarization = pipeline("summarization")
            summary_text = summarization(sentence)[0]['summary_text']
            st.write(summary_text)

option = st.sidebar.selectbox("Select option",  ("Text Summarisation","Other"))

get_option(option)
