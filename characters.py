import json

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