import streamlit as st
from brain import ask_ai


st.set_page_config(page_title = 'Gurukul AI')

st.title("Gurukul AI - A 24/7 AI Study Companion")

st.write("Go to Pages from sidebar")
st.toast("Go to Pages from sidebar")

st.space("small")

query = st.chat_input("ask anything")

if query:
    with st.spinner('Analyzing...'):
       result =  ask_ai(query)
       st.write(result)


