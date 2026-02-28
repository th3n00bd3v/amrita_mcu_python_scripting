# write a short command line game

# 1. ask the user for their name: (use the input() function)

# Say hello to them with their name
# If their name begins with a vowel say something funny about that ("Aha! Oho! Uhu! Ihi! etc", your name begins with a vowel!)
# If their n ame begins with a consonant make an even better joke about it.

# Ask them to pick a number between 1 and 10.
# If they guessed the right number, tell them they won
# Else, tell them they lost.

import random

rand_nos = random.randint(0, 10)

name = input("Please enter your name: ")

print(f"Hello {name}!")

vowel_list = "aeiouAEIOU"

if name[0] in vowel_list:
    print("Your name begins with a vowel!")
else:
    print("Your name begins with a consonant!")

number = int(input("Please pick a number between 1 and 10: "))

if number == rand_nos:
    print("Congratulations! You won!")
else:
    print(f"Sorry, you lost. The number was {rand_nos}.")