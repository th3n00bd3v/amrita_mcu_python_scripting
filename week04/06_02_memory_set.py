# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

# you will need the `input()` function to collect information from the user

numbers = set()
points_lost = 0

print("Welcome to the Memory Game!")
print("Enter unique numbers.")
print("You lose a point for duplicates.")
print("Lose 5 points and the game is over.")
print("Create more than 10 unique numbers to win!\n")

while True:
    user_input = input("Enter a number: ")

    # Check if input can be converted to integer
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input! Please enter an integer.\n")
        continue

    # Check for duplicate
    if number in numbers:
        points_lost += 1
        print(f"Duplicate! You lost a point. Total points lost: {points_lost}\n")
    else:
        numbers.add(number)
        print(f"Added! Current set: {numbers}\n")

    # Check losing condition
    if points_lost >= 5:
        print("Game Over! You lost 5 points.")
        break

    # Check winning condition
    if len(numbers) > 10:
        print("Congratulations! You win!")
        break