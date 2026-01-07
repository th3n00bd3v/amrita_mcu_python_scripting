# write a function that has more than one return statement


def greater_than_x(n, x):
    """
    input:
       n: int
       x: int
    returns:
       True if n > x
       False otherwise
    """

    if n>x:
        return True
    return False


### Extra credit
# Is it required to use the else block? Can you write the above code with only the if statement but no else?

'''
Answer: It's not strictly necessary to use the 'else' block. 
The same result can be achieved with just an 'if' statement followed by an implicit 'return'.
'''
