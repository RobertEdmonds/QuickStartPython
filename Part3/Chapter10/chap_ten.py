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
title = "Python QuickStart Guide"
# This is for upper case
print(title.upper())
# this is for lower case
print(title.lower())
