"""
CP1404/CP5632 - Practical
Random numbers
Demonstrates the use of the random module.
"""

import random

# Line 1
print(random.randint(5, 20))
# Smallest number possible: 5
# Largest number possible: 20

# Line 2
print(random.randrange(3, 10, 2))
# Possible values: 3, 5, 7, 9
# Smallest number possible: 3
# Largest number possible: 9
# Could line 2 have produced a 4? No

# Line 3
print(random.uniform(2.5, 5.5))
# Smallest number possible: 2.5
# Largest number possible: 5.5

# Code to produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))
