def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    index = 0
    length = len(lst)
    
    # Use while loop as specified
    while index < length:
        # Get current element
        current = lst[index]
        
        # Check if it's a number and negative
        if isinstance(current, (int, float)) and current < 0:
            return current
        
        index += 1
    
    # If no negative found
    return "No negative"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
test = [3, 5, -1, 7, -2, 8]
result = find_first_negative(test)
print(f"List: {test}")
print(f"First negative: {result}")
print()

# - [2, 10, 7, 0]
test = [2, 10, 7, 0]
result = find_first_negative(test)
print(f"List: {test}")
print(f"First negative: {result}")
print()

