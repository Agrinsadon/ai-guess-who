import json
import random

characters_json = '''
{
  "characters": [
    {"id": 1, "name": "Alex", "gender": "male", "hair_color": "brown", "hair_length": "short", "wears_glasses": false, "has_hat": false, "has_beard": true},
    {"id": 2, "name": "Bella", "gender": "female", "hair_color": "blonde", "hair_length": "long", "wears_glasses": true, "has_hat": false, "has_beard": false},
    {"id": 3, "name": "Charlie", "gender": "male", "hair_color": "black", "hair_length": "short", "wears_glasses": false, "has_hat": true, "has_beard": false},
    {"id": 4, "name": "Diana", "gender": "female", "hair_color": "red", "hair_length": "medium", "wears_glasses": false, "has_hat": false, "has_beard": false},
    {"id": 5, "name": "Evan", "gender": "male", "hair_color": "blonde", "hair_length": "short", "wears_glasses": true, "has_hat": false, "has_beard": false},
    {"id": 6, "name": "Fiona", "gender": "female", "hair_color": "brown", "hair_length": "long", "wears_glasses": false, "has_hat": true, "has_beard": false},
    {"id": 7, "name": "George", "gender": "male", "hair_color": "gray", "hair_length": "short", "wears_glasses": false, "has_hat": false, "has_beard": true},
    {"id": 8, "name": "Hannah", "gender": "female", "hair_color": "black", "hair_length": "medium", "wears_glasses": true, "has_hat": false, "has_beard": false},
    {"id": 9, "name": "Ian", "gender": "male", "hair_color": "brown", "hair_length": "medium", "wears_glasses": false, "has_hat": true, "has_beard": false},
    {"id": 10, "name": "Julia", "gender": "female", "hair_color": "blonde", "hair_length": "short", "wears_glasses": false, "has_hat": false, "has_beard": false},
    {"id": 11, "name": "Kevin", "gender": "male", "hair_color": "red", "hair_length": "short", "wears_glasses": true, "has_hat": false, "has_beard": false},
    {"id": 12, "name": "Lily", "gender": "female", "hair_color": "gray", "hair_length": "long", "wears_glasses": false, "has_hat": true, "has_beard": false}
  ]
}
'''

data = json.loads(characters_json)
characters = data["characters"]

ai_character = random.choice(characters)
print("AI has secretly chosen a character. Let’s start the game!")

def display_characters(char_list):
    print("\nRemaining characters:")
    for char in char_list:
        print(f"ID: {char['id']}, Name: {char['name']}, Gender: {char['gender']}, Hair Color: {char['hair_color']}, "
              f"Hair Length: {char['hair_length']}, Glasses: {char['wears_glasses']}, Hat: {char['has_hat']}, Beard: {char['has_beard']}")

def ai_answer_question(question):
    question = question.lower()
    if "male" in question or "man" in question:
        return "Yes" if ai_character["gender"] == "male" else "No"
    elif "female" in question or "woman" in question:
        return "Yes" if ai_character["gender"] == "female" else "No"
    elif "hair color" in question:
        color = question.split("hair color")[-1].strip()
        return "Yes" if ai_character["hair_color"] in color else "No"
    elif "hair length" in question:
        length = question.split("hair length")[-1].strip()
        return "Yes" if ai_character["hair_length"] in length else "No"
    elif "glasses" in question:
        return "Yes" if ai_character["wears_glasses"] else "No"
    elif "hat" in question:
        return "Yes" if ai_character["has_hat"] else "No"
    elif "beard" in question:
        return "Yes" if ai_character["has_beard"] else "No"
    else:
        return "I’m not sure how to answer that. Try a yes/no question about gender, hair, glasses, hat, or beard!"

remaining_characters = characters.copy()

while len(remaining_characters) > 1:
    display_characters(remaining_characters)
    print("\nOptions:")
    print("1. Ask a question")
    print("2. Pick/Eliminate characters")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        question = input("Ask a yes/no question about my character: ")
        answer = ai_answer_question(question)
        print(f"AI answers: {answer}")
        eliminate = input("Would you like to eliminate characters based on this? (yes/no): ").lower()
        if eliminate == "yes":
            ids_to_remove = input("Enter the IDs of characters to eliminate (comma-separated, e.g., 1, 2, 3): ")
            ids = [int(id.strip()) for id in ids_to_remove.split(",")]
            remaining_characters = [char for char in remaining_characters if char["id"] not in ids]
            print(f"Eliminated characters with IDs: {ids}")

    elif choice == "2":
        ids_to_remove = input("Enter the IDs of characters to eliminate (comma-separated, e.g., 1, 2, 3): ")
        ids = [int(id.strip()) for id in ids_to_remove.split(",")]
        remaining_characters = [char for char in remaining_characters if char["id"] not in ids]
        print(f"Eliminated characters with IDs: {ids}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

display_characters(remaining_characters)
print(f"\nOnly one character left: {remaining_characters[0]['name']}!")
guess = input(f"Do you think my character is {remaining_characters[0]['name']}? (yes/no): ").lower()
if guess == "yes":
    if remaining_characters[0]["id"] == ai_character["id"]:
        print("Congratulations! You guessed correctly!")
    else:
        print(f"Sorry, my character was {ai_character['name']}. You didn’t guess it!")
else:
    print(f"You didn’t guess. My character was {ai_character['name']}.")