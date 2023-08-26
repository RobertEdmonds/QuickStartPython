"""Arbitrary Arguments"""
# Arbitrary Argument provide a way to specify that a function can receive one or many arguments

# Define the average function
def average(*numbers):
    # To show the argument is arbitrary add the star(*) in-front of the argument
    """Use to get the sum value from a list of numbers"""
    sum = 0
    for n in numbers:
        # Add n to sum
        # (+= means add n to sum and store the sum)
        sum += n
    # len = length of numbers list
    return sum / len(numbers)

# Use our new function
print(average(1, 5, 8, 15, 7, 42, 58, 96, 3))
