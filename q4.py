def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if s is actually a string
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    
    # Method 1: Using slicing (most Pythonic)
    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"

test = "Hello World"
result = string_reverse(test)
print(f"Original: '{test}'")
print(f"Reversed: '{result}'")
print()

# - "Python"
test = "Python"
result = string_reverse(test)
print(f"Original: '{test}'")
print(f"Reversed: '{result}'")
print()

