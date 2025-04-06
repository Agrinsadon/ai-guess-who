import json
import random

# JSON data for characters
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

# Load characters
data = json.loads(characters_json)
characters = data["characters"]


# Display characters for player to pick
def display_characters(char_list):
    print("\nCharacters:")
    for char in char_list:
        print(f"ID: {char['id']}, Name: {char['name']}, Gender: {char['gender']}, Hair Color: {char['hair_color']}, "
              f"Hair Length: {char['hair_length']}, Glasses: {char['wears_glasses']}, Hat: {char['has_hat']}, Beard: {char['has_beard']}")


# Player picks a character
print("Pick your character secretly from the list below:")
display_characters(characters)
player_char_id = int(input("Enter the ID of your character: "))
player_character = next(char for char in characters if char["id"] == player_char_id)
print(f"You’ve picked {player_character['name']}. Let’s start the game!")

# AI picks a random character
ai_character = random.choice(characters)
print("AI has secretly chosen a character.")


# Function to answer a question based on a character
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


# AI’s turn logic
def ai_turn(ai_remaining):
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


# Main game loop
player_remaining = characters.copy()
ai_remaining = characters.copy()

while len(player_remaining) > 0 and len(ai_remaining) > 0:
    # Player’s turn
    display_characters(player_remaining)
    print("\nYour Options:")
    print("1. Ask a question")
    print("2. Pick/Eliminate characters")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        question = input("Ask a yes/no question about my character: ")
        answer = answer_question(question, ai_character)
        print(f"AI answers: {answer}")
        eliminate = input("Would you like to eliminate characters based on this? (yes/no): ").lower()
        if eliminate == "yes":
            ids_to_remove = input("Enter the IDs of characters to eliminate (comma-separated, e.g., 1, 2, 3): ")
            ids = [int(id.strip()) for id in ids_to_remove.split(",")]
            player_remaining = [char for char in player_remaining if char["id"] not in ids]
            print(f"Eliminated characters with IDs: {ids}")

    elif choice == "2":
        print("\nSub-options:")
        print("1. Guess the AI’s character")
        print("2. Eliminate characters")
        sub_choice = input("Enter your choice (1 or 2): ")

        if sub_choice == "1":
            guess = input("Enter the name of the character you think I picked: ").strip()
            if guess.lower() == ai_character["name"].lower():
                print(f"Congratulations! You guessed correctly! My character was {ai_character['name']}.")
                break
            else:
                print(f"Sorry, that’s not correct. My character is not {guess}. Game continues!")

        elif sub_choice == "2":
            ids_to_remove = input("Enter the IDs of characters to eliminate (comma-separated, e.g., 1, 2, 3): ")
            ids = [int(id.strip()) for id in ids_to_remove.split(",")]
            player_remaining = [char for char in player_remaining if char["id"] not in ids]
            print(f"Eliminated characters with IDs: {ids}")

        else:
            print("Invalid sub-choice. Please enter 1 or 2.")

    else:
        print("Invalid choice. Please enter 1 or 2.")

    # Check if player has one left
    if len(player_remaining) == 1:
        print(f"\nYou have one character left: {player_remaining[0]['name']}!")
        guess = input(f"Is my character {player_remaining[0]['name']}? (yes/no): ").lower()
        if guess == "yes" and player_remaining[0]["id"] == ai_character["id"]:
            print("Congratulations! You guessed correctly!")
            break
        elif guess == "yes":
            print(f"Sorry, my character was {ai_character['name']}. You lose!")
            break
        else:
            print("Game continues...")

    # AI’s turn
    ai_remaining, ai_guessed = ai_turn(ai_remaining)
    if ai_guessed and len(ai_remaining) == 1:
        print(f"\nAI guesses: Is your character {ai_remaining[0]['name']}?")
        if ai_remaining[0]["id"] == player_character["id"]:
            print(f"AI wins! Your character was {player_character['name']}.")
            break
        else:
            print("AI guessed wrong. Game continues!")
            ai_remaining = [c for c in ai_remaining if c["id"] != ai_remaining[0]["id"]]  # Remove wrong guess

# End conditions
if len(player_remaining) == 0:
    print(f"\nYou eliminated all characters! My character was {ai_character['name']}.")
if len(ai_remaining) == 0:
    print(f"\nAI eliminated all characters! Your character was {player_character['name']}.")