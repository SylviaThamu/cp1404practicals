"""
Broken program to determine score status (fixed)
Score must be 0..100 inclusive.
90+ = Excellent, 50–89 = Passable, below 50 = Bad.

function main
    get score as a number
    if score < 0 or score > 100
        display "Invalid score"
    else if score >= 90
        display "Excellent"
    else if score >= 50
        display "Passable"
    else
        display "Bad"

"""

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
