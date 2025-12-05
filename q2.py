def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if lst is actually a list
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    
    # Create a new list with replaced values
    result = []
    for item in lst:
        if item == find_val:
            result.append(replace_val)
        else:
            result.append(item)
    
    return result


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:

# Test case 1: Replace integers
test1 = [1, 2, 3, 4, 2, 2]
result1 = find_and_replace(test1, 2, 5)
print(f"Original: {test1}")
print(f"After replacing 2 with 5: {result1}")
print()

# Test case 2: Replace strings
test2 = ["apple", "banana", "apple"]
result2 = find_and_replace(test2, "apple", "orange")
print(f"Original: {test2}")
print(f"After replacing 'apple' with 'orange': {result2}")
print()

