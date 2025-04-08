import random

def ai_turn(ai_remaining, player_character):
    if len(ai_remaining) <= 1:
        return ai_remaining, True  # AI guesses if only one remains
    action = random.choice(["ask", "eliminate"])
    if action == "ask":
        questions = [
            "Is your character male?",
            "Does your character have brown hair color?",
            "Does your character have long hair_length?",
            "Does your character wear glasses?",
            "Does your character have a hat?",
            "Does your character have a beard?"
        ]
        question = random.choice(questions)
        print(f"\nAI asks: {question}")
        answer = answer_question(question, player_character)
        print(f"You answer: {answer}")
        if answer == "Yes":
            if "male" in question:
                ai_remaining = [c for c in ai_remaining if c["gender"] == "male"]
            elif "brown hair" in question:
                ai_remaining = [c for c in ai_remaining if c["hair_color"] == "brown"]
            elif "long hair" in question:
                ai_remaining = [c for c in ai_remaining if c["hair_length"] == "long"]
            elif "glasses" in question:
                ai_remaining = [c for c in ai_remaining if c["wears_glasses"]]
            elif "hat" in question:
                ai_remaining = [c for c in ai_remaining if c["has_hat"]]
            elif "beard" in question:
                ai_remaining = [c for c in ai_remaining if c["has_beard"]]
        elif answer == "No":
            if "male" in question:
                ai_remaining = [c for c in ai_remaining if c["gender"] != "male"]
            elif "brown hair" in question:
                ai_remaining = [c for c in ai_remaining if c["hair_color"] != "brown"]
            elif "long hair" in question:
                ai_remaining = [c for c in ai_remaining if c["hair_length"] != "long"]
            elif "glasses" in question:
                ai_remaining = [c for c in ai_remaining if not c["wears_glasses"]]
            elif "hat" in question:
                ai_remaining = [c for c in ai_remaining if not c["has_hat"]]
            elif "beard" in question:
                ai_remaining = [c for c in ai_remaining if not c["has_beard"]]
        print(f"AI eliminated some characters. {len(ai_remaining)} remain.")
    else:
        char_to_eliminate = random.choice(ai_remaining)
        ai_remaining = [c for c in ai_remaining if c["id"] != char_to_eliminate["id"]]
        print(f"AI eliminated {char_to_eliminate['name']}. {len(ai_remaining)} remain.")
    return ai_remaining, False