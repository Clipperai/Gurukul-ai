import streamlit as st
from brain import ask_ai


st.set_page_config(page_title = 'Gurukul AI')

st.title("Gurukul AI - A 24/7 AI Study Companion")

st.write("Go to Pages from sidebar")

query = st.chat_input("Ask")

ask = st.button('Ask ai')

if query and ask:
    with st.spinner('Analyzing...'):
       result =  ask_ai(query)
       st.write(result)


