import json
import os

def my_function():
    x = 10
    y = 20
    # This print statement is fine, but we imported 'json' and didn't use it.
    # The quality checker should warn us about "Unused Imports".
    print(f"The sum is {x + y}")

if __name__ == "__main__":
    my_function()
