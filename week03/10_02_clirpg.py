# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.

# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

print("Welcome to the Dungeon Adventure!")
name = input("What is your name, brave adventurer? ")

print(f"\nGreetings, {name}! You find yourself in a mysterious dungeon.")
print("In front of you are two doors.")

has_sword = False
game_over = False

while not game_over:
    print("\nDo you choose the LEFT door or the RIGHT door? (left/right)")
    choice = input("> ").lower()

    if choice == "left":
        print("\nYou enter the left room. It seems empty.")

        while True:
            print("\nWhat would you like to do?")
            print("1. Look around")
            print("2. Go back")
            action = input("> ")

            if action == "1":
                if not has_sword:
                    print("\nYou look around and find a shiny sword!")
                    print("Do you want to take it? (yes/no)")
                    take = input("> ").lower()

                    if take == "yes":
                        has_sword = True
                        print("\nYou picked up the sword.")
                    else:
                        print("\nYou leave the sword behind.")
                else:
                    print("\nThere is nothing else in this room.")

            elif action == "2":
                print("\nYou go back to the main room.")
                break
            else:
                print("\nInvalid choice.")

    elif choice == "right":
        print("\nYou enter the right room and see a dragon!")

        while True:
            print("\nWhat would you like to do?")
            print("1. Fight the dragon")
            print("2. Go back")
            action = input("> ")

            if action == "1":
                if has_sword:
                    print("\nYou fight the dragon with your sword and win!")
                    print("Congratulations! You defeated the dragon!")
                else:
                    print("\nYou try to fight the dragon without a weapon.")
                    print("The dragon eats you. Game over.")
                game_over = True
                break

            elif action == "2":
                print("\nYou go back to the main room.")
                break
            else:
                print("\nInvalid choice.")

    else:
        print("\nInvalid choice. Please type 'left' or 'right'.")