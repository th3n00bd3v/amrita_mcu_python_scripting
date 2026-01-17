# write a recursive function to calculate the factorial

def factorial(n):
    """
    input: 
        n: int
    returns: 
        factorial of n
    
    reminder: factorial 8! is
    8*7*6*5*4*3*2*1
    """
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

    
for number in range (0,10):
    print(f"{number}! = {factorial(number)}")


    