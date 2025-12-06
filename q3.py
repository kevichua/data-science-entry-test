def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key already exists
    if key in dct:
        print(f"Key '{key}' already exists with value: {dct[key]}")
        # Print the original value as required
        print(f"Original value: {dct[key]}")
    
    # Update the dictionary with the new key-value pair
    dct[key] = value
    
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
print("Scenario: {}, 'name', 'Alice'")
print("Expected: Add new key 'name' with value 'Alice'")
result = update_dictionary({}, "name", "Alice")
print(f"Result: {result}")
print()

# - {"age": 25}, "age", 26
print("Scenario: {'age': 25}, 'age', 26")
print("Expected: Print original value 25, then update to 26")
result = update_dictionary({"age": 25}, "age", 26)
print(f"Result: {result}")
print()
