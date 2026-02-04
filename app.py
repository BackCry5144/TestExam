
import streamlit as st
import json
import os

# Set page config
st.set_page_config(page_title="OutSystems Certification Practice (Bilingual)", page_icon="🚀", layout="wide")

# Custom CSS for better aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stRadio [role="radiogroup"] {
        padding: 10px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .question-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        border-left: 5px solid #2d3e50;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .correct-ans {
        color: #28a745;
        font-weight: bold;
    }
    .wrong-ans {
        color: #dc3545;
        font-weight: bold;
    }
    .explanation {
        background-color: #f1f3f5;
        padding: 15px;
        border-radius: 10px;
        font-style: italic;
        border-left: 3px solid #2d3e50;
    }
    </style>
""", unsafe_allow_html=True)

# Image paths mapping
IMAGES = {
    "46": "Q46.png",
    "52": "Q52.png",
    "64": "Q64.png"
}

# Load data
@st.cache_data
def load_quiz_data():
    questions_file = "structured_data.json"
    trans_file = "translations.json"
    
    questions = []
    if os.path.exists(questions_file):
        with open(questions_file, "r", encoding="utf-8") as f:
            questions = json.load(f)
            
    translations = {}
    opt_translations = {}
    if os.path.exists(trans_file):
        with open(trans_file, "r", encoding="utf-8") as f:
            t_data = json.load(f)
            translations = t_data.get('translations', {})
            opt_translations = t_data.get('option_translations', {})
            
    return questions, translations, opt_translations

questions, trans, opt_trans = load_quiz_data()

# Session State for User Answers
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Sidebar for Navigation and Progress
st.sidebar.title("🎮 Quiz Control")
if st.sidebar.button("Reset Quiz"):
    st.session_state.user_answers = {}
    st.session_state.submitted = False
    st.rerun()

st.title("🛡️ OutSystems Associate Certification Practice Exam (KR/EN)")
st.write("---")

def get_bilingual_q(q_text):
    t = trans.get(q_text, "")
    return f"{q_text} ({t})" if t else q_text

def get_bilingual_opt(opt_text):
    t = opt_trans.get(opt_text, "")
    return f"{opt_text} ({t})" if t else opt_text

if questions:
    if not st.session_state.submitted:
        # Quiz Form
        with st.form("quiz_form"):
            for q in questions:
                st.markdown(f"#### 문제 {q['id']}")
                st.markdown(get_bilingual_q(q['question']))
                
                # Show image if exists
                if q['id'] in IMAGES and os.path.exists(IMAGES[q['id']]):
                    st.image(IMAGES[q['id']], caption=f"Reference for Question {q['id']}", width='stretch')
                
                # Format options for display
                options_list = [f"{opt['code']}. {get_bilingual_opt(opt['text'])}" for opt in q['options']]
                
                selected = st.radio(
                    f"Select your answer for Question {q['id']}:",
                    options_list,
                    index=None,
                    key=f"q_{q['id']}",
                    label_visibility="collapsed"
                )
                
                # Store answer (just the code A, B, C...)
                st.session_state.user_answers[q['id']] = selected[0] if selected else None
                st.write("") # Spacer

            submit_btn = st.form_submit_button("Submit Exam / 답안 제출", width='stretch')
            if submit_btn:
                st.session_state.submitted = True
                st.rerun()
    else:
        # Results Section
        score = 0
        wrong_questions = []
        
        for q in questions:
            if st.session_state.user_answers.get(q['id']) == q['answer_code']:
                score += 1
            else:
                wrong_questions.append(q)
        
        # summary
        st.header("📊 Exam Results / 시험 결과")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Questions", len(questions))
        col2.metric("Correct Answers", score, f"{score/len(questions)*100:.1f}%")
        col3.metric("Wrong Answers", len(wrong_questions))
        
        progress = score / len(questions)
        st.progress(progress)
        
        if progress >= 0.7:
            st.success("🎉 Congratulations! You passed. (합격점 70% 이상)")
        else:
            st.error("📉 You need more practice. (합격기준 미달)")
            
        st.write("---")
        st.subheader("📝 Review & Explanations / 오답 노트 및 해설")
        
        for q in questions:
            user_choice = st.session_state.user_answers.get(q['id'], "No Answer")
            correct_choice = q['answer_code']
            is_correct = user_choice == correct_choice
            
            with st.expander(f"문제 {q['id']}: {'✅ Correct' if is_correct else '❌ Incorrect'}", expanded=True):
                st.markdown(f"**Question:** {get_bilingual_q(q['question'])}")
                
                # Show image if exists
                if q['id'] in IMAGES and os.path.exists(IMAGES[q['id']]):
                    st.image(IMAGES[q['id']], width='stretch')

                # Display options
                for opt in q['options']:
                    color = "black"
                    prefix = ""
                    if opt['code'] == correct_choice:
                        color = "green"
                        prefix = "✔️ **(Answer)** "
                    elif opt['code'] == user_choice and not is_correct:
                        color = "red"
                        prefix = "✖️ **(Your Choice)** "
                    
                    st.markdown(f"<p style='color:{color}; margin-left: 20px;'>{prefix}{opt['code']}. {get_bilingual_opt(opt['text'])}</p>", unsafe_allow_html=True)
                
                if not is_correct:
                    st.markdown(f"**Your Answer:** <span class='wrong-ans'>{user_choice}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Correct Answer:** <span class='correct-ans'>{correct_choice}</span>", unsafe_allow_html=True)
                
                st.markdown("**Explanation / 해설:**")
                st.info(q['explanation'])
        
        if st.button("Restart Quiz / 다시 풀기"):
            st.session_state.submitted = False
            st.session_state.user_answers = {}
            st.rerun()

else:
    st.error("Question data not found. Please ensure 'structured_data.json' exists.")
