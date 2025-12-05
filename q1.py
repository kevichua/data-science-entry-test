def swap(x, y):
    #Swap using a temp variable
    temp = x
    x = y
    y = temp
    return x, y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

# Task 2a
a = "Apple"
b = 10
a, b = swap(a, b)
print(f"a = {a}, b = {b}")  # Output: a = 10, b = Apple
   
# Task 2b
a = 9
b = 17
a, b = swap(a, b)
print(f"a = {a}, b = {b}")  # Output: a = 17, b = 9


