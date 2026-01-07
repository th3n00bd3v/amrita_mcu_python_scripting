"""
experiment with the function below
1. run the script as is. What prints out? Are you surprised?
2. Modify the function so that x becomes a local variable. There are two ways to do this.
   a. pass x into the function through the arguments
   b. create a new x variable inside the function.
3. After modifying the function, is the x inside the function the same as the x outside? Are they different? Why or why not?
"""
x = 100


def add_to_me(num):
    y = num + x
    print(f"x inside the function is: {x}")
    return y


z = add_to_me(10)
print(z)

print(x)  # what do you think will print out? Answer: This will print z as 110 and x as 100.

# 2. a.


def add_to_me(num, x):
    y = num + x
    print(f"x inside the function is: {x}")
    return y

z = add_to_me(10, x)
print(z)

print(x) 

'''
In this version, x is now explicitly passed as an argument when calling the function add_to_me(10, x). 
Inside the function, x is treated as a local variable, and it prints the same value as passed to it (which is the global x).
'''

# b.

x = 100

def add_to_me(num):
    x = 200  # New local variable
    y = num + x
    print(f"x inside the function is: {x}")
    return y

z = add_to_me(10)
print(z)

print(x)

'''
Here, a new x is created within the function and set to 200. This local variable shadows the global x within the function scope. 
The output will be: 210 for z and 100 for x.
'''
