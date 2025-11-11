def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    try:
        # Try to perform the modulo operation
        return num % divisor == 0
    except:
        #return error if argument is not numeric
        return str('not numeric')

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print(check_divisibility(10, 2))  # True
print(check_divisibility(7, 3))   # False
