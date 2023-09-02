"""This is code and notes on Chapter 10(Advance Strings)"""

a = "Hello, World!"
# Finding and replacing text

# Use the find method 
# make it a if statement just incase it is empty
if a.find("World") != -1:
    # have it replace world with reader
    b = a.replace("World", "Reader")
    # first is the word you want it to find, second is the replacement

print(f"{a} is replaced with {b}")

# Cases = upper and lower cases
title = "python quickStart guide"
# will separate at every space
title_array = title.split()

for index, word in enumerate(title_array):
    title_array[index] = word.replace(word[0], word[0].upper())
# will join at the comma with a space between
print(" ".join(title_array))
# This is for upper case
print(title.upper())
# this is for lower case
print(title.lower())

# Pattern Counting
tongue_twister = "She sells seashells by the seashore."
# count is great tool for counting what ever the argument is in the function
answer = tongue_twister.lower().count("s")
print(f"There are {answer} letters s in:")
print(tongue_twister)

# Split and joining
number = "112-223-4789"
id = number.split('-')
# split can be run on any string
print(id)
id = "-".join(id)
print(id)

# Input Validations
value = input("Please enter in value: ")
# Check if is a number 
if value.strip().isnumeric():
    print(f"{value} is a number")
# Check if it is alphabetical
if value.strip().isalpha():
    print(f"{value} is a alphabetical")
# Check if alphanumeric
if value.strip().isalnum():
    print(f"{value} is a alphanumeric")

