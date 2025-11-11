def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        print("Original value:", dct[key])
        dct[key] = value
    else:
        dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

# First scenario
result1 = update_dictionary({}, "name", "Alice")
print("Result 1:", result1)

print("-" * 20)

# Second scenario
result2 = update_dictionary({"age": 25}, "age", 26)
print("Result 2:", result2)
