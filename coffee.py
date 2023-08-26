"""Making a coffee shop game in the terminal"""
# Import item to produce random numbers for the temperature
from random import randint
# Need a list of days that include
    # pricing, advertisement budget, sales, weather
# sales = [
#     {
#         "day": 1,
#         "coffee_inv": 100,
#         "advertising": "10",
#         "temp": 68,
#         "cups_sold": 16
#     },
#     {
#         "day": 2,
#         "coffee_inv": 84,
#         "advertising": "15",
#         "temp": 72,
#         "cups_sold": 20
#     },
#     {
#         "day": 3,
#         "coffee_inv": 64,
#         "advertising": "5",
#         "temp": 78,
#         "cups_sold": 10
#     }
# ]

# Coffee Shop Game
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

def daily_stats(cash_on_hand, weather, coffee_inventory):
    """Display game inventory at beginning of new day"""
    print(f"You have ${cash_on_hand} cash on hand and the temperature is {weather}")
    print(f"You have enough coffee on hand to make {coffee_inventory} cups.")

def convert_to_float(s):
    """Check if input is a float"""
    # if conversion fails assign 0
    try:
        f = float(s)
    except ValueError:
        f = 0
    return f

def get_weather():
    """Get a random number to be used as the weather"""
    return randint(20, 90)
# Print welcome message
welcome()

# Get name and store name
name = prompt("What is your name?")
shop_name = prompt(f"What is the name of {name}'s coffee shop?")

# Display what we have
print("\nGreat. Here's what we've collected so far.\n")
print(f"Your name is {name} and your opening {shop_name}!")
# Start game
print("\nOk, let's get started. Have fun!")
# Day Counter
day = 1
# Starting cash
cash = 100
# Amount of cups of coffee on hand
coffee = 100
# Empty sales list to add dictionary info into
sales = []

running = True
while running:
    # Display the day and add a "fancy" text effect
    print(f"\n-----| Day {day} @ {shop_name} |-----")
    # Generate a random temp between 20 and 90
    temperature = get_weather()
    # Display cash and weather
    daily_stats(cash, temperature, coffee)
    # Get the price for the coffee
    print(f"\nThanks, {name}. Let's set some initial pricing.\n")
    cup_price = prompt("What do you want to charger per cup of coffee?")
    try:
        # checks for cup price
        cup_price = float(cup_price)
        # validates that the cup price is above zero
        if cup_price == 0:
            print("Your not running a homeless shelter.\nCoffee must be greater than 0")
            cup_price = prompt("What do you want to charger per cup of coffee?")
        else:
            cup_price = float(cup_price)
    except ValueError:
        # If there is a value error it will ask you again
        cup_price = prompt("What do you want to charger per cup of coffee?")

    print(f"\nYour first cup of coffee will sell for ${cup_price}.\n")
    print("\nYou can buy advertising to help promote sales")
    # Input on how much user wants to spend on advertisement
    advertise = prompt("How much would you like to spend on advertisement today (0 is none)?", False)
    # convert advertise to a float
    # If it fails, assign it to 0
    advertise = convert_to_float(advertise)
    # Deduct advertising from cash on hand
    cash -= advertise
    # TODO: Calculate today's performance
    # TODO: Display today's performance

    # Before we loop around add a day
    day += 1
    if day == 2:
        break
