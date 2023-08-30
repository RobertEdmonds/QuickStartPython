"""Holds all the functionality for Coffee Shop Simulator"""
def welcome():
    """Welcome to the game statements"""
    print('CyberBank Coffee Shop Simulator 4000\n Version 1.0.0')
    print("Lets collect some information before we start\n")
# Get name and shop name
# 1. Set name and shop_name to False
# 2. Use while not name and shop_name to continue to prompt for a non empty string
def prompt(display="Please input a string", require=True):
    """Help with all the input fields"""
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + ' ')
    return s

def convert_to_float(s):
    """Check if input is a float"""
    # if conversion fails assign 0
    try:
        f = float(s)
    except ValueError:
        f = 0
    return f

def x_of_y(x, y):
    """Gives all the possibilities for the temperature"""
    num_list = []
    # Returns a list of x copies of y
    for i in range(x):
        num_list.append(y)
    return num_list