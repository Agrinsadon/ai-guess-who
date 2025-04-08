import json

# JSON data for characters
characters_json = '''
{
  "characters": [
    {"id": 1, "name": "Alice", "attributes": {"glasses": true, "hat": false, "beard": false}},
    {"id": 2, "name": "Bob", "attributes": {"glasses": false, "hat": true, "beard": true}},
    {"id": 3, "name": "Carol", "attributes": {"glasses": true, "hat": true, "beard": false}},
    {"id": 4, "name": "David", "attributes": {"glasses": false, "hat": false, "beard": true}},
    {"id": 5, "name": "Eve", "attributes": {"glasses": false, "hat": false, "beard": false}}
  ]
}
'''

# Load characters
data = json.loads(characters_json)
characters = data["characters"]
