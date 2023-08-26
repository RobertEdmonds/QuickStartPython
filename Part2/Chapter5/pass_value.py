"""Passing Values and Returning Results"""
# Argument is a value we pass to a function

# Define the function full_name
def full_name(first, middle, last, display):
    """This is to get the full name of the user"""
    name = f"{first} {middle} {last}"
    if display:
        print(name)
    return name

# Use our newly created function
full_name("Robert", "T", "Edmonds", True)
complete_name = full_name("Bobby", "", "Edmonds", False)
print(complete_name)
