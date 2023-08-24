# Excercise for Chapter One

# Slicing exercise
# name = input('What is your name? ')
# print(name[:1])
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