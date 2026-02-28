# write rock-paper-scissors game

# have the user play against the computer
# you can use the random library to select an option for the computer

# use a while loop so the user can play until they win
import random

# you can map each of rock / paper / scissors to an integer from 1 - 3

print("Welcome to Rock, Paper, Scissors!")
print("1 - Rock")
print("2 - Paper")
print("3 - Scissors")

while True:
    computer_choice = random.randint(1, 3)
    user_choice = int(input("\nEnter your choice (1-3): "))

    if user_choice < 1 or user_choice > 3:
        print("Invalid choice. Game will start again.")
        break

    print(f"Computer chose: {computer_choice}")

    # Tie
    if user_choice == computer_choice:
        print("It's a tie! Try again.")

    # Winning conditions
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win! 🎉")
        break

    # Losing condition
    else:
        print("You lose! Try again.")