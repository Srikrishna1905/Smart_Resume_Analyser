import streamlit as st
import PyPDF2
import io
import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(page_title="Smart Resume Analyzer", page_icon="📄", layout="wide")

# Sidebar styling and information
with st.sidebar:
    st.header("About the Project")
    st.markdown("""
    **Smart Resume Analyzer** is an AI-Powered Feedback System designed for job seekers.
    
    It analyzes your resume and provides structured, professional feedback on:
    - Content clarity and impact
    - Presentation of skills
    - Measurable achievements
    - Job-role specific customization
    - ATS compatibility
    """)
    st.markdown("---")
    st.markdown("### How to use:")
    st.markdown("1. Upload your complete resume in PDF or TXT format.")
    st.markdown("2. (Optional) Enter the specific job title you are applying for to get tailored feedback.")
    st.markdown("3. Click **Analyze Resume** and wait for the AI report.")

st.title("Smart Resume Analyzer 📄")
st.markdown("### Land your dream job with an ATS-friendly, impactful resume.")
st.write("Upload your resume below to receive instant, intelligent, and constructive feedback from our AI Expert Reviewer.")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("API key not found. Please ensure you have created a `.env` file with `GEMINI_API_KEY=your_key`.")
    st.stop()

# Configure new Gemini AI Client
client = genai.Client(api_key=GEMINI_API_KEY)

# Input section
col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"], help="Limit 10MB")

with col2:
    job_role = st.text_input("Target Job Role (Optional)", placeholder="e.g. Senior Software Engineer", help="Providing a job role helps the AI tailor its feedback.")

analyze_button = st.button("Analyze Resume", type="primary", use_container_width=True)

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze_button:
    if not uploaded_file:
        st.warning("Please upload a resume to proceed.")
    else:
        with st.spinner("Our AI is carefully reviewing your resume... This may take a few seconds."):
            try:
                file_content = extract_text_from_file(uploaded_file)

                if not file_content.strip():
                    st.error("The uploaded file appears to be empty or unreadable.")
                    st.stop()

                prompt = f"""
You are an Expert Resume Reviewer and Advanced Applicant Tracking System (ATS). 
Your task is to analyze the following resume in detail and provide constructive, professional, and structured feedback.

Target Job Role (if any): {job_role if job_role else 'General / Not specified'}

Please evaluate the resume based on the following criteria:
1. ATS Compatibility & Formatting
2. Content Clarity and Impact (use of action-oriented language)
3. Measurable Achievements (quantifiable metrics)
4. Skills Presentation (alignment with the target role)
5. Experience Descriptions

Provide the analysis in the following structured format using Markdown:

### 📊 Executive Summary
[A brief 2-3 sentence overview of the resume's overall quality and immediate impression.]

### 🤖 ATS Compatibility
[Assessment of how well this resume would pass through an ATS. Identify any formatting or keyword issues.]

### ⭐ Key Strengths
[Bullet points highlighting what the candidate has done well (e.g., strong action verbs, clear formatting).]

### 📉 Areas for Improvement
[Specific, constructive points on what is lacking. E.g., missing metrics, vague bullet points, irrelevant skills.]

### 🛠️ Actionable Recommendations
[Step-by-step suggestions on how to improve the resume for the target job role. Provide specific examples of how to rewrite bullet points to include measurable achievements.]

---
**Resume Content:**
{file_content}
"""

                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )

                st.success("Analysis Complete!")
                st.markdown("---")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"An error occurred during analysis: {str(e)}")
