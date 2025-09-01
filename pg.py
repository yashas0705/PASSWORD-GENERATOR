import string
import secrets

def generate_password(length=16, use_upper=True, use_digits=True, use_specials=True):
    """Generate a secure password with given options.

    Args:
        length (int): Length of the password.
        use_upper (bool): Include uppercase letters.
        use_digits (bool): Include digits.
        use_specials (bool): Include special characters.

    Returns:
        str: The generated password.
    """
    characters = list(string.ascii_lowercase)

    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_specials:
        characters += list("!@#$%^&*()-_=+[]{};:,.<>?")

    if not characters:
        raise ValueError("No characters available for password generation!")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated Password:", generate_password())
