def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise TypeError("Both num and divisor must be numeric (int or float)")
    
    # Check for division by zero
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    
    # Check divisibility using modulo operator
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
result = check_divisibility(10, 2)
print(f"check_divisibility(10, 2) = {result}")
print()

# - 7, 3
result = check_divisibility(7, 3)
print(f"check_divisibility(7, 3) = {result}")
print()

