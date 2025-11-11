def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
  if type(x) not in (int, float, complex) or type(y) not in (int, float, complex):
        return -1
    else:
        # Swap x & y using arithmetic operations (no temporary variables)
        x = x + y
        y = x - y
        x = x - y

        # Print the swapped values if numeric
        print("swapped x =", x)
        print("swapped y =", y)
        
        return x, y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

swap("Apple", 10)
swap(9, 17)
