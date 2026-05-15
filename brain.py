from groq import Groq 
import streamlit as st

client = Groq(api_key = st.secrets["GROQ_API_KEY"])


SYSTEM_PROMPT = """
    You are CSV Analyzer
    Give 5 insights + trends + anomalies
    Keep the response under 12 bullet points or under 300 words.
"""     

MODEL="openai/gpt-oss-safeguard-20b"

def ask_ai(prompt):

    full_prompt = f"{SYSTEM_PROMPT}\nUser: {prompt}"
    response = client.chat.completions.create(
            model = MODEL,
            temperature = 0,
            messages = [{"role": "user", "content": prompt}]
        )
    return response.choices[0].message.content

