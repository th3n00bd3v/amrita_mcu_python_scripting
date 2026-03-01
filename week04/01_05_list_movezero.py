# Exercise

# Write a program to move all zero digits to end of a given list of numbers
# Expected output:
# Original list:

# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:

# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

original_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
non_zero_list = []
for number in original_list:
    if number != 0:
        non_zero_list.append(number)
zero_count = original_list.count(0)
result_list = non_zero_list + [0] * zero_count

print(f"Original list: {original_list}")
print(f"Result list: {result_list}")