"""
rewrite inner_multiple from  Week 8

# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]


Iterate over the args summing them up. 
Use an if statement ot check if the user passed tuples.
Raise an exception if they passed something else
"""


def inner_multiplication(*args):
    result = []

    for item in args:
        if not isinstance(item, tuple):
            raise TypeError(f"Expected tuple, got {type(item).__name__}")

        if len(item) != 2:
            raise ValueError("Each tuple must contain exactly two elements")

        a, b = item
        result.append(a * b)

    return result


a = inner_multiplication((1, 2), (2, 2), (3, 2), (4, 5))
print("a =", a)

# this will raise an exception
b = inner_multiplication((1, 2), (2, 2), (3, 2), (4, 5), [5, 3.0], {4, 2})
print(b)

