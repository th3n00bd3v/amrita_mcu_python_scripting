"""
Write a function that accepts user input with the input() function
Specify that they must use alphabet characters only.
Then raise an exception if they enter anything that is not able an alphabet character!

Hint: you can use .isalpha() to check if a character is an alpha character.
"""

def check_user_input():
    user_input = input("Enter your name: ").strip()
    if not user_input.replace(" ", "").isalpha():
        raise ValueError("Input must contain alphabets only!")
    return f"Hello, {user_input}!"

try:
    print(check_user_input())
except ValueError as e:
    print(f"Error: {e}")
