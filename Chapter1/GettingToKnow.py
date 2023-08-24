# getting_to_know_python
print("Hello, World!")
# This is a variable that is assigned an input function
name = input("What is your name? ")
# The next two lines work the exact same
print(f'Hello {name}!')
print('Hello,' + ' ' + name)
# Slicing
# Returns information from the index in the slice
GREETINGS = "Well, hello there!"
# Starts after first number and ends including last number
HELLO = GREETINGS[6:11]
print(HELLO)
# Numbers and floats
price = input('What is the price of a cup of coffee? ')
cups = input("How many cups do you want? ")
total = float(price) * int(cups)
print(f'Your total is ${total} for {cups} cups')
# Python interpreter runs our Python code
# We can convert between strings, integers and floats
