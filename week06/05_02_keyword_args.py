## Write a function with keyword arguments
## your function can be a mix of positional and keyword arguments
## it must use a default value for the keyword argument.


def rectangle(length,width=10):
    """
    Input:
        length: int
        width: int, defaults to 10
        
    Returns:
        the area of the rectangle
    """
    return f"The area of the rectangle is {length*width} m2"


# Calling the function with the default width
area1 = rectangle(5)
print(area1)  # Output: The area of the rectangle is 50 m²

# Calling the function with a custom width
area2 = rectangle(5, 4)
print(area2)  # Output: The area of the rectangle is 20 m²
