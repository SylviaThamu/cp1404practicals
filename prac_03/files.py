"""
CP1404/CP5632 - Practical
Files exercises
"""

# 1. Ask the user for their name, then write it to name.txt
#    Use open and close for this question.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from name.txt and print: Hi Bob!
#    Use open and close for this question.
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. Read only the first two numbers in numbers.txt, add them, print the total
#    Use with instead of open and close for this question.
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    total = number1 + number2
print(total)

# 4. Print the total for all lines in numbers.txt
#    Works for any number of numbers.
#    Use with instead of open and close for this question.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
