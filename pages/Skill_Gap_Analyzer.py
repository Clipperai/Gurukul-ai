import streamlit as st
import time as t
from PyPDF2 import PdfReader

from brain import ask_ai

def extract_text(file):
    if file.type == 'application/pdf':
        pdf = PdfReader(file)
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''
        return text
        
    return ""

st.title(" AI Skill Gap Analyzer")

goal = st.selectbox("Select Goal", ['-Select-', 'Frontend Dev', 'Backend Dev', 'FullStack Dev', 'Data Analyst', 'AIML Dev', 'Ethical Hacker'])



resume= st.file_uploader("Upload resume to auto-detect your skills", type=['pdf'])


if st.button("Submit") and (resume) and goal != '-Select-':
    with st.spinner("Analyzing your skills and gaps..."):
        t.sleep(1)
    
        resume_text = extract_text(resume)

        if resume_text.strip() == "":
            st.error("Could not read file!")
        else:
            prompt = f"""
Build a Skill Gap Analyzer for: {goal}

Auto detect skills from user's resume =  {resume}

🎯 Output Rules:
Use arrow flow (→)
Apply Pareto Principle:
Highlight top 20% missing skills → biggest impact
Keep it analysis-only (no roadmap, no resume)

🧠 Analysis Flow:
Step 1 → List required skills (role-based)
Step 2 → Capture user's current skills (from resume)
Step 3 → Compare → find gaps
Step 4 → Rank gaps (high → low priority)

📊 Output Structure:
Current Skills → Required Skills → Gap
Show:
Missing Skills
Weak Skills (low proficiency)
Strong Skills
Add Gap Score / Priority Tag

🚫 Restrictions:
❌ Do NOT generate roadmap
❌ Do NOT analyze resumes/files
❌ Do NOT suggest resources/projects

🔗 Redirection:
Show message:
“→ For improvement plan, go to Pareto Principle based Roadmap Generator”
Add sidebar navigation hint/button

⚙️ Constraints:
Focus on job-relevant skills only
Keep output clean, structured, actionable
No fluff, only insights

🔥 Output Format:
Skill Analysis → Gap → Priority (arrow flow)
Clear CTA → Go to Roadmap Generator (Sidebar)
"""
        
        result = ask_ai(prompt)

        st.subheader("Analysis Result")
        st.write(result)

else:
    st.toast("Goal is not defined or resume is not uploaded")






