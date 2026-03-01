# Exercise

# Write a program to create a dictionary from a string.
# Track the count of the letters from the string.
# Sample string : 'securecoding'
# Expected output: {'s': 1, 'e': 2, 'c': 2, 'u': 1, 'r': 1, 'o': 1, 'd': 1, 'i': 1, 'n': 1, 'g': 1}


string_input = 'securecoding'
letter_count = {}

for letter in string_input:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)