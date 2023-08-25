"""Making a coffee shop game in the terminal"""
# Day Counter
day = 1
# Empty sales list to add dictionary info into
sales = []
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
name = input("What is your name? ")
shop_name = input(f"What is the name of {name}'s coffee shop? ")

print(f"\nThanks, {name}. Let's set some initial pricing.\n")
# Get initial price of a cup of coffee
cup_price = input("What do you want to charger per cup of coffee? ")

# Display what we have
print("\nGreat. Here's what we've collected so far.\n")
print(f"Your name is {name} and your opening {shop_name}!")
print(f"Your first cup of coffee will sell for ${cup_price}.\n")
