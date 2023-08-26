"""Keyword Arguments"""
# Keyword arguments do not depend on the order the argument is provided

def full_name(first, middle, last, display = False):
    """Get users full name"""
    name = f"{first} {middle} {last}"
    if display:
        print(name)
    return name
# When using keyword argument you just have to change how you calling the function
print(full_name(first="Robert", last="Floyd", middle="Tom"))
# Instead of relying on there position we added the keyword in-front of the argument
# While calling a keyword argument function we should use a key word for all the arguments
