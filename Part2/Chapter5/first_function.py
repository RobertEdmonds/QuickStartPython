"""Our First Function"""
# Function are to reuse code across the entire platform
# Functions is a subset of the Python file

# Define the ask function
    # A function is defined with the def command
def ask(prompt):
    """This is to simplify the input function"""
    return input(prompt + ' ')

# Use the ask function to find out how many cups we want
# question = ask("How many cups do you want?")
# print(question)
# simplify 
print(ask("How many cups would you like?"))
