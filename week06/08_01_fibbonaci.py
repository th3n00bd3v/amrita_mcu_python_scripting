# wrtie a recursive fibonacci function


def fib(n):
    """
    input: 
        n: int

    return:
        fibbonacci number for n
    """

    if n < 0:
        raise ValueError("Input should be a non-negative integer")
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)

print(fib(6)) #should return 5
print(fib(10)) #should return 34
