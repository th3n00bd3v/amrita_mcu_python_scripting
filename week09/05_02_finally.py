"""
Construct a code sample where you force an error to happen.
Then run it in a try-except-finally block. But, do NOT catch your error! (Or re-raise it)
Print something out in the finally block.
Does it print out? Why?

The main purpose of the finally is to ensure that some safety code / exit condition will run no matter what, even 
if an error happens.

The purpose of this exercise is to just practice observing that
"""

# Answer coded below

def force_error():
    print("About to divide by zero...")
    return 10 / 0  # ZeroDivisionError

try:
    force_error()
except KeyError:
    # Not catching the actual error!
    print("This will never run.")
finally:
    print("FINALLY block executed: cleaning up resources.")

print("This line will never be reached.")
