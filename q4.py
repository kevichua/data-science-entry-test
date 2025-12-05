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

print("=== Test Case 1 ===")
test1 = "Hello World"
result1 = string_reverse(test1)
print(f"Original: '{test1}'")
print(f"Reversed: '{result1}'")
print()

print("=== Test Case 2 ===")
test2 = "Python"
result2 = string_reverse(test2)
print(f"Original: '{test2}'")
print(f"Reversed: '{result2}'")
print()

