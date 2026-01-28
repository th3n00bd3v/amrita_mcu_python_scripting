## write a function that uses **kwargs as input
## it should print out the sum of all the integers found in the values

"""
input: hi = 2020, bye = 1000, see = 2, def = 'this'
output : 3022

The function should work for any kind of values and as many keyword arguments as the use would like to pass

"""
def integers_sum(**kwargs):
    total = 0
    for value in kwargs.values():
        if isinstance(value, int):
            total += value
    return total

print(integers_sum(hi=2020, bye=1000, see=2, hear='this'))
print(integers_sum(a=10, b='hello', c=5, d=3.5, e=15))