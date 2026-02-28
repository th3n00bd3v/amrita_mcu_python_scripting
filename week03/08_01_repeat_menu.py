# Exercise

# Write an explicit infinite loop
# inside the infinite loop, read integer from user as an option

# If the option is 1: print here is your first step
# If the option is 2: print "you have some steps to go"
# If the option is 3: print "you are almost done"
# If the option is 4: quit from the loop

# If the option is other number: print it is an  invalid option

user_input = 0
while True:
    user_input = int(input("Enter an option (1-4): "))
    if user_input == 1:
        print("Here is your first step")
    elif user_input == 2:
        print("You have some steps to go")
    elif user_input == 3:
        print("You are almost done")
    elif user_input == 4:
        print("Quitting the loop. Goodbye!")
        break
    else:
        print("It is an invalid option")

