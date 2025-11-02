"""
CP1401/CP5632 - Practical
Menu program using functions:
(G)et a valid score (0–100)
(P)rint result (Excellent/Passable/Bad/Invalid)
(S)how stars (print as many '*' as the score)
(Q)uit
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the score menu program."""
    score = get_valid_score()  # get one before menu (as required)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = classify_score(score)
            print(result)
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")


def get_valid_score():
    """Get a score between 0 and 100 inclusive."""
    score_text = input("Enter score (0-100): ")
    # basic numeric check (digits only) then range check
    while not score_text.isdigit():
        print("Invalid input")
        score_text = input("Enter score (0-100): ")
    score = int(score_text)

    while score < 0 or score > 100:
        print("Invalid score")
        score_text = input("Enter score (0-100): ")
        while not score_text.isdigit():
            print("Invalid input")
            score_text = input("Enter score (0-100): ")
        score = int(score_text)
    return score


def classify_score(score):
    """Return the text result for the given score (no printing here)."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
