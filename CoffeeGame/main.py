"""The main view of the coffee game"""
# pylint: disable=no-name-in-module
# pylint: disable=undefined-variable
# Import all functions from the utility module
from utilities import *

# Import the game class from the coffee_shop_simulator module
from coffee_shop_simulator import CoffeeShopSimulator

# print welcome message
welcome()

# Get name and store name
t_name = prompt("What is your name?")
t_shop_name = prompt(f"What is the name of {t_name}'s coffee shop?")

# Create the game object
game = CoffeeShopSimulator(t_name, t_shop_name)

# Run the game
game.run()
