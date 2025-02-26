import streamlit as st
import random

# Initialize all session state variables at the start
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'asked_questions' not in st.session_state:
    st.session_state.asked_questions = set()
if 'questions_count' not in st.session_state:
    st.session_state.questions_count = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = None

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f6f7;
    }
    .stTitle {
        color: #1e4d2b;
        font-family: 'Arial', sans-serif;
        text-align: center;
        padding: 20px;
        border-bottom: 2px solid #1e4d2b;
    }
    .category-button {
        background-color: #1e4d2b;
        color: white;
        padding: 15px 30px;
        border-radius: 10px;
        margin: 10px;
        text-align: center;
        cursor: pointer;
    }
    .quote-container {
        background-color: #fff;
        padding: 20px;
        border-left: 5px solid #1e4d2b;
        margin: 20px 0;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Quiz questions by category (expanded to 15 questions each)
quiz_categories = {
    "Islamic Knowledge": {
        "Who was the first prophet in Islam?": "Adam",
        "In which month was the Quran revealed?": "Ramadan",
        "How many pillars are there in Islam?": "5",
        "Which is the holiest city in Islam?": "Mecca",
        "Who was the last prophet in Islam?": "Muhammad",
        "What is the Islamic greeting?": "Assalamualaikum",
        "How many chapters (Surahs) are there in the Quran?": "114",
        "What is the first revealed word of the Quran?": "Iqra",
        "Which angel brought revelations to Prophet Muhammad (PBUH)?": "Jibreel",
        "What is the name of the holy book in Islam?": "Quran",
        "What is the second pillar of Islam?": "Salah",
        "How many times do Muslims pray daily?": "5",
        "What is the Islamic New Year called?": "Hijri",
        "Which month do Muslims fast in?": "Ramadan",
        "What is the name of the holy mosque in Mecca?": "Masjid Al-Haram"
    },
    "General Knowledge": {
        "What is the capital of Japan?": "Tokyo",
        "Who painted the Mona Lisa?": "Leonardo da Vinci",
        "Which planet is known as the Red Planet?": "Mars",
        "What is the largest ocean on Earth?": "Pacific",
        "Who wrote Romeo and Juliet?": "William Shakespeare",
        "What is the capital of France?": "Paris",
        "Which is the largest planet in our solar system?": "Jupiter",
        "What is the chemical symbol for gold?": "Au",
        "Who invented the telephone?": "Alexander Graham Bell",
        "What is the tallest mountain in the world?": "Mount Everest",
        "Which is the largest continent?": "Asia",
        "What is the currency of Japan?": "Yen",
        "Who painted the Sistine Chapel ceiling?": "Michelangelo",
        "What is the largest desert in the world?": "Sahara",
        "Which country is known as the Land of the Rising Sun?": "Japan"
    },
    "Scientific Facts": {
        "What is the chemical symbol for gold?": "Au",
        "What is the hardest natural substance on Earth?": "Diamond",
        "What is the closest star to Earth?": "Sun",
        "What is the speed of light?": "299792458",
        "What is the chemical formula for water?": "H2O",
        "What is the largest organ in the human body?": "Skin",
        "What is the symbol for the element Oxygen?": "O",
        "What planet is known as the Blue Planet?": "Earth",
        "What is the atomic number of Carbon?": "6",
        "What is the powerhouse of the cell?": "Mitochondria",
        "What is the study of fossils called?": "Paleontology",
        "What is the unit of force?": "Newton",
        "What is the process by which plants make food?": "Photosynthesis",
        "What is the smallest unit of matter?": "Atom",
        "What is the normal body temperature in Celsius?": "37"
    }
}

# Growth mindset quotes
growth_mindset_quotes = [
    "\"The development of the mind comes through challenge.\" - Prophet Muhammad (PBUH)",
    "\"Seek knowledge from the cradle to the grave.\" - Islamic Proverb",
    "\"Success is not final, failure is not fatal: it is the courage to continue that counts.\" - Winston Churchill",
    "\"The only way to do great work is to love what you do.\" - Steve Jobs",
    "\"Every expert was once a beginner.\" - Helen Hayes"
]

def check_answer(user_answer, correct_answer):
    return user_answer.lower().strip() == correct_answer.lower().strip()

# App title
st.title("🌟 Interactive Learning Quiz")

# Display growth mindset message at the start
if not st.session_state.quiz_started:
    st.markdown("""
        <div class='quote-container'>
            <h3>🌱 Embrace the Growth Mindset</h3>
            <p style='font-style: italic;'>{}</p>
            <br>
            <p>Remember: Every question is an opportunity to learn and grow. Your intelligence and abilities can be developed through dedication and hard work!</p>
        </div>
    """.format(random.choice(growth_mindset_quotes)), unsafe_allow_html=True)

# Category selection
if not st.session_state.selected_category:
    st.markdown("### Choose Your Quiz Category:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("☪️ Islamic Knowledge", key="islamic"):
            st.session_state.selected_category = "Islamic Knowledge"
            st.session_state.quiz_started = True
    
    with col2:
        if st.button("🌍 General Knowledge", key="general"):
            st.session_state.selected_category = "General Knowledge"
            st.session_state.quiz_started = True
    
    with col3:
        if st.button("🔬 Scientific Facts", key="science"):
            st.session_state.selected_category = "Scientific Facts"
            st.session_state.quiz_started = True

# Continue with quiz if category is selected
if st.session_state.selected_category:
    current_questions = quiz_categories[st.session_state.selected_category]
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Get user input
    user_input = st.chat_input("Type your answer here...")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.chat_message("assistant"):
            bot_response = ""
            if len(st.session_state.chat_history) == 1:
                # First interaction - start the quiz
                available_questions = [q for q in current_questions.keys() 
                                    if q not in st.session_state.asked_questions]
                question = random.choice(available_questions)
                bot_response = f"🌟 Welcome to the {st.session_state.selected_category} Quiz!\n\nHere's your question:\n\n{question}"
                st.write(bot_response)
                st.session_state.current_question = question
                st.session_state.asked_questions.add(question)
                st.session_state.questions_count = 1
            else:
                correct_answer = current_questions[st.session_state.current_question]
                if check_answer(user_input, correct_answer):
                    bot_response = "✨ MashaAllah! That's correct! 🎉"
                    st.write(bot_response)
                    st.session_state.score += 1
                else:
                    bot_response = f"""❌ That's not correct.
Your answer: {user_input}
Correct answer: {correct_answer}

Don't worry! Keep learning and trying! 💪"""
                    st.write(bot_response)
                
                # Check if we've reached 15 questions
                if st.session_state.questions_count >= 15:
                    final_score = st.session_state.score
                    percentage = (final_score / 15) * 100
                    
                    final_message = f"""
                    \n🎊 Quiz completed! 🎊
                    {'─' * 40}
                    Your final score: {final_score}/15 ({percentage:.1f}%)
                    
                    {('MashaAllah! Outstanding performance! 🌟' if percentage >= 80 
                      else 'Good effort! Keep learning! 💫')}
                    
                    Would you like to try another category? Just refresh the page!
                    """
                    st.write(final_message)
                    bot_response += final_message
                    # Reset the quiz
                    st.session_state.chat_history = []
                    st.session_state.score = 0
                    st.session_state.asked_questions = set()
                    st.session_state.questions_count = 0
                    st.session_state.selected_category = None
                else:
                    # Get next question from unused questions
                    available_questions = [q for q in current_questions.keys() 
                                        if q not in st.session_state.asked_questions]
                    question = random.choice(available_questions)
                    next_question = f"""\n\n📝 Next Question:\n{'─' * 40}\n{question}"""
                    st.write(next_question)
                    bot_response += next_question
                    st.session_state.current_question = question
                    st.session_state.asked_questions.add(question)
                    st.session_state.questions_count += 1

            st.session_state.chat_history.append({"role": "assistant", "content": bot_response})

    # Add exit button in sidebar
    if st.sidebar.button("Exit Quiz"):
        st.markdown("""
            <div style='background-color: #f0f7ff; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;'>
                <h2>🙏 Thank you for using our Quiz App!</h2>
                <p>We hope you learned something new today.</p>
                <p>Remember: "Seeking knowledge is an obligation upon every Muslim."</p>
                <p>Come back soon for more learning! In Sha Allah 🌟</p>
            </div>
        """, unsafe_allow_html=True)
        # Reset all session state
        st.session_state.chat_history = []
        st.session_state.score = 0
        st.session_state.selected_category = None
        st.session_state.quiz_started = False
        st.session_state.asked_questions = set()
        st.session_state.questions_count = 0
        st.session_state.current_question = None
        st.rerun()

    # Display current score (only if quiz is active)
    st.sidebar.markdown(f"""
        <div style='background-color: #1e4d2b; color: white; padding: 20px; border-radius: 10px; text-align: center;'>
            <h3>{st.session_state.selected_category}</h3>
            <h2>Score: {st.session_state.score}/15</h2>
            <p>Question {st.session_state.questions_count}/15</p>
            <p>Keep going! You're doing great!</p>
        </div>
    """, unsafe_allow_html=True) 