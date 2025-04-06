# Guess Who: AI Edition

A Python terminal game where you and an AI play "Guess Who." Pick a character, ask yes/no questions, eliminate options, and guess your opponent’s choice first to win!

## Requirements
- Python 3.x

## Setup
1. Download `guess_who.py`.
2. Run it: `python guess_who.py`

## How to Play
1. Pick a character by ID from the list.
2. **Your Turn**:
   - **1: Ask**: Ask a yes/no question (e.g., "Is your character male?"), eliminate IDs.
   - **2: Pick**:
     - Guess the AI’s character by name.
     - Eliminate IDs manually.
3. **AI Turn**: AI asks a question or eliminates a character.
4. Win by guessing correctly!

## Characters
12 characters with attributes (gender, hair color, etc.) in `characters_json`.

## Customization
Edit `characters_json` or `ai_turn` for new characters or smarter AI.

## Limitations
- Basic AI logic.
- Terminal-only.

## License
MIT License