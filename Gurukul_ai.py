import streamlit as st
from brain import ask_ai

st.title("Gurukul AI - A 24/7 AI Study Companion")

st.header("Chat with Gurukul AI")
st.write("Your Personalized AI Guru")

st.space("small")

query = st.chat_input("ask anything")

if query:
    with st.spinner('Analyzing...'):
       st.write("You: ", query)
       st.space("small")
       result =  ask_ai(query)
       st.write("Gurukul AI: ", result)


