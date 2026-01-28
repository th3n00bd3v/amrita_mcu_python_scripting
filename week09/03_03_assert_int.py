"""
write a function that asks for user input with the input() function
Ask them to create a password that is greater than >6 and <12 characters long ( 6< pwd < 12)

Use an assert statement to validate their password choice

"""

def user_password():
    pwd = input("Please enter a password (6-12 characters long): ")
    assert 6 < len(pwd) < 12, "Password must be greater than 6 and less than 12 characters long."
    return pwd

password = user_password()
print("Your password is set.")
