def display_characters(char_list):
    print("\nCharacters:")
    for char in char_list:
        print(f"ID: {char['id']}, Name: {char['name']}, Gender: {char['gender']}, Hair Color: {char['hair_color']}, "
              f"Hair Length: {char['hair_length']}, Glasses: {char['wears_glasses']}, Hat: {char['has_hat']}, Beard: {char['has_beard']}")

def answer_question(question, character):
    question = question.lower()
    if "male" in question or "man" in question:
        return "Yes" if character["gender"] == "male" else "No"
    elif "female" in question or "woman" in question:
        return "Yes" if character["gender"] == "female" else "No"
    elif "hair color" in question:
        color = question.split("hair color")[-1].strip()
        return "Yes" if character["hair_color"] in color else "No"
    elif "hair length" in question:
        length = question.split("hair_length")[-1].strip()
        return "Yes" if character["hair_length"] in length else "No"
    elif "glasses" in question:
        return "Yes" if character["wears_glasses"] else "No"
    elif "hat" in question:
        return "Yes" if character["has_hat"] else "No"
    elif "beard" in question:
        return "Yes" if character["has_beard"] else "No"
    else:
        return "I’m not sure how to answer that. Try a yes/no question about gender, hair, glasses, hat, or beard!"