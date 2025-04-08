import random

def ai_turn(remaining_chars, player_character):
    if len(remaining_chars) == 1:
        return remaining_chars, True

    attr_counts = {"glasses": 0, "hat": 0, "beard": 0}
    for char in remaining_chars:
        for attr in attr_counts:
            if char["attributes"].get(attr):
                attr_counts[attr] += 1

    best_attr = max(attr_counts, key=lambda k: min(attr_counts[k], len(remaining_chars) - attr_counts[k]))
    player_value = player_character["attributes"].get(best_attr, False)
    remaining_chars = [c for c in remaining_chars if c["attributes"].get(best_attr) == player_value]
    return remaining_chars, False
