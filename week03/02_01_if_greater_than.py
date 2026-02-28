# Exercise

# Write a program by accepting 2 numbers from the user and check number is greater than other and print the result
# you can use the function `input()` to get user input

# example
first_number = input("Please enter a number: ")
second_number = input("Please enter another number: ")

print(f"First number: {first_number}")
print(f"Second number: {second_number}")

if first_number > second_number:
    print("first number is greater than second number.")
else:
    print("second number is greater than first number.")

## note, what type is your first_number? Is it what you expected?
## look-up the input() documentation to find out what type it will create by default
