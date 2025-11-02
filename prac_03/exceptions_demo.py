"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# 1. A ValueError will occur when the user enters a non-integer value
#    for either the numerator or the denominator (for example, a letter or symbol).

# 2. A ZeroDivisionError will occur when the user enters 0 as the denominator.

# 3. Yes, you could change the code to avoid the ZeroDivisionError by checking
#    if the denominator is zero before performing the division.
#    The updated version below does this using a while loop.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
