import streamlit as st
from model import predict_character

st.title("AI Guess Who – The Mystery Character Game")

questions = [
    "Is the character real?",
    "Is it from a movie?",
    "Does it have superpowers?",
    "Is it human?",
    "Is it from an anime?"
]

answers = []
for q in questions:
    answer = st.radio(q, ["Yes", "No"])
    answers.append(answer)

if st.button("Guess Character"):
    character = predict_character(answers)
    st.success(f"I think your character is {character}! 🎉")
