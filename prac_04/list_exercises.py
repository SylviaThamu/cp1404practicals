"""
CP1404/CP5632 - Practical
List exercises: basic list operations and security check

Pseudocode:
get 5 numbers from user and store in a list
display first number
display last number
display smallest number
display largest number
display average of numbers

get username
if username in list
    display "Access granted"
else
    display "Access denied"
"""


def main():
    """Get numbers and display statistics, then check usernames."""
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

    check_username()


def check_username():
    """Check if username is authorised."""
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
        'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
    ]

    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
