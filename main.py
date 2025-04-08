import random
from characters import characters
from utils import display_characters, answer_question, eliminate_characters
from ai_logic import ai_turn

print("Pick your character secretly from the list below:")
display_characters(characters)
player_char_id = int(input("Enter the ID of your character: "))
player_character = next(char for char in characters if char["id"] == player_char_id)
print(f"You’ve picked {player_character['name']}. Let’s start the game!")

ai_character = random.choice(characters)
print("AI has secretly chosen a character.")

player_remaining = characters.copy()
ai_remaining = characters.copy()

while len(player_remaining) > 0 and len(ai_remaining) > 0:
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
        if eliminate in ["yes", "y"]:
            player_remaining = eliminate_characters(player_remaining, question, expected_answer=answer)
            print("Characters have been automatically eliminated based on the AI's answer.")

    elif choice == "2":
        print("\nSub-options:")
        print("1. Guess the AI’s character")
        print("2. Eliminate characters manually")
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
        print("Invalid choice. Please enter 1 or 2.")

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

    ai_remaining, ai_guessed = ai_turn(ai_remaining, player_character)
    if ai_guessed and len(ai_remaining) == 1:
        print(f"\nAI guesses: Is your character {ai_remaining[0]['name']}?")
        if ai_remaining[0]["id"] == player_character["id"]:
            print(f"AI wins! Your character was {player_character['name']}.")
            break
        else:
            print("AI guessed wrong. Game continues!")
            ai_remaining = [c for c in ai_remaining if c["id"] != ai_remaining[0]["id"]]

if len(player_remaining) == 0:
    print(f"\nYou eliminated all characters! My character was {ai_character['name']}.")
if len(ai_remaining) == 0:
    print(f"\nAI eliminated all characters! Your character was {player_character['name']}.")
