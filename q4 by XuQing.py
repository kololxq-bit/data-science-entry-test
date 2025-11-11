def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    return s[::-1]    #the slicing syntax has supported an optional third “step” or “stride” argument

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print(string_reverse("Hello World"))    #Will return "dlroW olleH"
print(string_reverse("Python"))         #Will return "nohtyP"
