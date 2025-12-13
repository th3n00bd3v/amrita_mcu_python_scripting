# rewrite your function from the previous exercise (01_01_dry.py)
# this time your function should be able change the divisible by number.

# I should be able to return the list of numbers which is divisible by "n", where
# 'n' can be any number.

## Input: a list of integers, a number 'n'
## output: a new list that only has retains numbers which are divisible by n

# Answer

def even_nos(numbers,k):
    div_two = []
    for new_list in numbers:
        if new_list % k == 0:
            div_two.append(new_list)
    return div_two

k = int(input("Enter the value of k: "))

nos1 = [2, 1, 3, 5, 1, 2, 3, 12, 3, 45, 1, 2, 3]
nos2 = [213, 2, 3, 125, 12, 32, 21, 3, 6, 23, 12, 3, 326, 45, 12, 32, 14, 2]

newlist01 = even_nos(nos1,k)
print(newlist01)
newlist02 = even_nos(nos2,k)
print(newlist02)
