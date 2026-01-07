# write a function that takes no arguments

# Define a global variable
message = "Hello from the global scope!"

def no_args():
    """
    Do something here!
    ideas: use a global
    Idea: just print something out
    """
    global message  # Access the global variable
    print(message)  # Print the global message


# call your function down here

    """
    This function takes no arguments and prints a message.
    It also uses a global variable to demonstrate interaction with the global scope.
    """

# Call the function
no_args()
