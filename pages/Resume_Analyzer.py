import streamlit as st
import time as t
from brain import ask_ai
from PyPDF2  import PdfReader 
# from docx 

st.title("Resume Analyzer AI")


def extract_text(file):
    if file.type == 'application/pdf':
        pdf = PdfReader(file)
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ""

        return text
    
    return ""


file = st.file_uploader("Upload your Resume:", type=['pdf', 'docx'])
role = st.selectbox(
    "Select Job Role",
    ['Frontend Dev', 'Backend Dev', 'Full Stack Dev', 'ML Dev', 'Data Analyst', 'AI Engineer', 'Python Dev']
)

if st.button("Submit") and file:
    with st.spinner("Analyzing your Resume"):
        t.sleep(1)

        resume_text = extract_text(file)

        if resume_text.strip() == "":
            st.error("Could not read file!")
        else:
            prompt = f"""
Analyze this resume for a {role} role.

Give:
1. Summary (bullet points)
2. Key Skills
3. Strengths
4. Missing Skills
5. Improvements
6. ATS score out of 100
7. Required ATS score for this role (1-2 bullet points)

Resume:
{resume_text}
"""
        
        result = ask_ai(prompt)

        st.subheader("Analysis Result")
        st.write(result)
