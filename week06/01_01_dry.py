# convert the following code into a function
# your function should take a single list as input
# it should return a list with only the even numbers from the input list

numbers = [2, 1, 3, 5, 1, 2, 3, 12, 3, 45, 1, 2, 3]

div_2 = []
for i in numbers:
    if i % 2 == 0:
        div_2.append(i)
print(div_2)

other_numbers = [213, 2, 3, 125, 12, 32, 21, 3, 6, 23, 12, 3, 326, 45, 12, 32, 14, 2]
new_div_2 = []
for i in numbers:
    if i % 2 == 0:
        new_div_2.append(i)

print(new_div_2)

# Answer

def even_nos(numbers):
    div_two = []
    for new_list in numbers:
        if new_list % 2 == 0:
            div_two.append(new_list)
    return div_two

nos1 = [2, 1, 3, 5, 1, 2, 3, 12, 3, 45, 1, 2, 3]
nos2 = [213, 2, 3, 125, 12, 32, 21, 3, 6, 23, 12, 3, 326, 45, 12, 32, 14, 2]

print(even_nos(nos1))
print(even_nos(nos2))

