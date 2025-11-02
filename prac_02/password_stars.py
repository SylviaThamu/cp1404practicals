"""
CP1401/CP5632 - Practical
Password check: ask for a password of at least MIN_LENGTH characters,
then print that many stars.
"""

MIN_LENGTH = 6


def main():
    password = get_password(MIN_LENGTH)
    print_stars(password)


def get_password(min_length):
    """Get a password that is at least min_length characters long."""
    password = input("Password: ")
    while len(password) < min_length:
        print(f"Invalid password; must be at least {min_length} characters")
        password = input("Password: ")
    return password


def print_stars(text):
    """Print stars equal to the length of text (no spaces, one line)."""
    print("*" * len(text))


main()
