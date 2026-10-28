"""Functions for password utility."""

from email import charset
import secrets
import string

#For Checking password strength

def check_password_strength(password: str) -> bool:
    """Check if the password is strong enough.

    A strong password must be at least 8 characters long and contain at least one uppercase letter,
    one lowercase letter, one digit, and one special character.

    Args:
        password (str): The password to check.
        """
    if len(password) < 8:
        return "Weak Password. It must be at least 8 characters long."

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_character = any(char in string.punctuation for char in password)

    if all([has_uppercase, has_lowercase, has_digit, has_special_character]):
        return "Strong Password."

    return "Weak Password. It must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."


#For generating a random password

def generate_random_password( length : int) -> str:

    """ Generate a random password.

    Args:
        length: Desired length of the password. A minimum length of 8 is recommended for security.

    Returns:
        str: The generated random password.

    Raises:
        ValueError: If the specified length is less than 8.
"""

    if length < 8:
        raise ValueError(
        "Password length should be at least 8 characters for security.")

    charset = string.ascii_letters + string.digits + string.punctuation
    
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ] 

    password.extend(
        secrets.choice(charset) for _ in range(length - 4)
    )

    secrets.SystemRandom().shuffle(password)

    return "".join(password)
