"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    """Ask for a score, print result, and also generate a random score result."""
    score = float(input("Enter score: "))
    print(get_result(score))

    # New part: random score
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} - {get_result(random_score)}")


def get_result(score):
    """Return result string for a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
