import streamlit as st
import time as t
from brain import ask_ai

st.title("Pareto Principle based Roadmap Generator")

goal = st.text_input("Enter your goal")

level = st.selectbox("Choose Current Level", ['Beginner', 'Intermediate', 'Advanced'])

duration = st.number_input("Enter duration(in months): ")


if st.button("Submit") and goal:
    with st.spinner("Generating your Roadmap..."):
        t.sleep(1)

        prompt = f"""
Generate a Pareto principle based roadmap for the {goal} goal.
current level = {level}
Duration = {duration} months

Output:-

give roadmap via pareto principle (20%- Theory and 80%- projects)
Give day wise roadmap with project name & details
use Arrows and make it perfect.
Replaces Notes section with projects

suggest resources with priority basis:
1.  Highlight this  --- pyPRO (youtube channel for python projects have 30days python projects series from hello world n mini calculator (day 1) to a Capistone project(day 30) )  THIS IS MUST/Recommended
2. Chatgpt/Gemini 
3. anything else like notes, books, courses etc.



"""
        
        result = ask_ai(prompt)

        st.subheader("Your Roadmap:")
        st.write(result)

