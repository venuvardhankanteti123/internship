import streamlit as st
import google.generativeai as genai
responses = {}
import os
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="SWOT ANALYSIS")
st.title("SWOT Analysis for JEE Aspirants")
st.header("Answer the following questions to receive insights into your Strengths, Weaknesses, Opportunities, and Threats.")

option_questions = [
    {"id": 1, "question": "What is your strongest subject?", "options": ["Physics", "Chemistry", "Mathematics", "All"]},
    {"id": 2, "question": "Which subject do you find the most difficult?", "options": ["Physics", "Chemistry", "Mathematics"]},
    {"id": 3, "question": "How often do you study Physics?", "options": ["Daily", "Weekly", "Occasionally", "Rarely"]},
    {"id": 4, "question": "How often do you study Chemistry?", "options": ["Daily", "Weekly", "Occasionally", "Rarely"]},
    {"id": 5, "question": "How often do you study Mathematics?", "options": ["Daily", "Weekly", "Occasionally", "Rarely"]},
    {"id": 6, "question": "What is your preferred study time?", "options": ["Morning", "Afternoon", "Evening", "Night"]},
    {"id": 7, "question": "Which branch of Chemistry do you excel in?", "options": ["Organic", "Inorganic", "Physical", "All"]},
    {"id": 8, "question": "Which branch of Chemistry do you find the most difficult?", "options": ["Organic", "Inorganic", "Physical", "None"]},
    {"id": 9, "question": "What type of Physics problems do you excel in?", "options": ["Mechanics", "Electrodynamics", "Thermodynamics", "Modern Physics"]},
    {"id": 10, "question": "What type of Mathematics problems do you find most challenging?", "options": ["Algebra", "Calculus", "Probability", "Geometry"]},
    {"id": 11, "question": "How often do you take mock tests?", "options": ["Every day", "Weekly", "Occasionally", "Never"]},
    {"id": 12, "question": "How frequently do you revise your concepts?", "options": ["Daily", "Weekly", "Monthly", "Rarely"]},
    {"id": 13, "question": "How do you prepare for problem-solving?", "options": ["Practice regularly", "Solve previous papers", "Attend coaching", "Self-study only"]},
    {"id": 14, "question": "Which study method works best for you?", "options": ["Group study", "Individual study", "Coaching classes", "Online tutorials"]},
    {"id": 15, "question": "What is your biggest distraction while studying?", "options": ["Social media", "Family obligations", "Health issues", "None"]},
    {"id": 16, "question": "Which study resources do you use?", "options": ["Books", "Online videos", "Coaching materials", "All"]},
    {"id": 17, "question": "Do you prefer timed practice sessions?", "options": ["Yes", "No"]},
    {"id": 18, "question": "What is your primary goal for this month?", "options": ["Improving weak subjects", "Taking more tests", "Revising concepts", "Scoring high in tests"]},
    {"id": 19, "question": "What is your biggest fear regarding JEE?", "options": ["Time management", "Difficult questions", "Negative marking", "None"]},
    {"id": 20, "question": "How do you track your progress?", "options": ["Test scores", "Feedback from mentors", "Self-assessment", "I don’t track"]},
    {"id": 21, "question": "What is your confidence level for JEE?", "options": ["High", "Moderate", "Low", "Not confident"]},
    {"id": 22, "question": "Do you use a dedicated study space?", "options": ["Yes", "No"]},
    {"id": 23, "question": "How often do you solve previous years’ question papers?", "options": ["Daily", "Weekly", "Occasionally", "Rarely"]},
    {"id": 24, "question": "What is your preferred way of revising concepts?", "options": ["Notes", "Online resources", "Group discussions", "Coaching material"]},
    {"id": 25, "question": "What motivates you the most?", "options": ["Career aspirations", "Parental expectations", "Self-interest", "Peers"]},
    {"id": 26, "question": "Do you attend doubt-clearing sessions?", "options": ["Yes", "No"]},
    {"id": 27, "question": "How do you approach a tough question?", "options": ["Skip it", "Attempt later", "Try immediately", "Seek help"]},
    {"id": 28, "question": "Do you prefer digital or paper-based tests?", "options": ["Digital", "Paper-based"]},
    {"id": 29, "question": "What do you prioritize during tests?", "options": ["Accuracy", "Speed", "Both"]},
    {"id": 30, "question": "What is your biggest strength?", "options": ["Knowledge", "Speed", "Accuracy", "Problem-solving"]},
]

for q in option_questions:
    responses[q["question"]] = st.selectbox(q["question"], q["options"])

slider_questions = [
    "Rate your time management skills on a scale of 1-10.",
    "Rate your confidence in solving mock test problems.",
    "Rate your consistency in studying daily.",
    "Rate your focus during study sessions.",
    "Rate the stress level you feel about JEE.",
    "Rate your ability to complete mock tests within the time limit.",
    "Rate your understanding of Physics concepts.",
    "Rate your understanding of Chemistry concepts.",
    "Rate your understanding of Mathematics concepts.",
    "Rate your overall JEE preparation on a scale of 1-10.",
    "Rate your ability to recall formulas during tests.",
    "Rate your performance in group studies.",
    "Rate your problem-solving speed.",
    "Rate your mental endurance during long study hours.",
    "Rate your ability to adapt to new topics quickly.",
]

for i, question in enumerate(slider_questions, start=31):
    responses[question] = st.slider(question, min_value=1, max_value=10, value=5)

text_questions = [
    "What is your biggest challenge while preparing for JEE?",
    "Describe your daily study routine.",
    "What do you enjoy most about preparing for JEE?",
    "What is your primary strategy for revising concepts?",
    "What is your plan for improving weak topics?",
    "What motivates you to keep studying?",
    "What feedback have you received from mentors or peers?",
    "What do you fear most about the JEE exam?",
    "Describe your ideal study environment.",
    "What is your long-term goal beyond JEE?",
]

for i, question in enumerate(text_questions, start=46):
    responses[question] = st.text_area(question)

responses_string = ""
for question_id, answer in responses.items():
    responses_string += f"Question: {question_id}\nAnswer: {answer}\n\n"

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt,responses_string):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([input_prompt,responses_string])
    return response.text
input_prompt="""
Analyze the following student's responses to a questionnaire about their preparation for the Joint Entrance Examination (JEE) and generate a personalized SWOT analysis report. The report should identify the student's:

- Strengths: Areas where the student excels and has a strong foundation
- Weaknesses: Areas where the student struggles or needs improvement
- Opportunities: Potential areas for growth and development
- Threats: External factors that may impact the student's performance or progress

Assumptions:

- The student is preparing for the JEE exam and wants to improve their performance
- The student is willing to put in effort and make changes to achieve their goals
- The student has access to resources and support to help them improve

Tone:

- Objective and analytical, with a focus on providing actionable recommendations
- Encouraging and supportive, with a focus on helping the student achieve their goals
"""
if st.button("Submit"):
    response=get_gemini_response(input_prompt,responses_string)
    st.write(response)
