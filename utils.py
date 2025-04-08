import re

def display_characters(char_list):
    print("\nCurrent characters:")
    for char in char_list:
        print(f"{char['id']}: {char['name']}")

def parse_question(question):
    question = question.lower()
    if re.search(r'\b(glasses|wear.*glasses|has glasses|spectacles)\b', question):
        return "glasses"
    elif re.search(r'\b(hat|wear.*hat|has hat|cap|helmet)\b', question):
        return "hat"
    elif re.search(r'\b(beard|has beard|facial hair|bearded)\b', question):
        return "beard"
    else:
        return None

def answer_question(question, character):
    keyword = parse_question(question)
    if keyword is None:
        return "I don't understand the question."
    return "yes" if character["attributes"].get(keyword, False) else "no"

def eliminate_characters(remaining_chars, question, expected_answer):
    keyword = parse_question(question)
    if keyword is None:
        print("Couldn't understand which attribute to use for elimination.")
        return remaining_chars

    expected_bool = True if expected_answer == "yes" else False
    return [char for char in remaining_chars if char["attributes"].get(keyword) == expected_bool]
