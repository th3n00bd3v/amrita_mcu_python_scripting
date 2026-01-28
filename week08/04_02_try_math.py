""""
import the random library and use it to automatically generate a random list of numbers
You should generate 1000 random numbers.


"""
import random
random_numbers = [random.randint(1, 100) for _ in range(1000)]

random_output = print(random_numbers)