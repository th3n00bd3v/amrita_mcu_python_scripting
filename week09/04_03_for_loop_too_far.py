"""
Wrap the code below in a try - except
What is the correct exception to use?

Fix the error by "padding" the word with blank spaces (or - dashes) when the exception is hit.
"""

word = "abcde"

for i in range(12):
    try:
        print(i + 1, word[i])

    except IndexError:
        print(i + 1, "-")

    else:  # runs only if no exception
        print(f"As per now, you have {i} letters")

    finally:
        padded_word = word.ljust(i + 1, "-")
        print(f"Your final word is '{i},{padded_word}'")
