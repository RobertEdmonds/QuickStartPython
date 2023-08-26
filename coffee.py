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
print('CyberBank Coffee Shop Simulator 4000\n Version 1.0.0')
print("Lets collect some information before we start\n")
# Get name and shop name
# 1. Set name and shop_name to False
# 2. Use while not name and shop_name to continue to prompt for a non empty string
name = False
while not name:
    name = input("What is your name? ")

shop_name = False
while not shop_name:
    shop_name = input(f"What is the name of {name}'s coffee shop? ")

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
    temperature = randint(20, 90)
    # Display cash and weather
    print(f"You have ${cash} cash and it's {temperature} degrees.")
    print(f"You have coffee on hand to make {coffee} cups.")
    # Get the price for the coffee
    print(f"\nThanks, {name}. Let's set some initial pricing.\n")
    cup_price = False
    while not cup_price:
        cup_price = input("What do you want to charger per cup of coffee? ")
        try:
            cup_price = float(cup_price)
            if cup_price == 0:
                print("Your not running a homeless shelter.\nCoffee must be greater than 0")
                cup_price = False
            else:
                cup_price = float(cup_price)
        except Exception as e:
            print(str(e))
            cup_price = False
    else:
        print(f"\nYour first cup of coffee will sell for ${cup_price}.\n")
    print("\nYou can buy advertising to help promote sales")
    # Input on how much user wants to spend on advertisement
    advertise = input("How much would you like to spend on advertisement today (0 is none)? ")
    # convert advertise to a float
    # If it fails, assign it to 0
    try:
        advertise = float(advertise)
    except ValueError as e:
        advertise = 0
    finally:
        # Deduct advertising from cash on hand
        cash -= advertise
    # TODO: Calculate today's performance
    # TODO: Display today's performance

    # Before we loop around add a day
    day += 1
    if day == 2:
        break
