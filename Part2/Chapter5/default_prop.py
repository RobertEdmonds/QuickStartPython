"""Default Arguments"""
# Provide a default value for an argument in case the code that calls it doesn't specify an argument

# Create an ask function with a default argument
def ask(prompt = "Please enter a value:"):
    # Arguments that don't have a default value are required arguments
    """Use instead of the input function"""
    if prompt.endswith(' '):
        return input(prompt)
    else:
        return input(prompt + " ")
print(ask())
