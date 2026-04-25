import streamlit as st
import random
from wordbuff_game import evaluate_guess, WORDS

# --- Page Configuration ---
st.set_page_config(page_title="WordBuff", page_icon="🟩")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #121213;
    }
    div[data-testid="stVerticalBlock"] > div:has(div.stButton) {
        display: flex;
        justify-content: center;
    }
    .stTextInput input {
        text-align: center;
        text-transform: uppercase;
        font-size: 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- Initialize Game State ---
if "target" not in st.session_state:
    st.session_state.target = random.choice(WORDS).lower()
    st.session_state.history = []
    st.session_state.attempts = 5
    st.session_state.game_over = False

def restart_game():
    st.session_state.target = random.choice(WORDS).lower()
    st.session_state.history = []
    st.session_state.attempts = 5
    st.session_state.game_over = False

def submit_guess():
    guess = st.session_state.current_guess.lower().strip()
    
    if len(guess) != 5 or not guess.isalpha():
        st.warning("Please enter a valid 5-letter word.")
        return

    result = evaluate_guess(guess, st.session_state.target)
    st.session_state.history.append(result)
    st.session_state.attempts -= 1
    
    if guess == st.session_state.target:
        st.session_state.game_over = True
    elif st.session_state.attempts == 0:
        st.session_state.game_over = True
    
    # Clear input
    st.session_state.current_guess = ""

# --- UI Header ---
st.markdown("<h1 style='text-align: center; color: white;'>WORD BUFF</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #818384;'>Guess the 5-letter hidden word.</p>", unsafe_allow_html=True)
st.divider()

# --- Game Grid ---
grid_container = st.container()

grid_container = st.container()

with grid_container:
    # Display historical guesses
    for row in st.session_state.history:
        # Using a container with a margin for row spacing
        with st.container():
            cols = st.columns([1,1,1,1,1], gap="small")
            for i, item in enumerate(row):
                if item["color"] == "\033[92m": color = "#6aaa64" 
                elif item["color"] == "\033[93m": color = "#c9b458" 
                else: color = "#3a3a3c" 
                
                cols[i].markdown(f"""
                    <div style="background-color:{color}; padding:15px; text-align:center; 
                    font-weight:bold; font-size:22px; color:white; border-radius:4px; 
                    margin-bottom:10px;"> {item['char'].upper()}
                    </div>""", unsafe_allow_html=True)

    # Display empty rows for remaining attempts
    for _ in range(st.session_state.attempts):
        with st.container():
            cols = st.columns([1,1,1,1,1], gap="small")
            for i in range(5):
                cols[i].markdown("""
                    <div style="background-color:transparent; padding:15px; text-align:center; 
                    border: 2px solid #3a3a3c; border-radius:4px; height:65px; 
                    margin-bottom:10px;"> </div>""", unsafe_allow_html=True)

st.divider()

# --- Input Section ---
if not st.session_state.game_over:
    st.text_input(
        "Enter your guess", 
        key="current_guess", 
        max_chars=5, 
        on_change=submit_guess,
        label_visibility="collapsed",
        placeholder="Type here & press Enter"
    )
else:
    if len(st.session_state.history) > 0 and "".join([x['char'] for x in st.session_state.history[-1]]) == st.session_state.target:
        st.balloons()
        st.success(f"Excellent! The word was **{st.session_state.target.upper()}**")
    else:
        st.error(f"Game Over! The word was **{st.session_state.target.upper()}**")
    
    st.button("Play Again", on_click=restart_game)