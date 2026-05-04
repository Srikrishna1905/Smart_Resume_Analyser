# Smart Resume Analyzer: An AI-Powered Feedback System for Job Seekers 📄

Many students, fresh graduates, and experienced professionals struggle to write professional, impactful resumes. Common issues include lacking measurable achievements, using weak verbs, failing to tailor the resume for specific roles, and the high cost of manual resume review services.

The **Smart Resume Analyzer** solves this by providing an automated, web-based system that gives instant, intelligent, and constructive feedback on uploaded resumes using Artificial Intelligence.

## 🎯 Objective
- Develop a web-based application to analyze resumes using Google's Gemini AI.
- Provide structured, professional, and ATS-friendly feedback on resume quality.
- Improve content clarity, skills presentation, and experience descriptions.
- Offer tailored, actionable suggestions based on the user’s targeted job role.
- Help students and job seekers create impactful resumes to enhance their chances of securing interviews.

## 🛠️ Proposed Methodology & Tools Built With
- **[Streamlit](https://streamlit.io/):** To develop an interactive and user-friendly web interface.
- **[PyPDF2](https://pypdf2.readthedocs.io/):** To parse and extract text from uploaded PDF resumes.
- **[Google Gemini AI](https://deepmind.google/technologies/gemini/):** To analyze the extracted resume content and generate structured, expert-level feedback.
- **[Prompt Engineering]:** To guide the AI model to output specific ATS-focused insights, strengths, and actionable recommendations.
- **[Python-dotenv]:** To securely manage API keys and configuration settings.

## 🌟 Expected Outcome
- A fully functional, blazing-fast AI-powered resume critique system.
- Real-time, structured, and professional feedback generation.
- Improved resume quality and clarity for users.
- Better alignment of resumes with targeted job roles.
- Enhanced application success through optimized resumes.

## 🚀 Setup & Installation

### Prerequisites
- Python 3.10+ or `uv` package manager.
- A Google Gemini API Key. (Get one at [Google AI Studio](https://aistudio.google.com/))

### Steps

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/yourusername/Ai_Cv.git
   cd Ai_Cv
   ```

2. **Configure Environment Variables:**
   Create a `.env` file in the root directory of the project and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Install dependencies:**
   ```bash
   pip install streamlit PyPDF2 google-generativeai python-dotenv
   ```
   *(Dependencies include streamlit, PyPDF2, google-generativeai, and python-dotenv).*

4. **Run the Application:**
   ```bash
   python -m streamlit run main.py
   ```
   *(Or just `streamlit run main.py` if your environment is already activated).*

5. **Open your browser** to the local Streamlit URL (typically `http://localhost:8501`) and start analyzing!

## 💡 Workflow
1. **Resume Upload:** User uploads a PDF or TXT file.
2. **Text Extraction:** PyPDF2 parses the textual data from the file.
3. **AI Analysis:** The extracted text and optional job role are structured into an advanced prompt and sent to the Gemini 1.5 Flash model.
4. **Feedback Generation:** The LLM processes the data and streams back an Executive Summary, ATS Compatibility check, Strengths, Weaknesses, and Actionable Recommendations directly to the UI.
