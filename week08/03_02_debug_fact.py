## DEBUG THIS CODE


def h_fact(n):
    
    ## Added input validation for n =< 0 and raised exception for the same
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    if n == 1:
        return 0
    else:
        return n - 2 * h_fact(n - 1)


h_fact(10)


