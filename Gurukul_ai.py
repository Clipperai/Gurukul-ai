import streamlit as st
from brain import ask_ai


st.set_page_config(page_title = 'Gurukul AI')

st.title("Gurukul AI - A 24/7 AI Study Companion")

st.header("Chat with Gurukul AI")
st.write("Your Personalized AI Guru")
st.toast("Go to Pages from sidebar")

st.space("small")

st.toast("How can I help you todaay?")
st.toast("Hello, Builder!👋")

query = st.chat_input("ask anything")

if query:
    with st.spinner('Analyzing...'):
       st.write("You: ", query)
       result =  ask_ai(query)
       st.write("Gurukul AI: ", result)


