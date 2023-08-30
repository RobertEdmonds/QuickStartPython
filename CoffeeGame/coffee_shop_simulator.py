"""Runs the Coffee Shop Loop"""
# pylint: disable=undefined-variable
import random
import re
from utilities import *

class CoffeeShopSimulator:
    """Simulator Class for the Coffee Shop game"""

    # Minimum and maximum temperatures
    TEMP_MIN = 20
    TEMP_MAX = 90

    def __init__(self, player_name, shop_name) -> None:
        # Set player and coffee shop names
        self.player_name = player_name
        self.shop_name = shop_name
        # Current day
        self.day = 1
        # Cash on hand
        self.cash = 100
        # Inventory at start
        self.coffee_inventory = 100
        # Sales List
        self.sales = []
        # Possible temperatures
        self.temps = self.make_temp_distribution()

    def run(self):
        """This is the code to run the game"""
        print("\nOk, let's get started. Have fun!")
        # The main game loop
        running = True
        while running:
            # Display the day and add a "fancy" text effect
            self.day_header()

            # Get the Weather
            temperature = self.weather

            # Display the cash and weather
            self.daily_stats(temperature)

            # Get price of a cup of coffee
            cup_price = prompt("What do you want to charger per cup of coffee?")
            restrict = True
            while restrict:
                try:
                    # checks for cup price
                    cup_price = float(cup_price)
                    # validates that the cup price is above zero
                    if cup_price == 0:
                        print("Your not running a homeless shelter.\nCoffee must be greater than 0")
                        cup_price = prompt("What do you want to charger per cup of coffee?")
                    else:
                        cup_price = float(cup_price)
                        break
                except ValueError:
                    # If there is a value error it will ask you again
                    print("Must be a numerical value")
                    cup_price = prompt("What do you want to charger per cup of coffee?")

            # Get advertising spend
            print("\nYou can buy advertising to help promote sales")
            # Input on how much user wants to spend on advertisement
            advertising = prompt(
                "How much would you like to spend on advertisement today (0 is none)?",
                False
            )
            # convert advertise to a float
            # If it fails, assign it to 0
            advertising = convert_to_float(advertising)

            # Deduct advertising from cash on hand
            self.cash -= advertising

            # Simulate today's sales
            cups_sold = self.simulate(temperature, advertising, cup_price)
            gross_profit = cups_sold * cup_price

            # Display the results
            print(f"You sold {cups_sold} cups of coffee today.")
            print(f"You made ${gross_profit}.")

            # Add the profit to our coffers
            self.cash += gross_profit

            # Subtract inventory
            self.coffee_inventory -= cups_sold

            # Before we loop around, add a day
            self.increment_day()

    def simulate(self, temperature, advertising, cup_price):
        """Simulates data for what happened during the day of sales"""
        # Find out how many cups were sold
        cups_sold = self.daily_sales(temperature, advertising)

        # Save the sales data for today
        self.sales.append({
            "day": self.day,
            "coffee_inv": self.coffee_inventory,
            "advertising": advertising,
            "temp": temperature,
            "cup_price": cup_price,
            "cups_sold": cups_sold
        })

        # We technically don't need this, but why make the next step
        # Read from the sales list when we have the data right here
        return cups_sold

    def make_temp_distribution(self):
        """Gets the x and y value on what the temperatures might be"""
        # This is not a good bell curve, but it will do for now
        # until we get to more advanced mathematics
        temps = []

        # First, find the average between TEMP_MIN and TEMP_MAX
        avg = (self.TEMP_MIN + self.TEMP_MAX) / 2
        # Find the distance between TEMP_MAX and TEMP_MIN and the average
        max_dist_from_avg = self.TEMP_MAX - avg

        # Loop through all possible temperatures
        for i in range(self.TEMP_MIN, self.TEMP_MAX):
            # How far away is the temperature from average?
            # abs() gives us the absolute values
            dist_from_avg = abs(avg - i)
            # How far away is the dist_from_max from the maximum?
            # This will be lower for temps at the extremes
            dist_from_max_dist = max_dist_from_avg - dist_from_avg
            # If the distance is zero make it one
            if dist_from_max_dist == 0:
                dist_from_max_dist = 1
            # Append the output of x_of_y to temps
            for t in x_of_y(int(dist_from_max_dist), i):
                temps.append(t)
        return temps

    def increment_day(self):
        """Adds one to the days"""
        self.day += 1

    def daily_stats(self, temperature):
        """Display game inventory at beginning of new day"""
        print(f"You have ${self.cash} cash on hand and the temperature is {temperature}.")
        print(f"You have enough coffee on hand to make {self.coffee_inventory} cups.")

    def day_header(self):
        """Displays New Day Header"""
        print(f"\n-----| Day {self.day} @ {self.shop_name} |-----")

    def daily_sales(self, temperature, advertising):
        """Returns how many sales were made that day"""
        return int((self.TEMP_MAX - temperature)*(advertising * .5))

    @property
    def weather(self):
        """Provides a random temperature for a day"""
        # Generate a random temperature between 20 and 90
        # We'll consider seasons later on, but this is good enough for now
        return random.choice(self.temps)
