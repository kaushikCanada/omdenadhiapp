import streamlit as st
from transformers import pipeline

st.set_page_config(page_title='Omdena DHI Dzongkha-English Translation Application', page_icon=':shark:', layout="centered", initial_sidebar_state="auto", menu_items=None)


def get_option(option):
    if option == "Dzongkha to English":
        st.title("Please enter text in Dzongkha")
        sentence = st.text_area('Enter your text here...')
        if sentence:
            summarization = pipeline("summarization")
            summary_text = summarization(sentence)[0]['summary_text']
            st.write(summary_text)
    if option == "English to Dzongkha":
        st.title("Please enter text in English")
        sentence = st.text_area('Enter your text here...')
        if sentence:
            summarization = pipeline("summarization")
            summary_text = summarization(sentence)[0]['summary_text']
            st.write(summary_text) 

 

option = st.sidebar.selectbox("Select option",  ("Dzongkha to English","English to Dzongkha"))

get_option(option)
