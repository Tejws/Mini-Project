import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters  # includes both uppercase and lowercase letters

    if include_digits:
        characters += string.digits

    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_password()
print("Generated Password:", password)
