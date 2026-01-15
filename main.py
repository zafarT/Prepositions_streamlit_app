import streamlit as st
import pandas as pd
import random

# ---------------------------------------------------------
# 1. DATA PREPARATION
# ---------------------------------------------------------
# We stick to the B2 list we discussed.
# You can replace this with a CSV load if you prefer later.
# ---------------------------------------------------------
# EXPANDED B2 DATA SET
# ---------------------------------------------------------
try:
    df = pd.read_csv('prep.csv')
    data = df.to_dict('records')
except FileNotFoundError:
    st.error("prep.csv file not found. Please ensure the file exists.")
    data = []

# ---------------------------------------------------------
# 2. SESSION STATE MANAGEMENT
# ---------------------------------------------------------
# This keeps track of which card we are looking at and if it is flipped
if 'card_index' not in st.session_state:
    st.session_state.card_index = 0
    st.session_state.flipped = False
    if data:
        random.shuffle(data) # Shuffle once at startup
    st.session_state.deck = data

def next_card():
    # Move to next card and reset flip state
    if st.session_state.deck:
        st.session_state.card_index = (st.session_state.card_index + 1) % len(st.session_state.deck)
        st.session_state.flipped = False

def flip_card():
    st.session_state.flipped = not st.session_state.flipped

# ---------------------------------------------------------
# 3. UI LAYOUT & CSS
# ---------------------------------------------------------
st.set_page_config(page_title="B2 German Flashcards", page_icon="🇩🇪")

# Custom CSS to make it look like a real card
st.markdown("""
<style>
    .flashcard {
        background-color: #f9f9f9;
        border: 2px solid #ddd;
        border-radius: 15px;
        padding: 50px;
        text-align: center;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: #333;
    }
    .verb-text {
        font-size: 40px;
        font-weight: bold;
        color: #333;
    }
    .prep-text {
        font-size: 30px;
        color: #d63031; /* Red for emphasis */
        font-weight: bold;
    }
    .case-badge {
        background-color: #0984e3;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 16px;
        margin-top: 10px;
        display: inline-block;
    }
    .sentence-box {
        margin-top: 20px;
        font-style: italic;
        color: #555;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

st.title("Verb-Prepositions")

if st.session_state.deck:
    st.progress((st.session_state.card_index + 1) / len(st.session_state.deck))

    # Get current card data
    card = st.session_state.deck[st.session_state.card_index]

    # ---------------------------------------------------------
    # 4. CARD DISPLAY LOGIC
    # ---------------------------------------------------------
    # We use a container to hold the card content
    card_container = st.container()

    with card_container:
        if not st.session_state.flipped:
            # --- FRONT SIDE ---
            st.markdown(f"""
            <div class="flashcard">
                <div style="font-size: 20px; color: #888;">VERB</div>
                <div class="verb-text">{card['verb']}</div>
                <div style="font-size: 14px; color: #888; margin-top: 20px;">(Click Flip to reveal preposition)</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # --- BACK SIDE ---
            st.markdown(f"""
            <div class="flashcard">
                <div class="verb-text" style="font-size: 25px; margin-bottom: 10px;">{card['verb']}</div>
                <div class="prep-text">{card['prep']} <span style="color: #333;">+</span> <span class="case-badge">{card['case']}</span></div>
                <div style="margin-top: 10px; font-weight: bold;">{card['trans']}</div>
                <div class="sentence-box">"{card['sentence']}"</div>
            </div>
            """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 5. CONTROLS
    # ---------------------------------------------------------
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("🔄 FLIP CARD", use_container_width=True):
            flip_card()
            st.rerun()

        if st.button("➡️ NEXT CARD", use_container_width=True):
            next_card()
            st.rerun()

    st.caption(f"Card {st.session_state.card_index + 1} of {len(st.session_state.deck)}")
else:
    st.warning("No cards available to display.")
