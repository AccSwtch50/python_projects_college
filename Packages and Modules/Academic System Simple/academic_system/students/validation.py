def validate_name(name):
    if len(name) > 100:
        return False
    letters = []
    for letter_index in range(0, 26):
        letters.append(chr(ord("a") + letter_index))
    if not set(name.lower()).issubset(set(letters)):
        return False
    return True