"""
Write a function that accepts user input with the input() function
Try to convert their input to `int` and catch any exceptions that happen.

what kind of exceptions did you find?

"""

def input_to_int():
    user_input = input("Please enter a number: ")

    try:
        result = int(user_input)
    except ValueError:
        print("ValueError: The entered value is not a valid integer.")
        return None
    else:
        print(f"The integer value is: {result}")
        return result
    
input_to_int()    