"""Debugging Python Code"""
x = input("What is x? ")

print(f"x = {x}")

y = input("What is y? ")

print(f"y = {y}")

if x > y:
    print("x > y")
else:
    print("y > x")

debug = True

def debug_msg(msg):
    if debug:
        print(msg)
debug_msg(y)

import logging

logging.basicConfig(
    filename="test.log",
    encoding="utf-8",
    level= logging.DEBUG
)
