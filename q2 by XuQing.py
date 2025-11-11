def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
new_list = []
    
    # Simple loop through each item
    for item in lst:
        if item == find_val:
            new_list.append(replace_val)
        else:
            new_list.append(item)
    
    return new_list
    


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

# First scenario
numbers = [1, 2, 3, 4, 2, 2]
result_numbers = find_and_replace(numbers, 2, 5)
print("Numbers result:", result_numbers)

# Second scenario  
fruits = ["apple", "banana", "apple"]
result_fruits = find_and_replace(fruits, "apple", "orange")
print("Fruits result:", result_fruits)
