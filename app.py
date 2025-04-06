import streamlit as st
from inference import predict, questions
from decision_tree import train
import json

st.title("🕵️ AI Guess Who")

st.markdown("Vastaa kyllä/ei-kysymyksiin ja tekoäly arvaa hahmon!")

answers = {}
for key, question in questions:
    answers[key] = st.radio(question, ["Kyllä", "Ei"]) == "Kyllä"

if st.button("Arvaa hahmo"):
    guess = predict(answers)
    st.success(f"🤖 Minä arvaan, että hahmosi on **{guess}**!")

    # Ask for feedback
    if st.button("Se oli väärin!"):
        correct_name = st.text_input("Mikä oli oikea hahmo?")

        if correct_name:
            # Add the new character to the dataset based on user input
            new_character = {
                "name": correct_name,
                "real": answers["real"],
                "movie": answers["movie"],
                "superpowers": answers["superpowers"],
                "human": answers["human"],
                "anime": answers["anime"]
            }

            # Load the existing characters from the JSON file
            with open("characters.json", "r") as f:
                characters = json.load(f)

            # Append the new character
            characters.append(new_character)

            # Save the updated list of characters back to the file
            with open("characters.json", "w") as f:
                json.dump(characters, f, indent=4)

            # Retrain the model with the updated dataset
            train()

            st.success(f"✅ Hahmo **{correct_name}** lisätty ja malli päivitetty!")
